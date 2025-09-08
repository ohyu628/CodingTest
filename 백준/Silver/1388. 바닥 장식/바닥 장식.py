# DFS 방식
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

# 반복문 방식
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

count = 0

for i in range(N):
    pre_v = ''
    for j in range(M):
        if arr[i][j] == '-' and arr[i][j] != pre_v:
            count += 1
        pre_v = arr[i][j]

for j in range(M):
    pre_v = ''
    for i in range(N):
        if arr[i][j] == '|' and arr[i][j] != pre_v:
            count += 1
        pre_v = arr[i][j]

print(count)
