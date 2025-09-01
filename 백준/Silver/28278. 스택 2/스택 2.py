# 빠른 입력 처리 
import sys

N = int(sys.stdin.readline())

stack = [''] * (N+1)
top = -1

for _ in range(N):
    txt = sys.stdin.readline().split()

    if txt[0] == '1':
        top += 1
        stack[top] = txt[1]
    elif txt[0] == '2':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
    elif txt[0] == '3':
        print(top+1)
    elif txt[0] == '4':
        if top == -1:
            print(1)
        else:
            print(0)
    elif txt[0] == '5':
        if top == -1:
            print(-1)
        else:
            print(stack[top])