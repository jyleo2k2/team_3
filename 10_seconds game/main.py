from game import start_game
from score import show_score

scores = []

while True:
    print("\n--- 메뉴 ---")
    print("1. 게임 시작")
    print("2. 점수 보기")
    print("3. 게임 종료")

    x = int(input("1-3번 중 번호를 입력하시오: "))

    if x == 1:
        start_game(scores)

    elif x == 2:
        show_score(scores)

    elif x == 3:
        print("게임을 종료합니다.")
        break

    else:
        print("잘못 입력했습니다.")