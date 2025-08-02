# 방법 1
N = int(input())

result =[]
for i in range(N,-1,-1):
    result.append(i)
print(*result)

# 방법 2
N = int(input())

for i in range(N, -1, -1):
    print(i, end=" ")
