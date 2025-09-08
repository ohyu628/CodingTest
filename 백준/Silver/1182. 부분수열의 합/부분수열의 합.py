def recur(n):
    global count

    if sum(path) == S and len(path) > 0:
        count += 1

    for i in range(n, N):
        path.append(arr[i])
        recur(i+1)
        path.pop()

N, S = map(int, input().split())

arr = list(map(int, input().split()))

path = []
visited = [0] * (N+1)
count = 0

recur(0)

print(count)