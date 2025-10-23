T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()

    result = "Possible"
    count = 0

    for i in range(max(arrive)+1):
        if i != 0 and i % M == 0:
            count += K
        
        for j in arrive:
            if i == j:
                if count == 0:
                    result = "Impossible"
                    break
                else:
                    count -= 1

    print(f'#{tc} {result}')