T = int(input())

for _ in range(T):
    txt = input()

    stack =[''] * (len(txt))
    top = -1
    result = "YES"

    for i in txt:
        if i == '(':
            top += 1
            stack[top] = i
        elif i == ')':
            if stack[top] == '(':
                top -= 1
            elif top == -1:
                result = "NO"
                break
    
    if top != -1:
        result = "NO"
    print(result)