# 방법 1
T = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T+1):
    date = input()

    result = ''
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])

    if year >= 1:
        result += str(year).zfill(4)+"/"
        if 1 <= month <= 12:
            result += str(month).zfill(2)+"/"
            if 1 <= day <= days[month-1]:
                result += str(day).zfill(2)
            else:  
                result = "-1"
        else:  
            result = "-1"
    else:  
        result = "-1"

    print(f'#{tc} {result}')

# 방법 2
# year가 0000이 있으면 문제가 될 수 있음
T = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T+1):
    date = input()

    month = int(date[4:6])
    day = int(date[6:])
    result = date[0:4] + '/' + date[4:6] + '/' + date[6:]
    if (1 <= month <= 12) and (1 <= day <= days[month-1]):
        print(f'#{tc} {result}')
    else:
        print(f'#{tc}', -1)
