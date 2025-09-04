# DFS 풀이
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    global house_count
    global city
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1 and visited[nr][nc] == 0:
            house_count += 1
            visited[nr][nc] = 1
            dfs(nr, nc)
    pass

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
city = 0
house = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            house_count = 1
            city += 1
            visited[i][j] = 1
            dfs(i, j)
            house.append(house_count)

house.sort()
print(city)
for i in range(len(house)):
    print(house[i])