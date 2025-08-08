T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]

    # 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    dir = 0
    r = 0
    c = 0

    for num in range(1, N*N+1):
        arr[r][c] = num
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r = nr
            c = nc
        else:
            dir = (dir + 1) % 4
            r = r + dr[dir]
            c = c + dc[dir]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()