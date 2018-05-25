prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(150000, "switch off MOT ")
    prg.add(5050000, "Set MOT")
    prg.add(5170000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5170500, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(5171000, "DAC Horiz IR", 5.4000)
    prg.add(5171500, "AOM IR Horizontal freq", 80.00)
    prg.add(45171500, "wait")
    prg.add(45174004, "switch off MOT fast")
    prg.add(45176849, "GM BrokenRamp_Short")
    prg.add(45226849, "Config Field MT")
    prg.add(45426849, "Evaporation Ramp.sub")
    prg.add(145426849, "[VOID] End Evaporation")
    prg.add(145428349, "MT_FastTransfer_to_Dipole10A")
    prg.add(149428349, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V")
    prg.add(181928349, "[VOID] End Evaporation")
    prg.add(181928353, "MTtoHorDipoleTransfer")
    prg.add(191928463, "wait")
    prg.add(191938463, "DAC Magnetic Trap current", 1.0000)
    prg.add(191938463, "Config field OFF", enable=False)
    prg.add(191948463, "Compensate_external_Mag_Field", enable=False)
    prg.add(191948463, "Landau_Zener")
    prg.add(193858463, "wait")
    prg.add(193858563, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(193858574, "Picture_Levit_2018")
    prg.add(193859774, "Swich Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False))
    prg.add(193861474, "Config field OFF", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(193862786, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(193862786, "Picture Na_2Gdet_offset", enable=False)
    prg.add(193862786, "Picture Na_1Gdet_offset", enable=False)
    prg.add(193862786, "Picture Na_offset", functions=dict(time=lambda x: x + cmd.get_var('t1'), funct_enable=False), enable=False)
    prg.add(193862786, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(193862786, "Picture Na_3Gdet_offset", enable=False)
    prg.add(193862786, "Picture Na_4Gdet_offset", enable=False)
    prg.add(200090097, "Relay BCompZ Normal")
    prg.add(208862786, "Initialize_Dipole_Off")
    prg.add(208867786, "Set MOT")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(0.25, 0.28, 0.003)
    j = 0
    while(cmd.running):
        bfin1 = iters[j]
        cmd.set_var('bfin', bfin1)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nbfin = %g\n'%(j+1, len(iters), bfin1))
        cmd.run(wait_end=True, add_time=1000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd