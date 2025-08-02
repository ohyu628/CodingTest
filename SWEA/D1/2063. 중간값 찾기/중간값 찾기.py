N = int(input())

number = list(map(int, input().split()))
# number 정렬
number.sort()
# 9//2=4 -> number[4] = 5번째 값 출력
print(number[len(number)//2])