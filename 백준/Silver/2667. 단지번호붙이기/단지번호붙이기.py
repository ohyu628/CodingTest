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