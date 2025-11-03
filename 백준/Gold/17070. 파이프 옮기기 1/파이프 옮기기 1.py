N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

# 우, 하, 대각선
dr = [0, 1, 1]
dc = [1, 0, 1]

q = [(0, 1, 'width')]
total = 0

while q:
    r, c, dir = q.pop()

    # N, N에 도착하면 카운트
    if r == N-1 and c == N-1:
        total += 1

    # 가로 파이프
    if dir == 'width':
        count = 0
        for d in range(3):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and house[nr][nc] == 0:
                count += 1
                if d == 0:
                    q.append((nr, nc, 'width'))
                if count == 3:
                    q.append((nr, nc, 'diagonal'))
    # 대각선 파이프
    elif dir == 'diagonal':
        count = 0
        for d in range(3):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and house[nr][nc] == 0:
                count += 1
                if d == 0:
                    q.append((nr, nc, 'width'))
                elif d == 1:
                    q.append((nr, nc, 'height'))
                if count == 3:
                    q.append((nr, nc, 'diagonal'))
    # 세로 파이프
    elif dir == 'height':
        count = 0
        for d in range(3):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and house[nr][nc] == 0:
                count += 1
                if d == 1:
                    q.append((nr, nc, 'height'))
                if count == 3:
                    q.append((nr, nc, 'diagonal'))

print(total)