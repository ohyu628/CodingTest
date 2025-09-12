# 방법 1
def top(n):
    global result
    if sum(path) >= B:
        result = min(result, sum(path) - B)
        return

    for i in range(n, N):
        path.append(height[i])
        top(i+1)
        path.pop()

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    path = []
    result = 1e9

    top(0)

    print(f'#{tc} {result}')

# 방법 2
def recur(cnt, total_height):
    global result
    if total_height >= B:
        result = min(result, total_height)
        return
    
    if cnt == N:
        return
    
    recur(cnt + 1, total_height + heights[cnt])
    recur(cnt + 1, total_height)

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())

    height = list(map(int, input().split()))
    result = 10000 * N
    
    recur(0, 0)

    print(f'#{tc} {min_answer - B}')
