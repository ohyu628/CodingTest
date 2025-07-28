# 무한 반복문 생성
while True:
    A, B = list(map(int, input().split()))
    
    # A, B가 모두 0일 때 종료
    if A == 0 and B ==0:
        break
    else:
        print(A+B)