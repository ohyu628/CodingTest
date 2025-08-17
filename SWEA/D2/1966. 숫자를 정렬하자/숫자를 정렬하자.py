# 버블 정렬 사용
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))


    for i in range(N-1, 0, -1):
        for j in range(i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    print(f'#{tc}', *num)