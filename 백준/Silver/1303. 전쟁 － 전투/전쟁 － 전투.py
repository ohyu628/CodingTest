dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def find_W(r, c):
    global count_W
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 'W' and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            count_W += 1
            find_W(nr, nc)

def find_B(r, c):
    global count_B
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 'B' and visited[nr][nc] == 0:
            count_B += 1
            visited[nr][nc] = 1
            find_B(nr, nc)

N, M = map(int, input().split())
arr = list(input() for _ in range(M))

visited = [[0] * N for _ in range(M)]
result_W = 0
result_B = 0

for i in range(M):
    for j in range(N):
        count_W = 0
        count_B = 0
        if arr[i][j] == 'W' and visited[i][j] == 0:
            visited[i][j] = 1
            count_W += 1
            find_W(i, j)
            result_W += count_W ** 2

        if arr[i][j] == 'B' and visited[i][j] == 0:
            visited[i][j] = 1
            count_B += 1
            find_B(i, j)
            result_B += count_B ** 2

print(result_W, result_B)