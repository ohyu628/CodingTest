T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0
    for i in range(N):
        count = 0
        for j in range(M):
            if arr[i][j] == 1:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 0
            if max_count < count:
                max_count = count
    
    for j in range(M):
        count = 0
        for i in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 0
            if max_count < count:
                max_count = count
    if max_count > 1:
        print(f'#{tc} {max_count}')
    else:
        print(f'#{tc} 0')