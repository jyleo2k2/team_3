
import random
class NumberBaseball:
    def __init__(self,start,end):
        self.answer = random.randint(start,end)
        self.guess=["_"]*len(self.answer)
        self.tries=0


    def input_number(self):
        while True:
            while True:
                try:
                    number = int(input("네 자리 숫자를 입력하세요: "))
                    if number <1000:
                        print("숫자가 네자리 숫자가 아닙니다.")
                    return number
                except ValueError:
                    print("숫자만 입력해주세요.")

    def play(self):
        guess_list=[]
        while True:
            if "_" not in self.guess:
                print("승리하셨습니다.")
                score= 10*(11-self.tries)
                return score
                

            print("현재 상태:", ' '.join(self.guess))

            if len(guess_list) ==0:
                print("입력한 글자가 없습니다.")

            else:
                print("입력한 글자:", ' '.join(guess_list))

            guess_number=self.input_number()
            guess_list.append(guess_number)
            
            if len(guess_number)==4:
                self.tries+=1
                strike=0
                ball=0
                for i in range (len(self.answer)):
                    if self.answer[i] == guess_number:
                        self.answer[i]==guess_number
                if str(guess_number) not in str(self.answer):
                    print("O")
                for i in range(len(self.answer)):
                    if guess_number[i]==self.answer[i]:
                        strike+=1
                    elif guess_number[i] in self.answer:
                        ball+=1
                print(f"{strike}S{ball}B")


            


