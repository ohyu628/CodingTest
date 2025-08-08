T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = 1

    for i in range(9):
        # 가로, 세로 값
        row = set()
        column = set()
        for j in range(9):
            row.add(arr[i][j])
            column.add(arr[j][i])
       
            if (i % 3 == 0) and (j % 3 == 0): 
                square = set()
                for r in range(3):
                    for c in range(3):
                        square.add(arr[i+r][j+c])
                if len(square) != 9:
                    flag = 0
                    break
        if flag == 0:
            break
        if len(row) != 9 or len(column) != 9:
            flag = 0
            break
    print(f'#{tc} {flag}')