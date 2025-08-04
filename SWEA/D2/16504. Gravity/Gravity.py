T = int(input())

for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))

    max_count = 0
    for i in range(N):
        count = 0
        for j in range(i+1, N):
            if boxes[i] > boxes[j]:
                count += 1
        if count > max_count:
            max_count = count

    print(f'#{tc} {max_count}')