x1,y1,x2,y2 = map(int, input().split())

res = 2
corners = [(0,0), (0,2024), (2024,0), (2024,2024)]

for corner in corners:
    if (x1,y1) == corners[i]:
        res -= 1

print(res)
