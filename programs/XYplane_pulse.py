prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "DAC SRS", -1.0000, enable=False)
    prg.add(1000, "DAC 100W_amplitude", 1.0000, functions=dict(value=lambda x: cmd.get_var('uW_100WDAC')))
    prg.add(1100, "DDS41_setfull", ch0_amp=1000, ch0_freq=10.000, ch1_freq=20.000, ch0_phase=1.000, ch1_phase=1.000, ch1_amp=1000, functions=dict(ch0_freq=lambda x: 100e6 + cmd.get_var('uW_freq1')*1e3 + cmd.get_var('uW_Delta')*1e3, ch1_freq=lambda x: 100e6 + cmd.get_var('uW_freq2')*1e3 + cmd.get_var('uW_Delta')*1e3, ch0_amp=lambda x: cmd.get_var('uW_amp1'), ch1_amp=lambda x: cmd.get_var('uW_amp2')))
    prg.add(2010, "TTL uW 1 (100W) ON")
    prg.add(2010, "TTL uW 1 (100W) OFF", functions=dict(time=lambda x: x+cmd.get_var('uW_pulse')))
    return prg
