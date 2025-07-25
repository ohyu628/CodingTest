N = int(input())
M = list(map(int, input().split()))
V = int(input())

count = 0
for i in range(len(M)):
    if V == M[i]:
        count += 1
print(count)