# DFS 형식
N = int(input())

def check(date, total):
    global result
    if date > N+1:
        return

    if date == N + 1:
        result = max(result, total)
        return

    day, price = work[date]
    if date + day <= N + 1:
        check(date + day, total + price)
    check(date + 1, total)
    
work = [(0, 0)]
result = 0

for i in range(N):
    day, price = map(int, input().split())
    work.append((day, price))

check(1, 0 )

print(result)