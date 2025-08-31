T = int(input())

for tc in range(1, T+1):
    txt = input()

    stack = [0] * len(txt)
    top = -1

    for i in txt:
        if top >= 0 and i == stack[top]:
            top -= 1
        else:
            top += 1
            stack[top] = i

    print(f'#{tc} {top+1}')