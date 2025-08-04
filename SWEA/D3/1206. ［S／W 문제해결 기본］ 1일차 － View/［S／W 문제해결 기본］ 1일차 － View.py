for tc in range(1, 11):
    N = int(input())
    b = list(map(int, input().split()))

    total = 0
    for i in range(2, N-2):
        if (b[i-1] < b[i]) and (b[i] > b[i+1]) and (b[i-2] < b[i]) and (b[i] > b[i+2]):
            total += b[i] - max(b[i-2], b[i-1], b[i+1], b[i+2])
    print(f'#{tc} {total}')   