import string

S = input()

# 알파벳 리스트에 담기
lower = list(string.ascii_lowercase)

result = []
for i in lower:
    result.append(S.find(i))
print(*result)
