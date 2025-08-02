# 학생 출석번호 생성
student = [i for i in range(1, 31)]

# 과제 낸 학생만큼 반복문 실행
for i in range(28):
    N = int(input())
    student.remove(N)
print(min(student))
print(max(student))



