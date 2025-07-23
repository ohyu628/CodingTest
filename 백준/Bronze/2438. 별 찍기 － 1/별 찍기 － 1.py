# 방법 1
N = int(input())

for i in range(1, N+1):
    print('*'*i)

# 방법 2
result = ""
N = int(input())

for i in range(N): # 열
    for j in range(i+1): # 행
        result += "*"
    result += "\n"
print(result)
