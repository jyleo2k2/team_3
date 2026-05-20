import time

def start_game(scores):

    input("시작하려면 Enter를 누르세요!")

    start = time.time()

    input("10초라고 생각되는 바로 그 순간에 Enter를 누르세요!")

    end = time.time()

    result = end - start
    difference = abs(10 - result)

    score = 100 - int(difference * 10)

    if score < 0:
        score = 0

    scores.append(score)

    print(score)

    return score