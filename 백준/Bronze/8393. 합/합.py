n = int(input())

# 누적합 저장할 변수
# for문 안에 설정하면 매번 0으로 재설정되기 때문에 밖에 설정해줘야 함
result = 0

for i in range(1, n+1):
    result += i
print(result)
