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
    prg.add(55175800, "Switch Off MOT")
    prg.add(55178900, "DAC MT-MOT Current", 55.0000)
    prg.add(55179400, "DAC MT-MOT Voltage", 6.0000)
    prg.add(55182500, "GM_051018")
    prg.add(55232500, "wait")
    prg.add(55234500, "Config Field MT-MOT")
    prg.add(55236500, "DAC Horiz IR", 4.0000)
    prg.add(55237500, "AOM IR Horizontal freq", 80.00)
    prg.add(55238500, "AOM IR Horizontal Amp", 1000)
    prg.add(105238500, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=55, stop_t=300)
    prg.add(109238500, "Horizontal Dipole Evaporation Ramp 10_2018", enable=False)
    prg.add(109238500, "Horizontal Dipole Evaporation Ramp_4V_12_2018")
    prg.add(141738500, "[VOID] End Evaporation")
    prg.add(144938500, "IGBT BCompZfine CLOSE")
    prg.add(147938500, "MT_to_Hor_Dipole_Cigar_Transfer_102018", enable=False)
    prg.add(147938500, "Hybrid_to_Cross_Lownumber_Transfer_122018", enable=False)
    prg.add(147938500, "MT_to_Cross_Dipole_Transfer_122018")
    prg.add(158038500, "wait")
    prg.add(158138500, "Config field OFF")
    prg.add(158139500, "Oscilloscope Trigger ON", enable=False)
    prg.add(158140500, "Hysteresis_check_221118", enable=False)
    prg.add(158140500, "Hysteresis_check_021218", enable=False)
    prg.add(160351500, "Oscilloscope Trigger OFF", enable=False)
    prg.add(170351500, "[test] Degauss_1012")
    prg.add(170352500, "Oscilloscope Trigger ON", enable=False)
    prg.add(190352500, "Oscilloscope Trigger OFF", enable=False)
    prg.add(190353500, "Synchronize.sub")
    prg.add(190643500, "wait")
    prg.add(190643600, "DAC uW 2/4 Power", 5.0000)
    prg.add(190643700, "TTL uW 1 FSK LOW")
    prg.add(190643800, "TTL uW 1 (100W) ON")
    prg.add(190643900, "TTL uW 4 ON")
    prg.add(190652900, "TTL uW 1 (100W) OFF")
    prg.add(190653000, "DAC uW 2/4 Power", 0.1500)
    prg.add(190653100, "TTL uW 4 OFF", enable=False)
    prg.add(190653600, "[test] Degauss_Antihelm_1412")
    prg.add(205653600, "wait")
    prg.add(210653600, "DAC uW 2/4 Power", 5.0000)
    prg.add(210653700, "Synchronize.sub")
    prg.add(210953700, "wait", enable=False)
    prg.add(210954700, "TTL uW 1 (100W) ON")
    prg.add(210954800, "TTL uW 4 ON")
    prg.add(210963800, "TTL uW 1 (100W) OFF")
    prg.add(210963900, "TTL uW 1 FSK HIGH")
    prg.add(211013900, "TTL uW 4 OFF")
    prg.add(211014400, "TTL uW 2 ON", enable=False)
    prg.add(226014400, "Synchronize.sub")
    prg.add(226314400, "wait")
    prg.add(226314500, "TTL uW 2 ON")
    prg.add(226314600, "TTL uW 1 (100W) ON")
    prg.add(226321850, "TTL uW 1 (100W) OFF")
    prg.add(226321950, "TTL uW 2 OFF", enable=False)
    prg.add(226421950, "TTL uW 2 ON", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False), enable=False)
    prg.add(226422050, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False))
    prg.add(226436550, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False))
    prg.add(226436650, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False), enable=False)
    prg.add(226536650, "TTL uW 2 ON", functions=dict(time=lambda x: x + 2*cmd.get_var('tpulse'), funct_enable=False), enable=False)
    prg.add(226536750, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x + 2*cmd.get_var('tpulse'), funct_enable=False))
    prg.add(226544000, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + 2*cmd.get_var('tpulse'), funct_enable=False))
    prg.add(226544100, "TTL uW 2 OFF", functions=dict(time=lambda x: x + 2*cmd.get_var('tpulse'), funct_enable=False))
    prg.add(226544200, "wait", enable=False)
    prg.add(226544300, "All_uW_off", functions=dict(time=lambda x: x + 2*cmd.get_var('tpulse'), funct_enable=False))
    prg.add(226544800, "Oscilloscope Trigger ON", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False), enable=False)
    prg.add(226545300, "Picture Levit_SG at 0ms - Levit 10 ms 10_2018", functions=dict(time=lambda x: x + 2*cmd.get_var('tpulse'), funct_enable=False))
    prg.add(226545300, "Picture Levit_SG at 0ms - Levit 20 ms 10_2018", enable=False)
    prg.add(226546900, "Swich Off Dipole", functions=dict(time=lambda x: x + 2*cmd.get_var('tpulse'), funct_enable=False))
    prg.add(226549009, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('tpulse'), funct_enable=False), enable=False)
    prg.add(226550009, "Picture Na_4Gdet", functions=dict(time=lambda x: x + cmd.get_var('TOF'), funct_enable=False), enable=False)
    prg.add(226550009, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(226550009, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(226550009, "Picture Na_uW_Probe_hamamatsu", enable=False)
    prg.add(226550009, "Picture Na_2Gdet", enable=False)
    prg.add(226550009, "Picture Na_1Gdet", enable=False)
    prg.add(226550009, "Picture Na_0Gdet", enable=False)
    prg.add(227050009, "IGBT BCompZfine OPEN", functions=dict(time=lambda x: x + 2*cmd.get_var('tpulse'), funct_enable=False))
    prg.add(232050009, "Set_MOT", functions=dict(time=lambda x: x + 2*cmd.get_var('tpulse'), funct_enable=False))
    prg.add(232050009, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    x_arr, tpulse_arr = np.mgrid[0:1:1, 4.5:4.6:1.5, ]
    iters = list(zip(x_arr.ravel(), tpulse_arr.ravel()))
    j = 0
    while(cmd.running):
        x1, tpulse1 = iters[j]
        cmd.set_var('x', x1)
        cmd.set_var('tpulse', tpulse1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nx = %g\ntpulse = %g\n'%(j+1, len(iters), x1, tpulse1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd