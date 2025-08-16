T = int(input())

for tc in range(1, T+1):
    N = int(input())
    trading = list(map(int, input().split()))

    max_price = 0
    result = 0

    # 뒤에서부터 max값 확인 후 갱신
    for i in range(N-1,-1, -1):
        if trading[i] > max_price:
            max_price = trading[i]
        else:
            result += max_price - trading[i]
    print(f'#{tc} {result}')
