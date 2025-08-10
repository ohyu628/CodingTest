T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_v = 0
    # 좌, 우, 상, 하
    plus_dx = [0, 0, -1, 1]
    plus_dy = [-1, 1, 0, 0]

    # 좌위, 우위, 좌아, 우아
    cross_dx = [-1, -1, 1, 1]
    cross_dy = [-1, 1, -1, 1]

    for i in range(N):
        for j in range(N):
            # + 중심 지점
            kill_plus = arr[i][j]
            for d in range(4):
                for m in range(1, M):
                    ni = i + plus_dx[d] * m
                    nj = j + plus_dy[d] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        kill_plus += arr[ni][nj]

            # x 중간 지점
            kill_cross = arr[i][j]
            for d in range(4):
                for m in range(1, M):
                    ni = i + cross_dx[d] * m
                    nj = j + cross_dy[d] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        kill_cross += arr[ni][nj]

            if max_v < kill_plus:
                max_v = kill_plus
            elif max_v < kill_cross:
                max_v = kill_cross

    print(f'#{t} {max_v}')