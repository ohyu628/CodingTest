dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    global answer

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < 16 and 0 <= nc < 16 and arr[nr][nc] != 1 and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc)
            visited[nr][nc] = 0
            if arr[nr][nc] == 3:
                answer = 1
                return

for tc in range(1, 11):
    input()
    arr = [list(map(int, input())) for _ in range(16)]

    visited = [[0]*16 for _ in range(16)]
    answer = 0

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                visited[i][j] = 1
                dfs(i, j)

    print(f'#{tc} {answer}')