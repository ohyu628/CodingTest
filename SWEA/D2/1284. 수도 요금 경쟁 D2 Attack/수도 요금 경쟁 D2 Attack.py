T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
	
    # A사 요금
    A = W * P
    # B사 요금
    if W > R:
        B = Q + (W-R) * S
    else:
        B = Q
    
    # A사와 B사 중 적은 요금 출력
    if A > B:
        print(f'#{tc} {B}')
    elif A < B:
        print(f'#{tc} {A}')
