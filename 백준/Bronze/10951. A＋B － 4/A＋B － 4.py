while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    # 에러 발생 시 while문 나가기
    except:
        break