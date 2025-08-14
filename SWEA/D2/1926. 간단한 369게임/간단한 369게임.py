N = int(input())

for i in range(1, N+1):
    i = str(i)
    # 3,6,9 개수 카운트
    temp_cnt = 0
    for j in range(len(i)):
        if i[j] in ['3', '6', '9']:
            temp_cnt += 1
    if temp_cnt == 0:
        print(i, end=' ')
    else:
        print('-'*temp_cnt, end=' ')