def show_score(scores):

    if len(scores) == 0:
        print("\n기록이 없습니다.")

    else:
        print("\n=== 점수 랭킹 ===")

        # 점수 높은 순
        ranking = sorted(scores, key=lambda x: x[1], reverse=True)

        for i in range(len(ranking)):
            print(
                i + 1, "등 :",
                ranking[i][0],
                "| 점수 :", ranking[i][1], "점"
            )