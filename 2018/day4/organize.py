import sys
from datetime import datetime

def parse(line):
    parts = line.split("] ")
    date = datetime.strptime(parts[0].split("[")[1], "%Y-%m-%d %H:%M")
    epoch = datetime.utcfromtimestamp(0)
    return (date - epoch).total_seconds()

cmds = [line.strip() for line in sys.stdin]
for cmd in sorted(cmds, key = lambda x: parse(x)):
    print(cmd)
    


