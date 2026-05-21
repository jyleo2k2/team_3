# 이 파일이 메인 실행 파일입니다.

from ten_seconds.game import TenSeconds
from odd_or_even.game import OddEvenGame
from number_baseball.baseball_game import NumberBaseball

Game_1 = TenSeconds() # 10초게임
Game_2 = NumberBaseball() # 중복 4자리 숫자야구
Game_3 = OddEvenGame() # 홀짝

class App:
    def __init__(self):
        self.ranking_lst = [] # 랭킹 저장 리스트

    def _one_number_only(self, prompt): # 숫자 입력만
        while True:
            num = input(prompt)
            try:
                num = int(num)
                if num in [1,2,3]:
                    return num
                print("1 ~ 3 까지의 숫자를 입력해주세요.")
            except:
                print("숫자를 입력해주세요.")

    def ranking_append(self,name,total_score):
        self.ranking_lst.append([name,total_score]) # [이름,점수] 순으로 저장

    def run(self):
        
        while True:
            print("당신의 운을 시험해보세요..!!")
            print("1 : 게임 시작\n2 : 랭킹 보기\n3 : 게임 종료")
            num = self._one_number_only("1부터 3까지의 숫자를 입력해주세요. : ")
            if num == 1:
                score_lst = []
                total_score = 0

                score_lst.append(Game_1.start_game())
                score_lst.append(Game_2.start_game())
                score_lst.append(Game_3.start_game())
                total_score = int(sum(score_lst) / 3) # 100점 만점으로 계산
                print(f"총 점수 : {total_score}")

                name = input("\n닉네임을 입력해주세요 : \n")
                self.ranking_append(name,total_score)

            elif num == 2:
                
                print("----명예의 전당----")
                if self.ranking_lst:
                    self.ranking_lst.sort(key=lambda x: -x[1])
                    for i in range(min(3,len(self.ranking_lst))):
                        print(f"{i+1}위 : {self.ranking_lst[i][0]}, {self.ranking_lst[i][1]}")
                else:
                    print("기록이 없습니다.\n")
                
            elif num == 3:
                break
            else:
                print("1부터 3까지의 숫자를 입력해주세요...")

app = App()
app.run()