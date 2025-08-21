arr = [list(map(int, input().split())) for _ in range(9)]

max_v = 0
r, c = 0, 0

for i in range(9):
    for j in range(9):
        if max_v < arr[i][j]:
            max_v = arr[i][j]
            r, c = i, j
print(max_v)
print(r+1, c+1)