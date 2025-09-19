# 재귀 1000 호출 제한 1000000으로 늘려줌
import sys
sys.setrecursionlimit(10**6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
 
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and farm[nr][nc] == 1 and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc)
            
T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())

    farm = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        a, b = map(int, input().split())
        farm[b][a] = 1
    
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and visited[i][j] == 0:
                count += 1
                visited[i][j] = 1
                dfs(i, j)
    print(count)