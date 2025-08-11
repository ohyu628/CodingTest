# 우주 괴물
T = int(input())

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                alien_r = i
                alien_c = j
    
    for d in range(4):
        for k in range(1, N):
            nr = alien_r + dr[d] * k
            nc = alien_c + dc[d] * k
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
                arr[nr][nc] = 2
            else:
                break
    
    count = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0:
                count += 1
    print(f'#{tc} {count}')