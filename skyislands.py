n, m = map(int, input().split())

parents = [i for i in range(n + 1)]  # Move this line after n is defined

def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]

def union(node1, node2):
    parent1 = find(node1)
    parent2 = find(node2)
    parents[parent1] = find(parent2)

for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)

groups = set()
for p in parents[1:]:
    groups.add(find(p))

if len(groups) == 1:
    print("YES")
else:
    print("NO")
