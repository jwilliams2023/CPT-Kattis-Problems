n, k = map(int, input().split())

operations = input().split()

for i, v in enumerate(operations):
    undo_count = 0
    if v == 0:
        continue

    if v == 'undo' :
        undo_count = int(operations[i+1])

        for j in range(undo_count, i-undo_count, -1):
            operations[j] = 0
        operations[i] = 0
        operations[i-1] = 0

    moves = sum([int(x) for x in operations[:i+1] if x != 0])

    rem = moves % n

print(rem)