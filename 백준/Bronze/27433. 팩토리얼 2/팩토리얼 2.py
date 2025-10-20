# 방법 1
N = int(input())

def factorial(cnt):
    total = 1
    for i in range(1, cnt + 1):
        total *= i
    return total

result = factorial(N)
print(result)

# 방법 2
N = int(input())

def factorial(cnt):
    if cnt > 1:
        return cnt * factorial(cnt - 1)
    else:
        return 1

result = factorial(N)
print(result)

# 방법 3
import math

N = int(input())

result = math.factorial(N)
print(result)
