# 방법 1
N = int(input())

def factorial(cnt):
    total = 1
    for i in range(1, cnt + 1):
        total *= i
    return total

result = factorial(N)
print(result)