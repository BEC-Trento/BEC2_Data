prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3250000, "TTL MirrorBottom Probe")
    prg.add(-3012000, "Shutter Probe Vert ON")
    prg.add(-5000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(-3000, "AOM Probe Detuning", 0.000, functions=dict(frequency=lambda x: cmd.get_var('probe_det')))
    prg.add(-2300, "TTL Picture Hamamatsu  ON")
    prg.add(-2200, "TTL Repumper MOT  ON")
    prg.add(-2000, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(-1400, "TTL Repumper MOT  ON", enable=False)
    prg.add(-1300, "TTL Repumper MOT OFF")
    prg.add(-1250, "AOM DS + RepumperMOT Amp ", 1)
    prg.add(-400, "two_photon_pulse", enable=False)
    prg.add(-300, "TTL Picture  ON")
    prg.add(0, "Probe_pulse")
    prg.add(2300, "TTL Picture OFF")
    prg.add(5200, "TTL Picture Hamamatsu OFF")
    prg.add(1008100, "TTL Picture  ON")
    prg.add(1008199, "TTL Picture Hamamatsu  ON")
    prg.add(1009600, "AOM Probe Amp ch1 (+)", 1000, enable=False)
    prg.add(1009600, "Probe_pulse")
    prg.add(1011800, "TTL Picture OFF")
    prg.add(1018800, "TTL Picture Hamamatsu OFF")
    prg.add(1019800, "TTL Repumper MOT OFF")
    prg.add(2009199, "TTL Picture  ON")
    prg.add(2009300, "TTL Picture Hamamatsu  ON")
    prg.add(2012100, "TTL Picture OFF")
    prg.add(2020100, "TTL Picture Hamamatsu OFF")
    prg.add(3010000, "TTL Picture  ON", enable=False)
    prg.add(3010100, "TTL Picture Hamamatsu  ON", enable=False)
    prg.add(3012900, "TTL Picture OFF", enable=False)
    prg.add(3020899, "TTL Picture Hamamatsu OFF", enable=False)
    return prg
