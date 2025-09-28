from heapq import heappush, heappop
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dists = [[1e9] * N for _ in range(N)]

    dists[0][0] = 0
    pq = [(0, 0, 0)]

    while pq:
        dist, r, c = heappop(pq)

        if dist > dists[r][c]:
            continue

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                cost = 1
                if arr[nr][nc] > arr[r][c]:
                    cost += arr[nr][nc] - arr[r][c]
                new_dist = dist + cost
                if new_dist < dists[nr][nc]:
                    dists[nr][nc] = new_dist
                    heappush(pq, (new_dist, nr, nc))

    print(f'#{tc} {dists[N-1][N-1]}')