prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "OpticalBEC_2019-10-15")
    prg.add(110402000, "Synchronize.sub")
    prg.add(110403000, "ARP_linear", enable=False)
    prg.add(110404000, "+-1_mixture_preparation", enable=False)
    prg.add(110405000, "ARP_field")
    prg.add(110835000, "wait", enable=False)
    prg.add(110835500, "DDS41_setfull", ch0_amp=0, ch0_freq=0.000, ch1_freq=0.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0, functions=dict(ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta2')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')))
    prg.add(110836000, "+-1_mixture_preparation_Back", enable=False)
    prg.add(110837000, "ARP_linear", enable=False)
    prg.add(110846000, "wait", enable=False)
    prg.add(110846005, "Oscilloscope Trigger ON", enable=False)
    prg.add(110946005, "transfer_p1p2", enable=False)
    prg.add(110947005, "transfer_p1p2", functions=dict(time=lambda x: x + cmd.get_var('hold_time')), enable=False)
    prg.add(110947010, "TTL uW 1 (100W) ON", enable=False)
    prg.add(110947025, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('uW_pulse')), enable=False)
    prg.add(110952025, "Switch Off Dipole", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(110956800, "Oscilloscope Trigger ON", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(110956810, "transfer_m1to0", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(110956810, "XYplane_pulse", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(110957035, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(110957045, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")+cmd.get_var("uW_pulse")), enable=False)
    prg.add(110957045, "dressing_transfer_m1m2", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(110958545, "dressing_transfer_p1p2", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")), enable=False)
    prg.add(110996554, "TOF_Levitation", functions=dict(time=lambda x: x+ cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(110998539, "imaging_repump", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(110999435, "All uW OFF", functions=dict(time=lambda x: x+ cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(111000413, "three-pictures_VarProbeDet_190625", functions=dict(time=lambda x: x + cmd.get_var('tof') + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")+cmd.get_var("uW_pulse2")))
    prg.add(113000413, "TTL Picture Hamamatsu  ON", 'emptyprobe', functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse2")+cmd.get_var("uW_pulse")), enable=False)
    prg.add(113017073, "Oscilloscope Trigger OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time') +  cmd.get_var('cc_ramplength')+cmd.get_var('uW_pulse')))
    prg.add(113027073, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var('uW_pulse')+cmd.get_var('uW_pulse2')))
    prg.add(116027073, "Initialize_Dipole_Off", functions=dict(time=lambda x: x + cmd.get_var('hold_time')+cmd.get_var("uW_pulse")))
    prg.add(126027073, "DDS39_setfull", ch1_freq=1.000, ch0_amp=1022, ch0_freq=75000000.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=0)
    return prg
def commands(cmd):
    import numpy as np
    iters = np.linspace(0.000000, 0.300000, 13.000000)
    np.random.shuffle(iters)
    j = 0
    while(cmd.running):
        print('\n-------o-------')
        uW_pulse_m1m2 = iters[j]
        cmd.set_var('uW_pulse_m1m2', uW_pulse_m1m2)
        print('\n')
        print('Run #%d/%d, with variables:\nuW_pulse_m1m2 = %g\n'%(j+1, len(iters), uW_pulse_m1m2))
        cmd._system.run_number = j
        cmd.run(wait_end=True, add_time=100)
        j += 1
        if j == len(iters):
            cmd._system.run_number = 0
            cmd.stop()
    return cmd
