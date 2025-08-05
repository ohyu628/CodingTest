# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )


# 다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )


# 다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    max_sum = 0
    min_sum = sum(a[:M])
    for i in range(N-M+1):
        # 합 최대값 재할당
        if sum(a[i:i+M]) > max_sum:
            max_sum = sum(a[i:i+M])
        # 합 최솟값 재할당
        elif sum(a[i:i+M]) < min_sum:
            min_sum = sum(a[i:i+M])

    print(f'#{tc} {max_sum - min_sum}')