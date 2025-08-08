T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 파리채 한번의 총합
            temp_sum = 0
            for k in range(M):
                for l in range(M): 
                    temp_sum += flies[i+k][j+l]
            # 둘중에 큰 값 비교하여 재할당
            if max_v < temp_sum:
                max_v = temp_sum
    print(f'#{tc} {max_v}')