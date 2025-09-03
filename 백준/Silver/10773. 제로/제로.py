K = int(input())

arr = [int(input()) for _ in range(K)]

stack = [0] * (K+1)
top = -1

for i in arr:
    if i == 0:
        stack.pop(top)
        top -= 1
    else:
        top += 1
        stack[top] = i
    
result = 0
for i in stack:
    result += i

print(result)