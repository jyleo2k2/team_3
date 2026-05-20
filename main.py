# 이 파일이 메인 실행 파일입니다.

def one_number_only(prompt): # 지울거임
    while True:
        num = input(prompt)
        try:
            num = int(num)
            if num in [1,2,3,4,5]:
                return num
            print("1 ~ 5 까지의 숫자를 입력해주세요.")
        except:
            print("숫자를 입력해주세요.")

while True:
    num = one_number_only("1 : 10초 맞추기\n2 : 커스텀 숫자야구\n3 : 홀짝\n4 : 랭킹 보기\n5 : 게임 종료")
    if num == 1:
        pass
    elif num == 2:
        pass
    elif num == 3:
        pass
    elif num == 4:
        pass
    elif num == 5:
        break