import sys
import random
if len(sys.argv) != 3 or sys.argv[1] != "-f":
    print("Usage: generateFraudTrain.py -f [file]")
    sys.exit()

def fifty_fifty():
    return "FRAUD" if random.choice([0, 1]) else "LOGIN"

seen = set()
with open("train.txt", "w") as g:
    with open(sys.argv[2]) as f:
        for line in f.readlines():
            s = line.split()
            for i in range(2):
                if s[i] not in seen:
                    g.write("%s %s\n" % (fifty_fifty(), s[i]))
                    seen.add(s[i])