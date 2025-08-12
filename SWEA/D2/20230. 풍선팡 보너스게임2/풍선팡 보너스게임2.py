# 방법 1
# 델타 사용
T = int(input())

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    balloon = [list(map(int, input().split())) for _ in range(N)]

    r = 0
    c = 0
    max_v = 0

    for r in range(N):
        for c in range(N):
            count = 0
            for d in range(4):
                for k in range(1, N):
                    nr = r + dr[d] * k
                    nc = c + dc[d] * k
                    if 0 <= nr < N and 0 <= nc < N:
                        count += balloon[nr][nc]
            count += balloon[r][c]

            if max_v < count:
                max_v = count
    print(f'#{tc} {max_v}')

# 방법 2
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    balloon = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    for R in range(N):
        for C in range(N):
            count = -balloon[R][C]

            # 행의 합 구하기
            for c in range(N):
                count += balloon[R][c]
            # 열의 합 구하기
            for r in range(N):
                count += balloon[r][C]
            
            # 최대값 업데이트
            if count > max_v:
                max_v = count
    
    print(f"#{tc} {max_v}")
