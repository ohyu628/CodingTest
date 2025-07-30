# 방법 1
S = input()

total = 0
for i in S:
    if i in ['A', 'B', 'C']:
        total += 2+1
    elif i in ['D', 'E', 'F']:
        total += 2+2
    elif i in ['G', 'H', 'I']:
        total += 2+3
    elif i in ['J', 'K', 'L']:
        total += 2+4
    elif i in ['M', 'N', 'O']:
        total += 2+5
    elif i in ['P', 'Q', 'R', 'S']:
        total += 2+6
    elif i in ['T', 'U', 'V']:
        total += 2+7
    elif i in ['W', 'X', 'Y', 'Z']:
        total += 2+8
print(total)

# 방법 2
S = input()

total = 0
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for i in range(len(S)):
    for j in dial:
        if S[i] in j:
            total += dial.index(j) + 3
print(total)
