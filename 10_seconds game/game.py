import time

def start_game(scores):

    nickname = input("\n닉네임을 입력하세요 : ")

    print("\n=== 10초 맞추기 게임 ===")
    input("시작하려면 Enter를 누르세요!")

    start = time.time()

    input("10초라고 생각되는 바로 그 순간에 Enter를 누르세요!")

    end = time.time()

    result = end - start
    difference = abs(10 - result)

    score = 100 - int(difference * 10)

    if score < 0:
        score = 0

    print("\n당신의 기록 :", round(result, 2), "초")
    print("10초와의 차이 :", round(difference, 2), "초")
    print("점수 :", score, "점")

    scores.append([nickname, score])

    if difference <= 0.5:
        print("대박! 거의 정확합니다!")
    elif difference <= 1:
        print("잘했어요!")
    else:
        print("아쉬워요! 다시 도전!")