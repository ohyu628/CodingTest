T = int(input())

for tc in range(1, T+1):
    N = list(map(int, input().split()))

    H = N[0] + N[2]
    M = N[1] + N[3]

    if M >= 60:
        H += 1
        M -= 60
    if H >= 12:
        H -= 12
    print(f'#{tc} {H} {M}')