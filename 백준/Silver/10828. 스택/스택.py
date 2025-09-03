import sys

N = int(sys.stdin.readline())

stack = [''] * N
top = -1

for _ in range(N):
    txt = sys.stdin.readline().split()

    if txt[0] == 'push':
        top += 1
        stack[top] = txt[1]
    elif txt[0] == 'pop':
        if top != -1:
            print(stack[top])
            top -= 1
        else:
            print(-1)
    elif txt[0] == 'size':
        print(top+1)
    elif txt[0] == 'empty':
        if top != -1:
            print(0)
        else:
            print(1)
    elif txt[0] == 'top':
        if top != -1:
            print(stack[top])
        else:
            print(-1)