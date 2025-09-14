# 방법 1
def recur(cnt, idx):
    global count
    if cnt == N:
        if sum(path) == K:
            count += 1
        return
    
    for i in range(idx, 13):
        path.append(i)
        recur(cnt + 1, i+1)
        path.pop()

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    path = []
    count = 0

    recur(0, 1)
    print(f'#{tc} {count}')

# 방법 2
def recur(cnt, subset):
    global count
    if cnt == len(arr):
        if sum(subset) == K and len(subset) == N:
            count +=1
        return

    recur(cnt + 1, subset + [arr[cnt]])
    recur(cnt + 1, subset)

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [i for i in range(1, 13)]
    count = 0

    recur(0, [])
    print(f'#{tc} {count}')
