T = int(input())

for tc in range(1, T+1):
    input()
    score = list(map(int, input().split()))
    max_idx = 0

    visited = [0] * 101
    for i in score:
        visited[i] += 1
        if visited[i] >= visited[max_idx]:
            max_idx = i
    print(f'#{tc} {max_idx}')