for tc in range(1, 11):
    N = int(input())
    data = list(map(int, input().split()))

    for _ in range(N):
        data[data.index(max(data))] -= 1
        data[data.index(min(data))] += 1
             
    print(f'#{tc} {max(data) - min(data)}')