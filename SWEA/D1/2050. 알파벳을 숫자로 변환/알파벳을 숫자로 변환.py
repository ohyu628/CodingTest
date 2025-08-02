# 방법 1
S = input()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

for i in range(len(S)):
    if S[i] in alphabet:
        result = alphabet.index(S[i])
        print(number[result], end=' ')

# 방법 2
# ord 함수를 사용해 문자를 아스키코드로 변경
# 아스키코드로 A가 64여서 -64를 해주면 1부터 출력
S = input()
for i in S:
    print(ord(i)-64, end=' ')
