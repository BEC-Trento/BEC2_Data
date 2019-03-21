prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "Switch Off MOT")
    prg.add(5060000, "Set_BrightMOT", enable=False)
    prg.add(5060000, "Set_MOT")
    prg.add(135060000, "Switch Off MOT")
    prg.add(135062340, "Picture Na_4Gdet", enable=False)
    prg.add(135062340, "Picture Na_4Gdet_hamamatsu", enable=False)
    prg.add(135063340, "Picture_Na_VarProbeDet")
    prg.add(135063340, "Picture_Mirror_Na_VarProbeDet", enable=False)
    prg.add(135063340, "Picture Na_3Gdet_hamamatsu", enable=False)
    prg.add(135063340, "Picture Na_resonant_hamamatsu", enable=False)
    prg.add(140063340, "Set_MOT")
    prg.add(140063340, "Set_BrightMOT", enable=False)
    return prg
def commands(cmd):
    import numpy as np
    det_arr, mot_I_arr, amp_arr = np.mgrid[-21:-17:0.5, 30:40:2, 300:800:100, ]
    iters = list(zip(det_arr.ravel(), mot_I_arr.ravel(), amp_arr.ravel()))
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        det1, mot_I1, amp1 = iters[j]
        cmd.set_var('det', det1)
        cmd.set_var('mot_I', mot_I1)
        cmd.set_var('amp', amp1)
        print('\n')
        print('Run #%d/%d, with variables:\ndet = %g\nmot_I = %g\namp = %g\n'%(j+1, len(iters), det1, mot_I1, amp1))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd
