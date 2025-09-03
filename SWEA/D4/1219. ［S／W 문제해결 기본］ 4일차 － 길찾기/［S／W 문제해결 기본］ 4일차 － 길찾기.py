def dfs(node):
    global answer

    if node == 99:
        answer = 1
        return
    
    for next_node in adj_list[node]:
        if visited[next_node]:
            continue
        visited[next_node] = 1
        dfs(next_node)


for _ in range(10):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)]
    visited = [0] * 100
    answer = 0

    for i in range(N):
        a = arr[2*i]
        b = arr[2*i+1]
        adj_list[a].append(b)
    
    visited[0] = 1
    dfs(0)

    print(f'#{tc} {answer}')