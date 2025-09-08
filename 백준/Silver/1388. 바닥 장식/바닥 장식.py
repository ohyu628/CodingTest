def dfs(r, c):
    visited[r][c] = 1
    if arr[r][c] == '-':
        for d in [1]:
            nc = c + d
            if 0 <= nc < M and arr[r][nc] == '-':
                dfs(r, nc)
                
    elif arr[r][c] == '|':
        for d in [1]:
            nr = r + d
            if 0 <= nr < N and arr[nr][c] == '|':
                dfs(nr, c)

# 세로 N, 가로 M = N x M 배열
N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

count = 0
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '-' or arr[i][j] == '|':
            if not visited[i][j]:
                dfs(i, j)
                count += 1
            
print(count)