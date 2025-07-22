# B를 list로 바꿔서 풀으려고 했지만 문자열로 받아 정수로 변경해주는게 더 쉬움
# 방법 1
# reversed() - 역순으로 뒤집는 함수
A = int(input())
B = input()

for i in reversed(B):
    print(A * int(i))
print(A * int(B))

# 방법 2
# range(start, stop, step)
A = int(input())
B = input()

for i in range(2, -1,-1):
    print(A * int(B[i]))
print(A * int(B))
