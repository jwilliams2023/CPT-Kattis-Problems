n, p = map(int, input().split())

watching = map(int, input().split())

current_profit = 0
best = 0
for num_watching in watching:
    current_profit += num_watching - p
    if current_profit < 0:
        current_profit = 0
        continue
    best = max(best, current_profit)

print(best)
