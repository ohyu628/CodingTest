T = int(input())

for tc in range(1, T+1):
    S = input()
    result = 0
    for i in range(len(S)//2):
        if S[i] == S[-(i+1)]:
            result = 1
    print(f'#{tc} {result}')