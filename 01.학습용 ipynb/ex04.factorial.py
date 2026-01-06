# factorial
# 5! = 5 x 4 x 3 x 2 x 1 = 120

"""여러 방법
for n in range(n,1,-1):
    reuslt = result * n

for n in range(2, n+1):
    reuslt = result * i

"""


def factorial(num):
    a = 1
    while num >= 2:
        a *= num
        num -= 1

    return a


result = factorial(5)
print(f"{result}")

# -----------------------------
# 재귀함수 : 자기 자신을 다시 호출
# f(5) = 5 x f(4) 표현해보기


def factorial2(n):
    # n = 5
    # 5 * factorial2(4)
    # 5 * 4 * factorial2(3)
    # 5 * 4 * 3 * 2 * 1
    if n <= 1:
        return 1
    else:
        return n * factorial2(n - 1)


print(f"5! = {factorial2(5)}")
