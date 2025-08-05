# 카운팅 정렬의 숫자 세기 사용
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a =list(map(int, input()))

    lst = [0] * (max(a)+1)
    for i in a:
        lst[i] += 1
    
    max_idx = 0
    for i in range(len(lst)):
        if lst[max_idx] <= lst[i]:
            max_idx = i 

    print(f'#{tc} {max_idx} {lst[max_idx]}')

    