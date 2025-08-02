T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = ''
    for _ in range(N):
        Ci, Ki = map(str, input().split())
        result += Ci * int(Ki)
    print(f'#{tc}')
    for i in range(0, len(result), 10):
        print(result[i:i+10], sep='\n')