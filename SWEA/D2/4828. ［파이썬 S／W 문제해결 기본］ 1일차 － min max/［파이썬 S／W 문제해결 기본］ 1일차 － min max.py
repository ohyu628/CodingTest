T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    max_value = 0
    min_value = a[0]
    for i in range(len(a)):
        if a[i] > max_value:
            max_value = a[i]
        elif a[i] < min_value:
            min_value = a[i]

    print(f'#{tc} {max_value - min_value}')