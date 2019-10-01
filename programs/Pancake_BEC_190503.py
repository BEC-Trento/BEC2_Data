prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(15800, "Initialize_Dipole_Lowpower", enable=False)
    prg.add(65800, "Switch Off MOT")
    prg.add(5075800, "Set_BrightMOT", enable=False)
    prg.add(5075800, "Set_MOT")
    prg.add(135075800, "Switch Off MOT", enable=False)
    prg.add(135075800, "Switch Off MOT_fast")
    prg.add(135077050, "GM_051018")
    prg.add(135078950, "DAC MT-MOT Current", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_I')))
    prg.add(135079450, "DAC MT-MOT Voltage", 0.0000, functions=dict(value=lambda x: cmd.get_var('MT_Voltage')))
    prg.add(135132550, "wait")
    prg.add(135133550, "Config Field MT-MOT")
    prg.add(135134550, "DAC Horiz IR", 0.0000, functions=dict(value=lambda x: cmd.get_var('CigarV')))
    prg.add(135135050, "AOM IR Horizontal Amp", 1000)
    prg.add(135135550, "AOM IR Horizontal freq", 80.00)
    prg.add(135136050, "Oscilloscope Trigger ON", enable=False)
    prg.add(135636050, "DAC MT-MOT Voltage", 8.5000)
    prg.add(135637050, "Evaporation Ramp.sub", enable=False)
    prg.add(137137050, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=24, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I'), stop_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(175637050, "MT Current Ramp", start_t=0, stop_x=18, n_points=100, start_x=0, stop_t=500, functions=dict(start_x=lambda x: cmd.get_var('MT_I_final')))
    prg.add(180738050, "Horizontal Dipole Evaporation RampPancake_5V_2019_05")
    prg.add(200739050, "wait")
    prg.add(200749050, "DAC IR Horiz_Ellipt", 0.0000)
    prg.add(200749550, "DAC Vert IR", 0.0000)
    prg.add(200759550, "AOM IR Horiz_Ellipt Amp", 1000)
    prg.add(200760050, "AOM IR Horiz_Ellipt freq", 110.00)
    prg.add(200760550, "AOM IR Vertical Amp", 1000)
    prg.add(200761050, "AOM IR Vertical freq", 80.00)
    prg.add(200762050, "DAC IR Horizontal Ellipt ramp", start_t=0, stop_x=6, n_points=100, start_x=0, stop_t=100)
    prg.add(200763050, "DAC IR Vertical ramp", start_t=0, stop_x=3.5, n_points=100, start_x=0, stop_t=100)
    prg.add(201764050, "wait")
    prg.add(201765050, "DAC IR Horizontal ramp", start_t=0, stop_x=-0.1, n_points=100, start_x=0.4, stop_t=500)
    prg.add(206775050, "AOM IR Horizontal freq", 110.00)
    prg.add(206776050, "AOM IR Horizontal Amp", 0)
    prg.add(206788550, "MT Current Ramp", start_t=0, stop_x=0, n_points=100, start_x=18, stop_t=500, enable=False)
    prg.add(206789550, "Config field OFF", enable=False)
    prg.add(206790550, "DAC IR Horiz_Ellipt Exp ramp", start_t=0.0000, func_args="start_value=6, tau=0.4, offset=0.5", n_points=100, func="(start_value-offset)*exp(-t/tau)+offset", stop_t=2000.0000)
    prg.add(206791550, "DAC Vert IR Exp ramp", start_t=0.0000, func_args="start_value=3.5, tau=0.4, offset=0.175", n_points=100, func="(start_value-offset)*exp(-t/tau)+offset", stop_t=2000.0000)
    prg.add(206803500, "Oscilloscope Trigger ON")
    prg.add(226803500, "wait")
    prg.add(226805500, "Switch Off Dipole")
    prg.add(226805550, "Config field MT-MOT to Levit", enable=False)
    prg.add(226805550, "Config field Levit", enable=False)
    prg.add(226806550, "DAC MT-MOT Current", 40.0000, enable=False)
    prg.add(226806550, "Config field OFF")
    prg.add(226806590, "Oscilloscope Trigger OFF")
    prg.add(226808340, "Picture_Mirror_Na_VarProbeDet", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(226808340, "Picture_Mirror_Levit_VarProbeDet", functions=dict(time=lambda x: x+cmd.get_var('tof')), enable=False)
    prg.add(241808340, "Set_MOT", functions=dict(time=lambda x: x +cmd.get_var('tof')))
    prg.add(241809340, "AOM IR Horizontal Amp", 1000)
    prg.add(241809340, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(1, 21, 4)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        tof1 = iters[j]
        cmd.set_var('tof', tof1)
        print('\n')
        print('Run #%d/%d, with variables:\ntof = %g\n'%(j+1, len(iters), tof1))
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd