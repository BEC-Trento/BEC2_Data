prg_comment = ""
prg_version = "0.7"
def program(prg, cmd):
    prg.add(0, "IGBT 1A CLOSE")
    prg.add(100, "IGBT 1B OPEN")
    prg.add(200, "IGBT 2A OPEN")
    prg.add(300, "IGBT 2B CLOSE")
    prg.add(400, "IGBT 3A CLOSE")
    prg.add(500, "IGBT 3B OPEN")
    prg.add(600, "IGBT 4A OPEN")
    prg.add(700, "IGBT 4B CLOSE")
    return prg
