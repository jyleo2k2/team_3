from od_or_even import OddEvenGame 

score_records = []

def main():
    while True:
        nickname = input("\n닉네임을 입력하세요 (종료하려면 'q' 입력): ")
        if nickname == "q":
            break
            
        game = OddEvenGame()
        score = game.start_game()
        
        score_records.append({"name": nickname, "score": score})
        
        print("\n[기록 보드]")
        for i, record in enumerate(score_records, 1):
            print(f"{i}번: {record['name']} {record['score']}점")

if __name__ == "__main__":
    main()