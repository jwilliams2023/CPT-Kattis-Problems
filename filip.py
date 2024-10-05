"""
#Original way
x,y = input().split()
x = int(x[::-1])
y = int(y[::-1])
z = max(x,y)
print(z)"""


x, y = input().split()

def filip(num1,num2):
    return max(int(num1[::-1]), int(num2[::-1]))

print(filip(x,y))