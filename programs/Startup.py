prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "AOM Zeeman Slower Amp", 1000)
    prg.add(50500, "Config field OFF")
    prg.add(52500, "DAC 3DMOT Coils Current", 6.0000)
    prg.add(53000, "DAC Magnetic Trap current", 0.0000)
    prg.add(53500, "Compensate_external_Mag_Field")
    prg.add(62500, "AOM Zeeman Slower freq", 170.00)
    prg.add(72500, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(82500, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(92500, "AOM Probe Detuning", 0.000)
    prg.add(102500, "AOM 2DMOT Amp ch1 (+)", 1000)
    prg.add(112500, "AOM 2DMOT Amp ch2 (-)", 1000)
    prg.add(122500, "AOM 2DMOT Detuning", -15.000)
    prg.add(132500, "AOM 3DMOT Amp ch1 (+)", 1000)
    prg.add(142500, "AOM 3DMOT Amp ch2 (-)", 1000)
    prg.add(152500, "AOM 3DMOT Detuning", -13.000)
    prg.add(162500, "AOM Push Amp ch1 (+)", 1000)
    prg.add(172500, "AOM Push Amp ch2 (-)", 1000)
    prg.add(182500, "AOM Push Detuning", 12.000)
    prg.add(192500, "AOM Repumper Amp", 1000)
    prg.add(202500, "AOM Repumper freq", 225.00)
    prg.add(212500, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(222500, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(232500, "TTL Dark Spot ON")
    prg.add(242500, "TTL Repumper MOT  ON")
    prg.add(252500, "All shutter open")
    prg.add(262500, "Config Field MOT")
    prg.add(272500, "AOM GM Amp ch1 (+)", 1000)
    prg.add(282500, "AOM GM Amp ch2 (-)", 1000)
    prg.add(283000, "AOM GM Detuning", 40.000)
    prg.add(292500, "Initialize_Dipole_Off")
    return prg
def commands(cmd):
    import numpy as np
    iters = np.arange(25, 35, 1)
    j = 0
    while(cmd.running):
        f11 = iters[j]
        cmd.set_var('f1', f11)
        print('\n-------o-------')
        print('Run #%d/%d, with variables:\nf1 = %g\n'%(j+1, len(iters), f11))
        cmd.run(wait_end=True, add_time=10000)
        j += 1
        if j == len(iters):
            cmd.stop()
    return cmd