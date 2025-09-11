import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def alphabet(r, c):
    global count

    count = max(count, len(path))

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in path:
            path.add(arr[nr][nc])
            alphabet(nr, nc)
            path.remove(arr[nr][nc])     
    
# 세로 r, 가로 c 
R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

path = set(arr[0][0])
count = 0

alphabet(0, 0)
print(count)