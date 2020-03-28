import os
import pytest

from anasymod.analysis import Analysis
from argparse import ArgumentParser

from time import sleep
from math import exp

root = os.path.dirname(__file__)
SIMULATOR = 'icarus' if 'FPGA_SERVER' not in os.environ else 'vivado'

def test_rc_sim(simulator_name=SIMULATOR):
    # create analysis object
    ana = Analysis(input=root,
                   simulator_name=simulator_name)
    # generate functional models
    ana.msdsl.models()
    # setup project's filesets
    ana.setup_filesets()
    # run the simulation
    ana.simulate()

@pytest.mark.skipif(
    'FPGA_SERVER' not in os.environ,
    reason='The FPGA_SERVER environment variable must be set to run this test.'
)
def test_rc_emu(gen_bitstream=True):
    # create analysis object
    ana = Analysis(input=root)
    # generate functional models
    ana.msdsl.models()
    ana.setup_filesets()
    ana.set_target(target_name='fpga')      # set the active target to 'fpga'

    if gen_bitstream:
        ana.build()                         # generate bitstream for project

    ctrl = ana.launch(debug=True)           # start interactive control

    # routine to pulse clock
    def pulse_clock():
        ctrl.set_param(name='go_vio', value=0b1)
        sleep(0.1)
        ctrl.set_param(name='go_vio', value=0b0)
        sleep(0.1)

    # reset emulator
    ctrl.set_reset(1)
    sleep(0.1)
    ctrl.set_reset(0)
    sleep(0.1)

    # reset everything else
    ctrl.set_param(name='go_vio', value=0)
    ctrl.set_param(name='rst_vio', value=1)
    ctrl.set_param(name='v_in', value=1.0)

    # pulse the clock
    pulse_clock()

    # release from reset
    ctrl.set_param(name='rst_vio', value=0)
    sleep(0.1)

    # walk through simulation values
    t_sim = 0.0
    tau = 1.0e-6
    abs_tol = 1e-3
    for _ in range(25):
        # get readings
        ctrl.refresh_param('vio_0_i')
        v_out = ctrl.get_param('v_out')

        # print readings
        print(f't_sim: {t_sim}, v_out: {v_out}')

        # check results
        meas_val = v_out
        expt_val = 1.0 - exp(-t_sim / tau)
        assert (expt_val - abs_tol) <= meas_val <= (expt_val + abs_tol), 'Measured value is out of range.'

        # pulse clock
        pulse_clock()

        # update the time variable
        t_sim += 0.1e-6

    # declare success
    print('Success!')

if __name__ == "__main__":
    # parse command-line arguments
    parser = ArgumentParser()
    parser.add_argument('--sim', action='store_true')
    parser.add_argument('--emulate', action='store_true')
    parser.add_argument('--gen_bitstream', action='store_true')
    parser.add_argument('--simulator_name', type=str, default=None)
    args = parser.parse_args()

    # run actions as requested
    if args.sim:
        print('Running simulation...')
        test_rc_sim(simulator_name=args.simulator_name)
    if args.emulate:
        print('Running emulation...')
        test_rc_emu(gen_bitstream=args.gen_bitstream)
