prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3250000, "TTL MirrorBottom Probe")
    prg.add(-3012000, "Shutter Probe Vert ON")
    prg.add(-10000, "TTL Picture Hamamatsu  ON", 'PTAI_m1')
    prg.add(-8000, "TTL Picture Hamamatsu OFF")
    prg.add(-4000, "TTL ProbeVert OFF")
    prg.add(-3990, "TTL ProbeHor OFF")
    prg.add(-2060, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(-1560, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(-400, "Oscilloscope Trigger ON", enable=False)
    prg.add(-100, "transfer_m1to0", enable=False)
    prg.add(-100, "transfer_p1to0", enable=False)
    prg.add(-100, "transfer_0to0", enable=False)
    prg.add(-100, "interferometer", enable=False)
    prg.add(-100, "transfer_m1m2")
    prg.add(-100, "transfer_p1p2", enable=False)
    prg.add(0, "TTL ProbeVert ON")
    prg.add(50, "TTL ProbeVert OFF")
    prg.add(500, "TTL ProbeHor ON")
    prg.add(600, "TTL ProbeHor OFF")
    prg.add(700, "AOM Probe Amp ch1 (+)", 0)
    prg.add(1100, "AOM Probe Amp ch2 (-)", 0)
    prg.add(8006, "AOM Probe Amp ch2 (-)", 1000)
    prg.add(8492, "AOM Probe Amp ch1 (+)", 1000)
    prg.add(8500, "TTL Picture Hamamatsu  ON", 'PTAI_p1')
    prg.add(9400, "imaging_repump", enable=False)
    prg.add(10300, "TTL Picture Hamamatsu OFF")
    prg.add(10400, "transfer_p1to0", enable=False)
    prg.add(10400, "transfer_m1to0", enable=False)
    prg.add(10400, "transfer_p1p2")
    prg.add(10400, "transfer_m1m2", enable=False)
    prg.add(10500, "TTL ProbeVert ON")
    prg.add(10550, "TTL ProbeVert OFF")
    prg.add(11500, "AOM Probe Amp ch1 (+)", 0)
    prg.add(12000, "AOM Probe Amp ch2 (-)", 0)
    prg.add(12500, "Oscilloscope Trigger OFF", enable=False)
    return prg
