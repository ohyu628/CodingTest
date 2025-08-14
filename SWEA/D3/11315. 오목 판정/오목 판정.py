T = int(input())
# 하, 우, 좌아, 우아
dr = [1, 0, 1, 1]
dc = [0, 1, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _  in range(N)]

    result = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(4):
                    count = 1
                    for k in range(1, 6):
                        nr = i + dr[d] * k
                        nc = j + dc[d] * k
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 'o':
                                count += 1
                            else:
                                if count == 5:
                                    result = 'YES'
                                count = 0
                    if count == 5:
                        result = 'YES'
                        break

    print(f'#{tc} {result}')