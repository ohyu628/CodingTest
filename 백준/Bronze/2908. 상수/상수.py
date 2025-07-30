A, B = map(int, input().split())

A = int(str(A)[::-1])
B = int(str(B)[::-1])

if A > B:
    print(A)
elif A < B:
    print(B)