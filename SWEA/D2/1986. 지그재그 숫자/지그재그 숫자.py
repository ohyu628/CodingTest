T = int(input())

for tc in range(1, T+1):
    N = int(input())

    result = 0
    for i in range(1, N+1):
        # 홀수면 +, 짝수면 -
        if i % 2 == 0:
            result -= i
        else:
            result += i
    print(f'#{tc} {result}')