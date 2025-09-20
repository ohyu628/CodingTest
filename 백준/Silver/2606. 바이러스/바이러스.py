# bfs
from collections import deque

computer = int(input())
connect = int(input())

adj_list = [[] for _ in range(computer + 1)]
visited = [0] * (computer + 1)
count = 0
q = deque()

for _ in range(connect):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visited[1] = 1
q.append(1)

while q:
    idx = q.popleft()

    for i in adj_list[idx]:
        if visited[i]:
            continue
        visited[i] = 1
        count += 1
        q.append(i)

print(count)


# dfs
def dfs(idx):
    global count
    for i in adj_list[idx]:
        if visited[i]:
            continue
        visited[i] = 1
        dfs(i)
        count += 1

computer = int(input())
connect = int(input())

adj_list = [[] for _ in range(computer + 1)]
visited = [0] * (computer + 1)
count = 0

for _ in range(connect):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visited[1] = 1
dfs(1)


print(count)

