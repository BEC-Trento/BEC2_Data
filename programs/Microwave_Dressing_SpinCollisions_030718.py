prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(150000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5170000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5170500, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(5171000, "DAC Horiz IR", 5.4000)
    prg.add(5171500, "DAC Vert IR", -0.1000)
    prg.add(5172000, "AOM IR Vertical freq", 120.00)
    prg.add(5172500, "AOM IR Horizontal freq", 80.00)
    prg.add(145172500, "wait")
    prg.add(145175004, "switch off MOT fast")
    prg.add(145177849, "GM BrokenRamp_Short")
    prg.add(145227849, "Config Field MT")
    prg.add(145427849, "Evaporation Ramp.sub")
    prg.add(245427849, "[VOID] End Evaporation")
    prg.add(245429349, "MT_FastTransfer_to_Dipole10A")
    prg.add(249429349, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V")
    prg.add(249429349, "Horizontal Dipole Evaporation Ramp_smallBEC", enable=False)
    prg.add(249429349, "Horizontal Dipole Deep Evaporation", enable=False)
    prg.add(281929349, "[VOID] End Evaporation")
    prg.add(281934349, "MTtoHorDipoleTransfer")
    prg.add(281934349, "MTtoCROSSDipoleTransfer", enable=False)
    prg.add(302034349, "wait", enable=False)
    prg.add(302034849, "Synchronize.sub")
    prg.add(302134849, "DAC Magnetic Trap Voltage", 6.5000, enable=False)
    prg.add(302149849, "Landau_Zener_NoBComp", enable=False)
    prg.add(302149849, "Landau_Zener_pure_020718")
    prg.add(304164849, "wait", enable=False)
    prg.add(304174849, "DAC BComp1", 0.5000)
    prg.add(304224849, "DAC BCompZ", 0.0000)
    prg.add(304324849, "Relay BCompZ Normal")
    prg.add(304374849, "IGBT Bcompz field OPEN")
    prg.add(304524849, "IGBT BCompz field CLOSE")
    prg.add(304525849, "DAC BCompZ", 0.2500)
    prg.add(304625849, "DAC BComp1", 0.3900)
    prg.add(304626349, "uW ON")
    prg.add(304626349, "Decompress_cross", enable=False)
    prg.add(312126349, "wait")
    prg.add(312126849, "uW OFF")
    prg.add(312126863, "Picture_Levit_2018")
    prg.add(312126863, "TESTBCompY_Picture_Levit_2018", enable=False)
    prg.add(312126863, "Picture MT to Levit at 0ms - Levit 50 ms", enable=False)
    prg.add(312128063, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False))
    prg.add(312129763, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(312131075, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(312211075, "Picture Na_uW_Repump", enable=False)
    prg.add(312211075, "Picture Na_2Gdet_offset", enable=False)
    prg.add(312211075, "Picture Na_1Gdet_offset", enable=False)
    prg.add(312214075, "Picture Na_offset", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(312214075, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(312214075, "Picture Na_3Gdet_offset", enable=False)
    prg.add(312214075, "Picture Na_4Gdet_offset", enable=False)
    prg.add(313214075, "Relay BCompZ Normal")
    prg.add(313224075, "IGBT BComp1 field CLOSE")
    prg.add(313234075, "IGBT BComp2 field CLOSE")
    prg.add(328234075, "Initialize_Dipole_Off")
    prg.add(328239075, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.1, 5, 0.1)
    j = 0
    while(cmd.running):
        pulse1 = iters[j]
        cmd.set_var('pulse', pulse1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\npulse = %g\n'%(j+1, len(iters), pulse1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd