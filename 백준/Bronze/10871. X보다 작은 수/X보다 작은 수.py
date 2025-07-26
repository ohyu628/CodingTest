# 방법 1
# int로 출력
N, X = map(int, input().split())
A = list(map(int, input().split()))

lst = []
for i in A:
    if i < X:
        lst.append(i)
print(*lst)

# 방법 2
# string으로 출력
N, X = map(int, input().split())
A = list(map(int, input().split()))

lst = ''
for i in A:
    if i < X:
        lst += str(i) + ' '
print(lst)
