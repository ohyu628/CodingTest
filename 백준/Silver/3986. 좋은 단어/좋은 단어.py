N = int(input())

count = 0

for _ in range(N):
    word = input()

    stack = [0] * (len(word)+1)
    top = -1

    for i in word:
        if top != -1 and stack[top] == i:
            top -= 1
        else:
            top += 1
            stack[top] = i

    if top == -1:
        count += 1

print(count)