import sys
input = sys.stdin.read # reading input we forgot

for line in input().splitlines(): #split function for the test cases from input
    n = int(line)
    ones = 1 # ones count
    x = 1  #ones
    while x %n != 0:
        x = (x * 10 + 1) % n # owen trick for TLE, only stores remianders of ones sequences isntead of huge numbers
        ones += 1
    print(ones)