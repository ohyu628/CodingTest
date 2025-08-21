N, M = map(int, input().split())

basket = [0] * N
for i in range(N):
    basket[i] = i+1

for _ in range(M):
    i, j = map(int, input().split())

    if i == j:
        continue
    else:
        basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)