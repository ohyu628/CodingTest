T = input()

# ord() - 문자를 아스키코드로 변경해주는 함수
if type(T) == str:
    print(ord(T))
# chr() - 숫자를 아스키코드로 변경해주는 함수
elif type(T) == int:
    print(chr(T))