T = int(input())

for tc in range(1, T+1):
    num = list(map(int, input().split()))

    sum_v = sum(num) - min(num) - max(num)

    print(f'#{tc} {round(sum_v / (len(num) - 2))}')