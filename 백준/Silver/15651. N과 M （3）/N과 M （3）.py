def recur(n):
    if n == M:
        print(*path)
        return
    
    for i in range(1, N+1):
        path.append(i)
        recur(n+1)
        path.pop()

N, M = map(int, input().split())

path = []
recur(0)