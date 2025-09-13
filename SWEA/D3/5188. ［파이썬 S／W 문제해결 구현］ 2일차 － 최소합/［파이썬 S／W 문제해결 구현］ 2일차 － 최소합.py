# 하, 우
dr = [1, 0]
dc = [0, 1]

def dfs(r, c, total):
    global result
    if r == N-1 and c == N-1:
        result = min(result, total)
        return

    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc, total + arr[nr][nc])
            visited[nr][nc] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    result = 1e9

    visited[0][0] = 1
    dfs(0, 0, arr[0][0])

    print(f'#{tc} {result}')