def solution(s):
    answer = ""
    data = s.split(" ")

    for i in data:
        for j in range(len(i)):
            if j % 2 == 1:
                # 소문자
                answer += i[j].lower()
            else:
                answer += i[j].upper()
        answer += " "ㅌ
    # answer.strip() # 공백을 지워주는 함수
    return answer.strip()


s = "tryy hello world"
result = solution(s)
print(result)
