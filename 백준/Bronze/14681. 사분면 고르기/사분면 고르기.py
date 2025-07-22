x = int(input())
y = int(input())

# Quadrant 1 x, y 모두 양수
# Quadrant 2 x 음수, y 양수
# Quadrant 3 x, y 모두 음수
# Quadrant 4 x 양수, y 음수
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)