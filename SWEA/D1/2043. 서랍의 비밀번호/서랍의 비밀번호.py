P, K = map(int, input().split())

result = 0
for i in range(K-1, P):
    result += 1
print(result)