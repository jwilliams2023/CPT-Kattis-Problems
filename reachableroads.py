num_cities = int(input())

for _ in range(num_cities):
    road_ends = int(input())
    num_roads = int(input())

    graph = {}
    for i in range(road_ends):
        graph[i] = []
    
    for _ in range(num_roads):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
    
    num_connect_groups = 0
    for node in graph:
        if node not in visited:
            dfs(node)
            num_connect_groups += 1
    num_connect_groups -= 1

    print(num_connect_groups)
    



