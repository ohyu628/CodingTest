# 방법 1
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    count = 0
    for i in range(N):
        if Ai[i] != Bi[i]:
            for j in range(i, N):
                if Bi[j] == 0:
                    Bi[j] = 1
                elif Bi[j] == 1:
                    Bi[j] = 0
            count += 1
    print(f'#{tc} {count}')

# 방법 2
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    count = 0
    for i in range(N):
        if Ai[i] != Bi[i]:
            for j in range(i, N):
                Bi[j] = 1 - Bi[j]
            count += 1
    print(f'#{tc} {count}')
