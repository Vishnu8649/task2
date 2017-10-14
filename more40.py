import sys
def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def check(lines):
    return (line for line in lines if len(line)>=40)

def printlines(lines):
    for line in lines:
        print line,

def main(filenames):
    lines = readfiles(filenames)
    lines = check(lines)
    printlines(lines)
main(sys.argv[1:])

