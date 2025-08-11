T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    stone = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        m = i-1
        
        for k in range(1, j+1):
            if m-k < 0 or m+k >= N:
                break
            if stone[m-k] == stone[m+k]:
                stone[m-k] = 1 - stone[m-k]
                stone[m+k] = 1 - stone[m+k]

    print(f'#{tc}', end=' ')
    for num in stone:
        print(num, end=' ')
    print()