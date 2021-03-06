prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3250000, "TTL MirrorBottom Probe", enable=False)
    prg.add(-3012000, "Shutter Probe Vert ON")
    prg.add(-10200, "DAC BCompY", 0.2000)
    prg.add(-6050, "IGBT BCompY CLOSE")
    prg.add(-3100, "AOM Probe Detuning", 0.000, functions=dict(frequency=lambda x: cmd.get_var('probe_det')))
    prg.add(-2900, "TTL Picture Hamamatsu  ON", 'atoms', enable=False)
    prg.add(-300, "TTL Picture  ON", 'atoms')
    prg.add(-100, "Oscilloscope Trigger ON", enable=False)
    prg.add(0, "Probe_pulse")
    prg.add(200, "Probe_pulse_Hamam", enable=False)
    prg.add(2300, "TTL Picture OFF")
    prg.add(15000, "Oscilloscope Trigger OFF")
    prg.add(1005000, "TTL Picture Hamamatsu  ON", 'probe', enable=False)
    prg.add(1008100, "TTL Picture  ON", 'probe')
    prg.add(1009600, "Probe_pulse")
    prg.add(1009800, "Probe_pulse_Hamam", enable=False)
    prg.add(1011700, "TTL Picture OFF")
    prg.add(2009099, "TTL Picture  ON", 'back')
    prg.add(2012000, "TTL Picture OFF")
    prg.add(2019900, "TTL Picture Hamamatsu  ON", 'back', enable=False)
    prg.add(2020000, "IGBT BcompY OPEN")
    prg.add(2021900, "TTL Picture Hamamatsu OFF", enable=False)
    prg.add(2030000, "AOM Probe Detuning", 100.000)
    return prg
