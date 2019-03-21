prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-4354000, "AOM Repumper Amp", 1000)
    prg.add(-4350000, "AOM Repumper freq", 225.00)
    prg.add(-3511500, "AOM Probe Amp ch2 (-)", 1)
    prg.add(-3501500, "AOM Probe Amp ch1 (+)", 1)
    prg.add(-3013000, "Shutter Probe Hor ON")
    prg.add(-3012000, "Shutter Probe Vert ON")
    prg.add(-3010000, "Shutter RepumperMOT ON")
    prg.add(-101199, "DAC BCompY", 0.1000)
    prg.add(-99100, "IGBT BCompY CLOSE")
    prg.add(-5000, "AOM DS + RepumperMOT Amp ", 1000)
    prg.add(-3000, "AOM Probe Detuning", 20.000)
    prg.add(-2300, "TTL Picture Hamamatsu  ON")
    prg.add(-2000, "AOM DS + RepumperMOT Freq", 408.00)
    prg.add(-1700, "TTL Repumper MOT  ON")
    prg.add(-1300, "TTL Repumper MOT OFF", enable=False)
    prg.add(-1250, "AOM DS + RepumperMOT Amp ", 1)
    prg.add(-300, "TTL Picture  ON")
    prg.add(-100, "Oscilloscope Trigger ON", enable=False)
    prg.add(0, "Probe_pulse")
    prg.add(0, "Probe_pulse_1ms", enable=False)
    prg.add(1200, "Oscilloscope Trigger ON", enable=False)
    prg.add(2300, "TTL Picture OFF")
    prg.add(3000, "Oscilloscope Trigger OFF", enable=False)
    prg.add(5200, "TTL Picture Hamamatsu OFF")
    prg.add(11230, "Oscilloscope Trigger OFF", enable=False)
    prg.add(1008100, "TTL Picture  ON")
    prg.add(1008199, "TTL Picture Hamamatsu  ON")
    prg.add(1009600, "AOM Probe Amp ch1 (+)", 1000, enable=False)
    prg.add(1009600, "Probe_pulse")
    prg.add(1009600, "Probe_pulse_1ms", enable=False)
    prg.add(1011800, "TTL Picture OFF")
    prg.add(1018800, "TTL Picture Hamamatsu OFF")
    prg.add(1019800, "TTL Repumper MOT OFF")
    prg.add(2009199, "TTL Picture  ON")
    prg.add(2009300, "TTL Picture Hamamatsu  ON")
    prg.add(2012100, "TTL Picture OFF")
    prg.add(2020100, "TTL Picture Hamamatsu OFF")
    prg.add(3010000, "TTL Picture  ON")
    prg.add(3010100, "TTL Picture Hamamatsu  ON")
    prg.add(3012900, "TTL Picture OFF")
    prg.add(3020899, "TTL Picture Hamamatsu OFF")
    prg.add(3030000, "IGBT BcompY OPEN")
    prg.add(3031000, "DAC BCompY", 0.0000)
    prg.add(4000000, "TTL Picture Hamamatsu  ON", enable=False)
    prg.add(4010000, "TTL Picture Hamamatsu OFF", enable=False)
    return prg
