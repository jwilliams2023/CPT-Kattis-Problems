import sys
#input = sys.stdin.readline

for inp in sys.stdin:
    inp = int(inp)
    #print(inp)
    if inp == 1:
        print(inp)
    else:
        ones = 2
        x = 11
        
        while x % inp != 0:
            x *= 10
            x +=1 
            ones +=1        
        print(ones)
        
    