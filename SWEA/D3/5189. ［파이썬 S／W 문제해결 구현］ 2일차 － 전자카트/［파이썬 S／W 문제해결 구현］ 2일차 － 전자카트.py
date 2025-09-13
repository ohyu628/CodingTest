# 방법 1 - 최적화 코드
def recur(r, total, cnt):
    global result
    if cnt == N:
        result = min(result, total + arr[r][0])
        return

    # 가지치기
    if total >= result:
        return
    
    for c in range(N):
        if visited[c]:
            continue
        visited[c] = 1
        recur(c, total + arr[r][c], cnt + 1)
        visited[c] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    visited[0] = 1
    result = 1e9

    # 현재 위치, 누적 배터리, 방문 구역 수
    recur(0, 0, 1)
        
    print(f'#{tc} {result}')
    
# 방법 2
def recur(r, c, total):
    global result
    if all(visited):
        total += arr[c][0]
        result = min(result, total)
        return
    
    for j in range(N):
        if visited[j]:
            continue
        if c == j:
            continue
        visited[j] = 1
        recur(c, j, total + arr[c][j])
        visited[j] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    visited[0] = 1
    result = 1e9

    for i in range(1, N):
        visited[i] = 1
        recur(0, i, arr[0][i])
        visited[i] = 0
        
    print(f'#{tc} {result}')
