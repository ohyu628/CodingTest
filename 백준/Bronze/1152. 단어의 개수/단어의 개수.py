# 방법 1
S = input()

lst = S.split()
print(len(lst))

# 방법 2
# map 함수 사용
S = list(map(str, input().split()))

print(len(S))
