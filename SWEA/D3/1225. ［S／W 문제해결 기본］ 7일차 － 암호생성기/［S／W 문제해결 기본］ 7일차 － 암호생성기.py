from collections import deque

for tc in range(1, 11):
    T = int(input())
    num = deque(map(int, input().split()))

    while num[-1] > 0:
        for i in range(1, 6):
            if num[0] - i > 0:
                num.append(num[0]-i)
                num.popleft()
            elif num[0] - i <= 0:
                num.append(0)
                num.popleft()
                break
    print(f'#{tc}', end=' ')
    print(*num)