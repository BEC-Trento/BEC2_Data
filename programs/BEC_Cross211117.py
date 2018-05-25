prg_comment = ""
prg_version = "0.5.1"
def program(prg, cmd):
    prg.add(0, "Initialize 0 TTL and Synchronize.sub")
    prg.add(50000, "switch off MOT ")
    prg.add(60000, "RF Evaporation", 0, enable=False)
    prg.add(5060000, "Set MOT")
    prg.add(5180000, "DAC Magnetic Trap current", 10.0000)
    prg.add(5180500, "DAC Magnetic Trap Voltage", 6.5000)
    prg.add(5181000, "DAC Horiz IR", 5.4000)
    prg.add(5181500, "DAC Vert IR", 0.1000)
    prg.add(5182000, "AOM IR Horizontal freq", 80.00)
    prg.add(5182500, "AOM IR Vertical freq", 80.00)
    prg.add(135082000, "Bright_Compressed_MOT", enable=False)
    prg.add(135090000, "switch off MOT _ Depumper ", enable=False)
    prg.add(135090000, "switch off MOT fast")
    prg.add(135092849, "GM BrokenRamp_Short")
    prg.add(135142849, "Config Field MT")
    prg.add(135142849, "DAC BCompZ", 0.2400, enable=False)
    prg.add(135142849, "BCompZ current ramp", start_t=0, stop_x=1.3, n_points=50, start_x=0.24, stop_t=500, enable=False)
    prg.add(135342849, "Evaporation Ramp.sub")
    prg.add(235342849, "[VOID] End Evaporation")
    prg.add(235343849, "DAC BCompZ", 0.2400, enable=False)
    prg.add(235345349, "MT_FastTransfer_to_Dipole10A")
    prg.add(235345349, "MT_Piecewise_Transfer_to_Dipole10A", enable=False)
    prg.add(239345349, "Horizontal Dipole Evaporation Ramp CMT10A_5.4V")
    prg.add(239345349, "Horizontal Dipole Evaporation Ramp variable", enable=False)
    prg.add(276845349, "[VOID] End Evaporation")
    prg.add(276846000, "IGBT BCompY field CLOSE", enable=False)
    prg.add(276846500, "BCompY current ramp", start_t=0, stop_x=8, n_points=30, start_x=0, stop_t=15, enable=False)
    prg.add(276997000, "Config field OFF", enable=False)
    prg.add(276997000, "Picture MT to Levit at 0ms - Levit 30 ms", enable=False)
    prg.add(276997000, "Picture MT to Levit at 0ms - Levit 20 ms", enable=False)
    prg.add(276997000, "Picture MT to Levit at 0ms - Levit 5 ms", enable=False)
    prg.add(276997000, "Picture MT to Levit at 0ms - Levit 10 ms", enable=False)
    prg.add(276997000, "Picture MT to Levit at 0ms - Levit 50 ms")
    prg.add(276997000, "Picture MT to Levit at 0ms - Levit variableTime", enable=False)
    prg.add(277000000, "DAC BCompZ", 0.2400)
    prg.add(277000500, "Swich Off Dipole")
    prg.add(277003500, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(277003500, "Picture Na_2Gdet_offset", enable=False)
    prg.add(277003500, "Picture Na_1Gdet_offset", enable=False)
    prg.add(277003500, "Picture Na_offset", enable=False)
    prg.add(277003500, "Picture Na_Shortrepumper_offset", enable=False)
    prg.add(277003500, "Picture Na_3Gdet_offset", enable=False)
    prg.add(277003500, "Picture Na_4Gdet_offset", enable=False)
    prg.add(282003500, "Initialize_Dipole_Off")
    prg.add(282008500, "Set MOT")
    return prg