# 이 파일이 메인 실행 파일입니다.

from ten_seconds.game import TenSeconds
from odd_or_even.game import OddEvenGame
from number_baseball.baseball_game import NumberBaseball

Game_1 = TenSeconds()
Game_2 = NumberBaseball()
Game_3 = OddEvenGame()

def one_number_only(prompt): # 지울거임
    while True:
        num = input(prompt)
        try:
            num = int(num)
            if num in [1,2,3]:
                return num
            print("1 ~ 3 까지의 숫자를 입력해주세요.")
        except:
            print("숫자를 입력해주세요.")

while True:
    print("당신의 운을 시험해보세요..!!")
    print("1 : 게임 시작\n2 : 랭킹 보기\n3 : 게임 종료")
    num = one_number_only("1부터 3까지의 숫자를 입력해주세요. : ")
    if num == 1:
        score_1 = Game_1.start_game()
        score_2 = Game_2.play()
        score_3 = Game_3.start_game()
        print(f"총 점수 : {score_3}")
    elif num == 2:
        pass
    elif num == 3:
        break