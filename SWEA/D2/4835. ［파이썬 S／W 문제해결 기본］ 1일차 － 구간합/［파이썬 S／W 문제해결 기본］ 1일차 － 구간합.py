# 내장 함수 사용 x
# 방법 1
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    max_v = 0
    min_v = 1e9
    for i in range(N-M+1):
        m_sum = 0
        for j in range(i, i+M):
            m_sum += a[j]
        if max_v  < m_sum:
            max_v = m_sum
        if min_v > m_sum:
            min_v = m_sum
    print(f'#{tc} {max_v - min_v}')

# 방법 2
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    max_v = 0
    min_v = 0
    for i in range(M):
        min_v += a[i]
        
    for i in range(N-M+1):
        m_sum = 0
        for j in range(i, i+M):
            m_sum += a[j]
        if max_v  < m_sum:
            max_v = m_sum
        if min_v > m_sum:
            min_v = m_sum
    print(f'#{tc} {max_v - min_v}')
