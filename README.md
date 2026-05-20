1. 구조

main.py : 메인 실행 파일

각각 게임 폴더에서 랭킹 클래스를 사용해서 점수 보관
이후 마지막으로 main에서 클래스 불러와서 점수 매기기

메인에서 1, 2, 3 입력받은 후 게임 실행, 4 입력 받으면 랭킹, 5 입력 받으면 종료

숫자 하나 입력받을 때 : 다음 함수 사용

def one_number_only(prompt):
    while True:
        num = input(prompt)
        try:
            num = int(num)
            if num in [1,2,3,4,5]:
                return num
            print("1 ~ 5 까지의 숫자를 입력해주세요.")
        except:
            print("숫자를 입력해주세요.")