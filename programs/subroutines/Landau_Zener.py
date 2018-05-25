prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(-50000, "Relay BCompZ Invert")
    prg.add(0, "IGBT Bcompz field OPEN")
    prg.add(100000, "IGBT BCompz field CLOSE")
    prg.add(100100, "BCompZ current ramp", start_t=0, stop_x=10, n_points=20, start_x=0, stop_t=10)
    prg.add(400000, "BCompZ current ramp", start_t=0, stop_x=9, n_points=100, start_x=10, stop_t=100)
    prg.add(680000, "RF Landau-Zener LUT", 14)
    prg.add(680500, "RF Landau-Zener LUT", 500)
    prg.add(1220000, "RF Landau-Zener LUT", 0)
    prg.add(1450000, "BCompZ current ramp", start_t=0, stop_x=0.270, n_points=10, start_x=9, stop_t=10, functions=dict(stop_x=lambda x: cmd.get_var('bfin'), funct_enable=False))
    prg.add(1898000, "RF Landau-Zener LUT", 1000, enable=False)
    prg.add(1899000, "RF Landau-Zener LUT", 541, enable=False)
    prg.add(1899900, "Oscilloscope Trigger ON")
    prg.add(1900000, "RF Landau-Zener ON", enable=False)
    prg.add(1900070, "RF Landau-Zener OFF", functions=dict(time=lambda x: 190+cmd.get_var('pulse'), funct_enable=False), enable=False)
    prg.add(1902020, "RF Landau-Zener OFF", enable=False)
    prg.add(1902047, "Oscilloscope Trigger OFF")
    prg.add(1905047, "RF Landau-Zener LUT", 0)
    return prg