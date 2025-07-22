H, M = map(int, input().split())

# 시간 1시간 빠지면 분 60분 추가
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
else:
    print(H, M-45)