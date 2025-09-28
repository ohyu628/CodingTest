# Prim
from heapq import heappush, heappop

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start][end] = weight
        graph[end][start] = weight

    pq = [(0, 0)]
    visited = [0] * (V+1)
    min_v = 0

    while pq:
        weight, node = heappop(pq)
        if visited[node]:
            continue

        visited[node] = 1
        min_v += weight

        for next_node in range(V+1):
            if graph[node][next_node] == 0:
                continue

            if visited[next_node]:
                continue

            heappush(pq, (graph[node][next_node], next_node))
    print(f'#{tc} {min_v}')


# Kruskal
def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return
    
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = []
    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph.append((start, end, weight))

    graph.sort(key=lambda x: x[2])

    cnt = 0
    min_v = 0

    parents = [i for i in range(V+1)]

    for s, e, w in graph:
        if find_set(s) != find_set(e):
            union(s, e)
            cnt += 1
            min_v += w
            
            if cnt == V:
                break
    print(f'#{tc} {min_v}')
