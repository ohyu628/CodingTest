def recur(r, c, total):
    global result
    if all(visited):
        total += arr[c][0]
        result = min(result, total)
        return
    
    for j in range(N):
        if visited[j]:
            continue
        if c == j:
            continue
        visited[j] = 1
        recur(c, j, total + arr[c][j])
        visited[j] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    visited[0] = 1
    result = 1e9

    for i in range(1, N):
        visited[i] = 1
        recur(0, i, arr[0][i])
        visited[i] = 0
        
    print(f'#{tc} {result}')