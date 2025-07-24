import sys

# 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 발생할 수 있음
# -> sys.stdin.readline()을 사용히먄 이를 예방할 수 있음
T = int(sys.stdin.readline())

for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)