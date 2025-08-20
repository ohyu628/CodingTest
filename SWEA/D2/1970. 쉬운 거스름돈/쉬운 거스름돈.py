T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T+1):
    N = int(input())
    result = []

    for i in money:
        if N//i > 0:
            result.append(N//i)
            N -= i * (N//i)
        else:
            result.append(0)
    print(f'#{tc}')
    print(*result)