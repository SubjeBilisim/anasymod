import os

from glob import glob

from anasymod.sim.sim import Simulator
from anasymod.util import call

class IcarusSimulator(Simulator):
    def simulate(self):
        # build up the simulation command
        cmd = [self.cfg.icarus_config.iverilog, '-g2012', '-o', self.cfg.icarus_config.output, '-s',
               self.cfg.top_module]

        # add defines
        for define in self.cfg.sim_verilog_defines:
            cmd.extend(['-D', define])

        # add include directories
        inc_dirs = set()
        for header in self.cfg.sim_verilog_headers:
            for file in glob(header):
                inc_dirs.add(os.path.dirname(file))

        for inc_dir in inc_dirs:
            cmd.extend(['-I', inc_dir])

        # add source files
        for src in self.cfg.sim_verilog_sources:
            cmd.extend(glob(src))

        # run iverilog
        call(cmd, cwd=self.cfg.build_dir)

        # run vvp
        call([self.cfg.icarus_config.vvp, self.cfg.icarus_config.output], cwd=self.cfg.build_dir)