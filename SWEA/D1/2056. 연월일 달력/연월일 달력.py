T = int(input())

for tc in range(1, T+1):
    date = input()

    result = ''
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
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