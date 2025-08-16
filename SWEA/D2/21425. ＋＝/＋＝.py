T = int(input())

for _ in range(T):
    A, B, N = map(int, input().split())
    
    cnt = 0
    
    while N >= A and N >= B:
        if A < B:
            A += B
            cnt += 1
        else:
            B += A
            cnt += 1
            
    print(cnt)