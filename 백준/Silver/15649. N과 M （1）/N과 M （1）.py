def recur(n):
    if n == M:
        print(*path)
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        path.append(i)
        recur(n+1)
        visited[i] = 0
        path.pop()

N, M = map(int, input().split())

path = []
visited = [0] * (N+1)

recur(0)