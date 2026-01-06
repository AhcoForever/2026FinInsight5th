"""1. art: 시각적으로 글씨 써주기
# https://pypi.org/project/art/
from art import tprint

tprint("PYTHON", font="block")
tprint("HELLO", font="random")

"""

# 2. 텍스트를 음성으로

# https://pypi.org/project/gTTS/
from gtts import gTTS

text = "한솔 행동"

# lang='ko'는 한국어
tts = gTTS(text=text, lang="ko")
tts.save("voice_hansol.mp3")

print("voice.mp3 파일이 생성되었습니다. 실행해보세요!")

"""
# 3. 웹서버 제작

from flask import Flask, jsonify
import random

app = Flask(__name__)


# 1. 인사
# 주소: http://127.0.0.1:5000/
@app.route("/")
def home():
    return jsonify({"status": "Server is running", "message": "Hello Flask"})


# 2. 오늘의 점심 메뉴 추천 API
# 주소: http://127.0.0.1:5000/menu
@app.route("/menu")
def get_menu():
    foods = [
        {"name": "짜장면"},
        {"name": "김치찌개"},
        {"name": "돈까스"},
        {"name": "떡볶이"},
        {"name": "제육볶음"},
    ]
    recommendation = random.choice(foods)

    return jsonify({"menu_list": foods, "today_pick": recommendation})


# 3. 덧셈 계산기 API (URL로 데이터 받기)
# 주소: http://127.0.0.1:5000/sum/10/20
@app.route("/sum/<int:a>/<int:b>")
def sum_numbers(a, b):
    result = a + b
    return jsonify(
        {
            "input_a": a,
            "input_b": b,
            "result": result,
            "description": f"{a}와 {b}를 더한 값입니다.",
        }
    )


if __name__ == "__main__":
    print("🚀 서버가 시작! http://127.0.0.1:5000 으로 접속해보기")
    app.run(debug=True, port=5000)



"""
