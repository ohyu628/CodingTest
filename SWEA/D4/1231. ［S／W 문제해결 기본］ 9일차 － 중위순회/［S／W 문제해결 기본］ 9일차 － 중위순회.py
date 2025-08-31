def inorder(node):
    if node <= N:
        inorder(node*2)
        result.append(tree[node])
        inorder(node*2+1)


for tc in range(1, 11):
    N = int(input())

    tree = [''] * (N+1)

    for i in range(N):
        arr = input().split()

        tree[i+1] = arr[1]

        result = []
        inorder(1)

    print(f'#{tc}', end=' ')
    for i in range(len(result)):
        print(result[i], end='')
    print()