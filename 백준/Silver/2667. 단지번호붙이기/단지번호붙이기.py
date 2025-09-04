# BFS 풀이
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
q = deque()
visited = [[0]*N for _ in range(N)]
count = 0
house = []

for r in range(N):
    for c in range(N):
        if arr[r][c] == 1 and visited[r][c] == 0:
            visited[r][c] = 1
            q.append((r, c))
            count += 1
            house_count = 0

            while q:
                house_count += 1
                i, j = q.popleft()
                for d in range(4):
                    ni = i + dr[d]
                    nj = j + dc[d]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                        q.append((ni, nj))
                        visited[ni][nj] = 1
            house.append(house_count)
                      
house.sort()
     
print(count)
for i in range(len(house)):
    print(house[i])


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
