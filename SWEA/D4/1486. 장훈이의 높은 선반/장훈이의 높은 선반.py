def top(n):
    global result
    if sum(path) >= B:
        if result > sum(path) - B:
            result = sum(path) - B
        return

    for i in range(n, N):
        path.append(arr[i])
        top(i+1)
        path.pop()



T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    path = []
    result = 1e9

    top(0)

    print(f'#{tc} {result}')
