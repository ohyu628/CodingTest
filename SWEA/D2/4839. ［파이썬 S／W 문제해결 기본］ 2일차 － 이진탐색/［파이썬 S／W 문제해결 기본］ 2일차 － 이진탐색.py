def binarySearch(N, key):
    start = 1
    end = N
    count = 0
    while start <= end:
        middle = (start + end) // 2
        count += 1
        if middle == key:
            return count
        elif middle > key:
            end = middle
        else:
            start = middle
    return count

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    A = binarySearch(P, Pa)
    B = binarySearch(P, Pb)

    if A > B:
        print(f'#{tc} B')
    elif A < B:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')