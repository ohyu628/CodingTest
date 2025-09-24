from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().strip())) for _ in range(N)]
    dist = [[1e9] * N for _ in range(N)]

    q = deque()

    dist[0][0] = 0
    q.append((0, 0))

    while q:
        r, c = q.popleft()
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                cost = dist[r][c] + arr[nr][nc]

                if cost < dist[nr][nc]:
                    dist[nr][nc] = cost
                    q.append((nr, nc))

    print(f'#{tc} {dist[N-1][N-1]}')