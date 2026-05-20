import random
class NumberBaseball:
    def __init__(self):
        self.challenge =[]
        self.correct_answer = str(random.randint(1000,9999))

    def start_game(self):
        print("\n==== 2. 네자리 숫자 야구 ====")
        count = 0
        hidden_answer = ["_"] * len(self.correct_answer)
        print("["," ".join(hidden_answer),"]")
        while True:
            ball = 0
            strike = 0
            out = 0 
            my_answer = input("네자리 숫자를 입력하세요 : ")
            count += 1
            if my_answer in self.challenge:
                print("이미 입력했던 글자입니다.")
                count -= 1
                continue  
            self.challenge.append(my_answer)
            for i in range (len(self.correct_answer)):
                if my_answer[i] != self.correct_answer[i] and my_answer[i] in self.correct_answer:
                    ball += 1
                elif my_answer[i] == self.correct_answer [i]:
                    strike += 1
                    hidden_answer[i] = my_answer[i]
                else:
                    out += 1
            print(f"{my_answer} : {strike}S,{ball}B,{out}O")
            if strike == 4 :
                print("★ ★ ★")
                print("성공!")
                score=10*(11-count)
                return score