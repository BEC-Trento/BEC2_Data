prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Switch Off MOT_fast")
    prg.add(5060000, "Set_MOT")
    prg.add(5160000, "Synchronize_MOT.sub")
    prg.add(5260000, "Switch Off MOT_fast")
    prg.add(5260020, "Oscilloscope Trigger ON")
    prg.add(5265250, "MOT_pictures_090120", functions=dict(time=lambda x: x + cmd.get_var('tof')))
    prg.add(8765250, "Set_MOT", enable=False)
    prg.add(8765270, "Oscilloscope Trigger OFF")
    prg.add(8765270, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(100.000000, 300.000000, 10.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        push_amplitude = iters[j]
        cmd.set_var('push_amplitude', push_amplitude)
        print('\n')
        print('Run #%d/%d, with variables:\npush_amplitude = %g\n'%(j+1, len(iters), push_amplitude))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
