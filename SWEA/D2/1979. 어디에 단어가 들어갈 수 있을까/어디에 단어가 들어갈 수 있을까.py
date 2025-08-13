T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for i in range(N):
        # 가로
        row_count = 0
        for j in range(N):
            if arr[i][j] == 1:
                row_count +=1
            elif arr[i][j] == 0:
                if row_count == K:
                    total += 1
                row_count = 0
        if row_count == K:
            total += 1
    for j in range(N):
        # 세로
        col_count = 0
        for i in range(N):
            if arr[i][j] == 1:
                col_count +=1
            elif arr[i][j] == 0:
                if col_count == K:
                    total += 1
                col_count = 0
        if col_count == K:
            total += 1
    print(f'#{tc} {total}')