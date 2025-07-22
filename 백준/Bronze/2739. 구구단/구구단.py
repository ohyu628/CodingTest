N = int(input())

if 1 <= N <= 9:
    for i in range(1,10):
        M = N * i
        print(f'{N} * {i} = {M}')