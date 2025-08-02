T = int(input())

for tc in range(1, T+1):
    N = list(map(int, input().split()))

    result = 0
    for i in N:
        if i % 2 != 0:
            result += i
    print(f'#{tc} {result}')