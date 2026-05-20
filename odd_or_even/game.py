import random

class OddEvenGame:
    def __init__(self):
        self.total_rounds = 10
        self.correct_count = 0
        self.final_score = 0

    def start_game(self):

       
        self.total_rounds = 10
        print(" 홀짝 게임을 시작합니다.")
        print(f"본 게임은 총 {self.total_rounds}회 진행되며, 100점에서 틀릴 때마다 10점씩 차감됩니다.")
        self.correct_count = 0 

       
        for round_num in range(1, self.total_rounds + 1):
            print(f"{round_num}번째 라운드/총 {self.total_rounds}회")
            
            computer_num = random.randint(1, 100)
            computer_answer = "홀" if computer_num % 2 != 0 else "짝"
            while True:
                user_guess = input("홀? 또는 짝? 입력하세요: ").strip() # strip()은 앞뒤 공백 제거
                
                if user_guess == "홀" or user_guess == "짝":
                    break
                else:
                    print(" 잘못된 입력입니다. '홀' 또는 '짝' 중에서만 정확히 입력해 주세요.")
            

            if user_guess == computer_answer:
                print("정답입니다!")
                print(f"컴퓨터의 숫자: {computer_num} [{computer_answer}]")
                self.correct_count += 1
            else:
                print("틀렸습니다!")
                print(f"컴퓨터의 숫자: {computer_num} [{computer_answer}]")

        self.final_score = 100 - ((self.total_rounds - self.correct_count) * 10)

        print("Game Over")
        print("---------Total Score----------")
        print(f"총 진행 횟수: {self.total_rounds}회")
        print(f"맞춘 횟수: {self.correct_count}회")
        print(f"최종 점수: {self.final_score}점")
        
      
        return self.final_score
