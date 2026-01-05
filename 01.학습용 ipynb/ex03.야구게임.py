# 야구 게임
# 정답인 숫자 3개 - 중복 X 한 자리 마다 0~9 (랜덤 함수)
# 사용자가 맞추는 게임 
# 예: (4,1,3) 같은 자리는 strike 자리는 안같지만 숫자가 존재하면 ball
# 결과 : 1S, 1B
# 맞는게 하나도 없으면 out
# 3s가 나올 때까지 게임은 계속됨..

# 정답 생성
# 정답 제출
# 사용자 입력
# 판단
# 3S가 될 때까지 출력
import random
def generate_number():
    num = random.sample(range(0,10),3)
    # 출력 예: [1,2,3]
    return f"{num[0]}{num[1]}{num[2]}"
    # "123"

def check_answer(a,u):
    point = {
        "S" : 0, # 같은 자리 같은 숫자
        "B" : 0, # 다른 자리 같은 숫자
    }
    for i in range(3):
        if a[i] ==u[i]:
            point["S"] +=1
        elif a[i] in u:
            point["B"] +=1
        
    return point


answer = generate_number()


result = {
    "S": 0,
    "B": 0
}

while result["S"] != 3:
    user = input("숫자입력: ")
    result = check_answer(answer, user)
    print(f"s:: {result["S"]} / b: {result["B"]}")

print("게임 끝")

