import random
class NumberBaseball:
    def __init__(self):
        self.challenge =[]
        self.correct_answer = str(random.randint(1000,9999))

    def start_game(self):
        count = 0
        hidden_answer = ["_"] * len(self.correct_answer)
        print("[", " ".join(hidden_answer), "]")
        while True:
            ball = 0
            strike = 0

            my_answer = input("네자리 숫자를 입력하세요 : ")
            count += 1
            if my_answer in self.challenge:
                print("이미 입력했던 글자입니다.")
                count -= 1
                continue
            self.challenge.append(my_answer)

            correct_used = [False] * 4
            my_used = [False] * 4

            for i in range(4):
                if my_answer[i] == self.correct_answer[i]:
                    strike += 1
                    hidden_answer[i] = my_answer[i]
                    correct_used[i] = True
                    my_used[i] = True

            for i in range(4):
                if my_used[i]:
                    continue
                for j in range(4):
                    if correct_used[j]:
                        continue
                    if my_answer[i] == self.correct_answer[j]:
                        ball += 1
                        correct_used[j] = True
                        my_used[i] = True
                        break

            out = 4 - strike - ball
            print(f"{my_answer} : {strike}S,{ball}B,{out}O")
            print("[", " ".join(hidden_answer), "]")
            if strike == 4:
                print("★ ★ ★")
                print("성공!")
                score = 10 * (11 - count)
                print((11 - count) * 10, "점!")
                return score
            