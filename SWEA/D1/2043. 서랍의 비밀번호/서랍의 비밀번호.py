# 방법 1
P, K = map(int, input().split())

result = 0
for i in range(K-1, P):
    result += 1
print(result)

# 방법 2
P, K = map(int, input().split())

print((P-K)+1)
