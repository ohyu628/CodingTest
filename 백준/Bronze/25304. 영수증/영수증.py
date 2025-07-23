# 방법 1
# for문 안에 if문을 넣게 되면 total이 바로 출력을 하기 때문에 바깥에 작성해줘야 함
X = int(input())
N = int(input())

total = 0
for i in range(N):
    a, b = map(int, input().split())
    total += a*b

if total == X:
    print("Yes")
else:
    print("No")

# 방법 2
# 반복 변수가 필요하지 않을 때 for문에 _(언더바) 사용
X = int(input())
N = int(input())

total = 0
for _ in range(N):
    a, b = map(int, input().split())
    total += a*b

if total == X:
    print("Yes")
else:
    print("No")
