def dfs(idx):
    for next_idx in adj_list[idx]:
        if visited[next_idx]:
            continue
        visited[next_idx] = 1
        dfs(next_idx)
        


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    adj_list = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    count = 0

    group = list(map(int, input().split()))

    for i in range(M):
        adj_list[group[2*i]].append(group[2*i+1])
        adj_list[group[2*i+1]].append(group[2*i])

    for i in range(1, N+1):
        if visited[i]:
            continue
        count += 1
        visited[1] = 1
        dfs(i)

    print(f'#{tc} {count}')