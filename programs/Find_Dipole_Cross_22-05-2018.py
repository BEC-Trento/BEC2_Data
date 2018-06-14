prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0, enable=False)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(5181000, "DAC Horiz IR", 5.4000)
    prg.add(5181500, "DAC Vert IR", 6.0000)
    prg.add(5182000, "AOM IR Horizontal freq", 80.00)
    prg.add(5182500, "AOM IR Vertical freq", 80.00)
    prg.add(145082000, "Bright_Compressed_MOT", enable=False)
    prg.add(145090000, "switch off MOT _ Depumper ", enable=False)
    prg.add(145090000, "switch off MOT fast")
    prg.add(145092849, "GM BrokenRamp_Short")
    prg.add(145102849, "DAC BCompZ", 0.2400, enable=False)
    prg.add(145152849, "Config Field MT")
    prg.add(145352849, "Evaporation Ramp.sub")
    prg.add(245352849, "[VOID] End Evaporation")
    prg.add(245353849, "DAC BCompZ", 0.2400, enable=False)
    prg.add(245355349, "MT_FastTransfer_to_Dipole10A")
    prg.add(249355349, "IGBT BCompY field CLOSE", enable=False)
    prg.add(249355849, "BCompY current ramp", start_t=0, stop_x=10, n_points=30, start_x=0, stop_t=49, enable=False)
    prg.add(249695849, "MT Current Ramp", start_t=0, stop_x=15, n_points=20, start_x=3.5, stop_t=15, enable=False)
    prg.add(249855349, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(250355349, "Swich Off Dipole")
    prg.add(250358349, "DAC BCompZ", 0.2400, functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(250361349, "Picture Na_Shortrepumper_offset", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False), enable=False)
    prg.add(250361349, "Picture Na_2Gdet_offset", enable=False)
    prg.add(250361349, "Picture Na_1Gdet_offset", enable=False)
    prg.add(250361349, "Picture Na_offset", enable=False)
    prg.add(250361349, "Picture Na_Shortrepumper_offset")
    prg.add(250361349, "Picture Na_3Gdet_offset", enable=False)
    prg.add(250361349, "Picture Na_4Gdet_offset", enable=False)
    prg.add(255361349, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    prg.add(255371349, "IGBT BCompY field OPEN")
    prg.add(255376349, "Set MOT", functions=dict(time=lambda x: x + cmd.get_var('dt'), funct_enable=False))
    return prg
def commands(cmd):
    import numpy as np
    pulse_arr, dummy_arr = np.mgrid[0.0025:0.2:0.0075, 0:3:1, ]
    iters = list(zip(pulse_arr.ravel(), dummy_arr.ravel()))
    j = 0
    while(cmd.running):
        pulse1, dummy1 = iters[j]
        cmd.set_var('pulse', pulse1)
        cmd.set_var('dummy', dummy1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\npulse = %g\ndummy = %g\n'%(j+1, len(iters), pulse1, dummy1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
