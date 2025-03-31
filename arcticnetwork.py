from collections import defaultdict
from heapq import heappush, heappop
from math import dist

N = int(input())

for _ in range(N):
    S, P = map(int, input().split())

    mst = []
    coords = []
    min_heap = [(0,0)]
    total_cost = 0

    for  _ in range(P):
        x,y = map(int, input().split())
        coords.append((x,y))

    adj = {}
    for i in range(P):
        for j in range(P):
            if i != j:
                adj[i].append((j, dist(coords[i],coords[j])))
    
    visited = set()

    while min_heap:
        dest, distance = heappop(min_heap)
        if dest in visited:
            continue
        visited.add(dest)
        mst.append(distance, dest)

        total_cost += distance
        for c_dest, c_distance in adj[dest]:
            if c_dest not in visited:
                heappush(min_heap, (c_dest, (c_dest, c_distance)))

    #print(mst)
    mst.sort()
    for _ in range(S):
        mst.pop()

    print(mst[-1][0])