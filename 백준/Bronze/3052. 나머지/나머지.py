result = set()

for _ in range(10):
    N = int(input())

    if N % 42 not in result:
        result.add(N%42)
print(len(result))