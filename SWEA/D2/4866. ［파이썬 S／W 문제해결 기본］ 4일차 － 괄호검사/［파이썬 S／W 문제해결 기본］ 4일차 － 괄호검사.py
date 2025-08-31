T = int(input())

for tc in range(1, T+1):
    txt = input()

    stack = [0] * 100
    top = -1
    answer = 1

    for i in txt:
        if i in ['{', '(']:
            top += 1
            stack[top] = i
        elif i in ['}', ')']:
            if top == -1:
                answer = 0
                break
            elif i == '}':
                if stack[top] != '{':
                    answer = 0
                    break
            elif i == ')':
                if stack[top] != '(':
                    answer = 0
                    break
            top -= 1
    if top != -1:
        answer = 0

    print(f'#{tc} {answer}')