prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT BCompZfine OPEN")
    prg.add(50000, "Config field OFF")
    prg.add(100000, "Initialize 0 TTL and Synchronize.sub")
    prg.add(115800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(165800, "Switch Off MOT")
    prg.add(5175800, "Set_BrightMOT", enable=False)
    prg.add(5175800, "Set_MOT")
    prg.add(135175800, "Switch Off MOT")
    prg.add(135178900, "DAC MT-MOT Current", 55.0000)
    prg.add(135179400, "DAC MT-MOT Voltage", 4.0000)
    prg.add(135182500, "GM_051018")
    prg.add(135232500, "wait")
    prg.add(135233500, "Config Field MT-MOT")
    prg.add(135235500, "DAC Horiz IR", 5.4000)
    prg.add(135236500, "AOM IR Horizontal freq", 80.00)
    prg.add(135237500, "AOM IR Horizontal Amp", 1000)
    prg.add(235237500, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=55, stop_t=300)
    prg.add(239237500, "Horizontal Dipole Evaporation Ramp 10_2018")
    prg.add(271737500, "[VOID] End Evaporation")
    prg.add(271837500, "Relay BCompZ Invert")
    prg.add(272037500, "IGBT BCompz CLOSE")
    prg.add(272047500, "DAC BCompZ", 1.0000)
    prg.add(272547500, "MT_to_Hor_Dipole_Cigar_Transfer_102018")
    prg.add(292647500, "IGBT BCompZfine CLOSE")
    prg.add(292648000, "BCompZ current ramp", start_t=0, stop_x=0, n_points=100, start_x=1, stop_t=10)
    prg.add(294648000, "IGBT Bcompz OPEN")
    prg.add(295648000, "Synchronize.sub")
    prg.add(295948000, "uW ON")
    prg.add(295948000, "uW OFF", functions=dict(time=lambda x: x +cmd.get_var('tpulse')))
    prg.add(295948500, "IGBT BCompz CLOSE", functions=dict(time=lambda x: x +cmd.get_var('tpulse')))
    prg.add(297948500, "BCompZ current ramp", start_t=0, stop_x=1, n_points=100, start_x=0, stop_t=10, functions=dict(time=lambda x: x +cmd.get_var('tpulse')))
    prg.add(298148500, "IGBT BCompZfine OPEN", functions=dict(time=lambda x: x +cmd.get_var('tpulse')))
    prg.add(298248500, "Oscilloscope Trigger ON", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(298249000, "Picture Levit_SG at 0ms - Levit 20 ms 10_2018", enable=False)
    prg.add(298249000, "Picture Levit_SG at 0ms - Levit 10 ms 10_2018", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(298250600, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(298251109, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('tpulse')))
    prg.add(298451109, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(298451109, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(298451109, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(298451109, "Picture Na_uW_Probe_hamamatsu", enable=False)
    prg.add(298451109, "Picture Na_2Gdet", enable=False)
    prg.add(298451109, "Picture Na_1Gdet", enable=False)
    prg.add(298451109, "Picture Na_0Gdet", enable=False)
    prg.add(298951109, "IGBT BCompZfine OPEN")
    prg.add(303951109, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tpulse')))
    prg.add(303951109, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.03, 0.72, 0.03)
    j = 0
    while(cmd.running):
        tpulse1 = iters[j]
        cmd.set_var('tpulse', tpulse1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\ntpulse = %g\n'%(j+1, len(iters), tpulse1))
        cmd.run(wait_end=True, add_time=1500)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd