# 비내림차순 - 숫자가 같을 때를 포함하면서 증가하는 순서로 정렬
def recur(n):
    if n == M:
        print(*path)
        return

    for i in range(1, N+1):
        if path and path[-1] > i:
            continue
        path.append(i)
        recur(n+1)
        path.pop()

N, M = map(int, input().split())

path = []
recur(0)