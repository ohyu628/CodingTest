T = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T+1):
    n = list(map(int, input().split()))

    m1 = n[0]
    m2 = n[2]
    d1 = n[1]
    d2 = n[3]
    result = 0

    if m1 == m2:
        result = (d2 - d1) + 1
    else:
        for i in range(m1, m2+1):
            if i == m1:
                result += (days[i-1] - d1) + 1
            elif i == m2:
                result += d2
            else:
                result += days[i-1]

    print(f'#{tc} {result}')