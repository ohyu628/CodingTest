# H 1시간 빠지면 M 60분 추가
# 방법 1
H, M = map(int, input().split())
if M < 45:
    if H == 0:
        H = 24
        H -= 1
        M += 60 - 45
        print(H, M)
    else:
        H -= 1
        M += 60 - 45
        print(H, M)
# M > 45 경우 출력값이 있어야 함
else:
    print(H, M-45)

# 방법 2
H, M = map(int, input().split())

if M < 45 :	
    if H == 0 :
        H = 23
        M += 60
    else :
        H -= 1	
        M += 60
        
print(H, M-45)
