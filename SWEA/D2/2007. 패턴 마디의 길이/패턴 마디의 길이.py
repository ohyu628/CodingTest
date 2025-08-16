T = int(input())

for tc in range(1, T+1):
    S = input()

    for i in range(1, 10):
        if S[:i] == S[i:2*i]:
            print(f'#{tc} {i}')
            break