prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT BCompY CLOSE")
    prg.add(2000, "DAC BCompY", 2.0000)
    prg.add(100000, "DAC MT-MOT Current", 0.0000)
    prg.add(200000, "Config Field_HelmUp")
    prg.add(210000, "MT Current Ramp", start_t=0, stop_x=20, n_points=100, start_x=0, stop_t=50)
    prg.add(1000000, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=20, stop_t=50)
    prg.add(2000000, "Config Field MT_helmDown")
    prg.add(2010000, "MT Current Ramp", start_t=0, stop_x=20, n_points=100, start_x=0, stop_t=50)
    prg.add(2810000, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=20, stop_t=50)
    prg.add(3810000, "Config Field_HelmUp")
    prg.add(3820000, "MT Current Ramp", start_t=0, stop_x=15, n_points=50, start_x=0, stop_t=25)
    prg.add(4320000, "MT Current Ramp", start_t=0, stop_x=0, n_points=50, start_x=15, stop_t=25)
    prg.add(4820000, "Config Field MT_helmDown")
    prg.add(4830000, "MT Current Ramp", start_t=0, stop_x=10, n_points=50, start_x=0, stop_t=25)
    prg.add(5330000, "MT Current Ramp", start_t=0, stop_x=0, n_points=50, start_x=10, stop_t=25)
    prg.add(6030000, "Config Field_HelmUp")
    prg.add(6040000, "MT Current Ramp", start_t=0, stop_x=7.5, n_points=25, start_x=0, stop_t=20)
    prg.add(6440000, "MT Current Ramp", start_t=0, stop_x=0, n_points=25, start_x=7.5, stop_t=20)
    prg.add(6840000, "Config Field MT_helmDown")
    prg.add(6850000, "MT Current Ramp", start_t=0, stop_x=5, n_points=25, start_x=0, stop_t=20)
    prg.add(7250000, "MT Current Ramp", start_t=0, stop_x=0, n_points=25, start_x=5, stop_t=20)
    prg.add(7650000, "Config Field_HelmUp")
    prg.add(7670000, "MT Current Ramp", start_t=0, stop_x=2, n_points=20, start_x=0, stop_t=20)
    prg.add(8071000, "MT Current Ramp", start_t=0, stop_x=0, n_points=20, start_x=2, stop_t=20)
    prg.add(8471000, "Config Field MT_helmDown")
    prg.add(8491000, "MT Current Ramp", start_t=0, stop_x=1, n_points=20, start_x=0, stop_t=20)
    prg.add(8892000, "MT Current Ramp", start_t=0, stop_x=0, n_points=20, start_x=1, stop_t=20)
    prg.add(9292000, "Config Field_HelmUp")
    prg.add(9302000, "MT Current Ramp", start_t=0, stop_x=0.5, n_points=20, start_x=0, stop_t=20)
    prg.add(9703000, "MT Current Ramp", start_t=0, stop_x=0, n_points=20, start_x=0.5, stop_t=20)
    prg.add(10103000, "Config Field MT_helmDown")
    prg.add(10113000, "MT Current Ramp", start_t=0, stop_x=0.2, n_points=20, start_x=0, stop_t=20)
    prg.add(10514000, "MT Current Ramp", start_t=0, stop_x=0, n_points=1, start_x=0.2, stop_t=20)
    prg.add(11514000, "Config field OFF")
    prg.add(11524000, "DAC BCompY", 0.0000)
    prg.add(11714000, "IGBT BcompY OPEN")
    return prg
