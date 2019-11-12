from anasymod.enums import FPGASimCtrl

class PYNQ_Z1():
    """
    Container to store PYNQ_Z1 FPGA board specific properties.
    """
    clk_pin = ['H16']
    clk_io = 'LVCMOS33'
    clk_freq = 125e6
    full_part_name = 'xc7z020clg400-1'
    short_part_name = 'xc7z020'
    dbg_hub_clk_freq = 100e6
    fpga_sim_ctrl = [FPGASimCtrl.UART_ZYNQ, FPGASimCtrl.VIVADO_VIO]

class TE0720():
    """
    Container to store PYNQ_Z1 FPGA board specific properties.
    """
    clk_pin = ['F7']
    clk_io = 'LVCMOS33'
    clk_freq = 33.333333e6
    full_part_name = 'xc7z020clg484-1'
    short_part_name = 'xc7z020'
    fpga_sim_ctrl = [FPGASimCtrl.UART_ZYNQ, FPGASimCtrl.VIVADO_VIO]

class VC707():
    """
    Container to store VC707 FPGA board specific properties.
    """
    clk_pin = ['E19', 'E18']
    clk_io = 'LVDS'
    clk_freq = 200e6
    full_part_name = 'XC7VX485T-2FFG1761C'
    short_part_name = 'XC7VX485T'
    dbg_hub_clk_freq = 100e6
    fpga_sim_ctrl = [FPGASimCtrl.VIVADO_VIO]

class ZC702():
    """
    Container to store ZC702 FPGA board specific properties.
    """
    clk_pin = ['D18', 'C19']
    clk_io = 'LVDS_25'
    clk_freq = 200e6
    full_part_name = 'xc7z020clg484-1'
    short_part_name = 'xc7z020'
    dbg_hub_clk_freq = 100e6
    fpga_sim_ctrl = [FPGASimCtrl.VIVADO_VIO]

class ULTRA96():
    """
    Container to store ULTRA96 FPGA board specific properties.
    """
    clk_pin = ['L19', 'L20']
    clk_io = 'LVDS'
    clk_freq = 26e6
    full_part_name = 'xczu3eg-sbva484-???'
    short_part_name = 'xczu3eg'
    fpga_sim_ctrl = [FPGASimCtrl.UART_ZYNQ, FPGASimCtrl.VIVADO_VIO]