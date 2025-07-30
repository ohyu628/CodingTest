T = int(input())

for _ in range(T):
    R , S = input().split()
    
    P = ''
    for i in range(len(S)):
        P += S[i] * int(R)
    print(P)