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