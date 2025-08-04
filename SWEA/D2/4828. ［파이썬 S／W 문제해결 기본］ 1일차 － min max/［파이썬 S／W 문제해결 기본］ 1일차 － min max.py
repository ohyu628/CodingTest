# 방법 1
# min, max 함수 사용
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    a = list(map(int, input().split()))

    print(f'#{tc} {max(a)-min(a)}')

# 방법 2
# 함수 사용하지 않고 반복문만 사용
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
