# index - 리스트, 문자열 모두 사용 가능한 함수
# find - 문자열만 사용 가능한 함수 
lst = []
for _ in range(9):
    N = int(input())

    lst.append(N)

print(max(lst))
print(lst.index(max(lst))+1)
