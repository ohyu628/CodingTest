# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    flied = [list(map(str, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if flied[i][j] == 'X':
                start_r, start_c = i, j
    result = []

    Q = int(input())
    for _ in range(Q):
        C, command = map(str, input().split())

        dir = 0
        r, c = start_r, start_c

        for k in range(int(C)):
            if command[k] == 'R':
                dir += 1

            elif command[k] == 'L':
                dir -= 1

            elif command[k] == 'A':
                dir = dir % 4

                nr = r + dr[dir]
                nc = c + dc[dir]
                if 0 <= nr < N and 0 <= nc < N and flied[nr][nc] != 'T':
                    r, c = nr, nc

        if flied[r][c] == 'Y':
            result.append(1)

        else:
            result.append(0)


    print(f'#{tc} ', end='')
    print(*result)