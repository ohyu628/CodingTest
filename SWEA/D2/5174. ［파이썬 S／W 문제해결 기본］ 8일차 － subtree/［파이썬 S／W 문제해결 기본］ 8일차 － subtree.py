def inorder(T):
    if T == 0:
        return 0
    l = inorder(left[T])
    r = inorder(right[T])
    return l + r + 1


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    left = [0] * (E+2)
    right = [0] * (E+2)
    par = [0] * (E+2)

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        par[c] = p

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    print(f'#{tc} {inorder(N)}')
