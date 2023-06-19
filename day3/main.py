import things.fileinputoutput as fileio
def parseSacks(sacksStr: str) -> list[str]:
    return sacksStr.split()

sacks = parseSacks(fileio.readFile('./input.txt'))
