# 이 파일이 메인 실행 파일입니다.

import random
challenge =[]
correct_answer = str(random.randint(1000,9999))

def number_baseball(correct_answer, challenge):
    count = 0
    print(correct_answer)
    hidden_answer = ["_"] * len(correct_answer)
    print("["," ".join(hidden_answer),"]")
    while True:
        ball = 0
        strike = 0
        out = 0 
        my_answer = input("네자리 숫자를 입력하세요 : ")
        count += 1
        if my_answer in challenge:
            print("이미 입력했던 글자입니다.")
            count -= 1
            continue  
        challenge.append(my_answer)
        for i in range (len(correct_answer)):
            if my_answer[i] != correct_answer[i] and my_answer[i] in correct_answer:
                ball += 1
            elif my_answer[i] == correct_answer [i]:
                strike += 1
                hidden_answer[i] = my_answer[i]
            else:
                out += 1
        print(f"{my_answer} : {strike}S,{ball}B,{out}O")
        if strike == 4 :
            print("★ ★ ★")
            print("성공!")
            break
        print("["," ".join(hidden_answer),"]")
        print(count)

number_baseball(correct_answer, challenge)