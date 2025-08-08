T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for r in range(M):
                for c in range(M):
                    total += arr[i+r][j+c]
            if max_v < total:
                max_v = total
    print(f'#{tc} {max_v}')