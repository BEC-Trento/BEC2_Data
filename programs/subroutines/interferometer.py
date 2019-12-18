prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(-3000, "DDS41_setfull", ch1_freq=100808785.000, ch0_amp=100, ch0_freq=100443733.000, ch0_phase=0.000, ch1_phase=0.000, ch1_amp=150, functions=dict(ch1_freq=lambda x: cmd.get_var('beat_freq1'), ch0_amp=lambda x: cmd.get_var('beat_amp0'), ch0_freq=lambda x: cmd.get_var('beat_freq0'), time=lambda x: x - cmd.get_var('beating_pulse'), ch0_phase=lambda x: 1, ch1_phase=lambda x: cmd.get_var('beat_phase'), ch1_amp=lambda x: cmd.get_var('beat_amp1')))
    prg.add(0, "TTL uW 1 (100W) OFF")
    prg.add(0, "TTL uW 1 (100W) ON", functions=dict(time=lambda x: x - cmd.get_var('beating_pulse')))
    return prg