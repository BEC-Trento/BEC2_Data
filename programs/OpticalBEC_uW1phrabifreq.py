prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(140100000, "Synchronize.sub")
    prg.add(140200000, "+-1_mixture_preparation")
    prg.add(142202000, "TTL uW 2 ON", enable=False)
    prg.add(142207000, "DDS41_setfull", ch0_amp=0, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta')*1e3, ch0_phase=lambda x: cmd.get_var('beat_phase'), ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')), enable=False)
    prg.add(142209000, "TTL uW 1 (100W) ON", enable=False)
    prg.add(142215000, "TTL uW 1 (100W) OFF", enable=False)
    prg.add(142215200, "Oscilloscope Trigger ON", enable=False)
    prg.add(142216400, "soliton_imaging", enable=False)
    prg.add(142216400, "transfer_m1to0", enable=False)
    prg.add(142226400, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(142236400, "transfer_m1to0", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(142246400, "DDSpulse", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(142246400, "interferometer", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(142246400, "TTL uW 2 ON")
    prg.add(142246400, "TTL uW 2 OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')))
    prg.add(142249300, "Oscilloscope Trigger ON", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(142249400, "three_pictures_hamamatsu", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(142249400, "transfer_m1m2", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(142249400, "transfer_p1p2", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(142249500, "transfer_p1to0", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(142249500, "transfer_0to0", enable=False)
    prg.add(142249500, "two_photon_pulse_DDS", functions=dict(time=lambda x: x - cmd.get_var('uW_pulse') + cmd.get_var('hold_time')), enable=False)
    prg.add(142249500, "interferometer", enable=False)
    prg.add(142249510, "Oscilloscope Trigger ON", enable=False)
    prg.add(142279510, "TOF_Levitation", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(142282630, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')), enable=False)
    prg.add(142284730, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')))
    prg.add(142289050, "Oscilloscope Trigger OFF")
    prg.add(142307950, "All uW OFF", enable=False)
    prg.add(146284730, "Cigar_beam_check", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(146294730, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')))
    prg.add(186294730, "wait")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.000000, 0.100000, 10.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uW_pulse = iters[j]
        cmd.set_var('uW_pulse', uW_pulse)
        print('\n')
        print('Run #%d/%d, with variables:\nuW_pulse = %g\n'%(j+1, len(iters), uW_pulse))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
