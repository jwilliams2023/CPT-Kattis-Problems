n = int(input())
a = []
b = []

for _ in range(n):
    a.append(int((input())))

aSet = set(a)
for i in range(1, 2*n + 1):
    if i not in aSet:
        b.append(i)

a.sort()
b.sort()

maxVal = 0
j = 0
for i in range(n):
    if a[i] > b[j]:
        maxVal += 1
        j += 1

j = 0
minVal = 0
for i in range(n):
    if a[j] < b[i]:
        minVal += 1
        j += 1

print(n-minVal, maxVal)