T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0

    if N < M:
        short, long = A, B
    else:
        short, long = B, A

    for i in range(len(long) - len(short) + 1):
        total = 0
        for j in range(len(short)):
            total += short[j] * long[i+j]

        result = max(result, total)

    print(f'#{tc} {result}')