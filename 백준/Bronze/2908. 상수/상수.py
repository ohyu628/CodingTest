# 방법 1
# 역슬라이싱
A, B = input().split()

A = int(A[::-1])
B = int(B[::-1])

if A > B:
    print(A)
elif A < B:
    print(B)

# 방법 2
# reverse 함수 - 리스트에서만 사용 가능
A, B = map(list, input().split())


A.reverse()
B.reverse()

if ''.join(A) > ''.join(B):
    print(''.join(A))
else:
    print(''.join(B))
