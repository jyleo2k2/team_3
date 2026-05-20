def show_score(scores):

    if len(scores) == 0:
        return "\n기록이 없습니다."

    else:

        result = "\n=== 점수 랭킹 ===\n"

        # 점수 높은 순
        ranking = sorted(scores, key=lambda x: x[1], reverse=True)

        for i in range(len(ranking)):

            result += (
                str(i + 1) + "등 : "
                + ranking[i][0]
                + " | 점수 : "
                + str(ranking[i][1])
                + "점\n"
            )

        return result