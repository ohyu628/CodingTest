T = int(input())

for tc in range(1, T+1):
    num = list(map(int, input().split()))

    sum_v = sum(num) - min(num) - max(num)
    
    # 반올림 round 함수 사용
    print(f'#{tc} {round(sum_v / (len(num) - 2))}')
