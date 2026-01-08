# 대칭 문자열
# level, aabbaa > True
# hello, abcd > false
# 사용자로부터 입력 받은 문자열이 대칭 문자열인지 아닌지 판단


def ispalindrome(input):
    for i in range(len(input) // 2):
        if input[i] != input[-1 - i]:
            return False
    return True

# 재귀함수 이용
def ispalendrome2(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return ispalindrome(s[1:-1])
    else:
        return False


result = ispalendrome2("12321")
# ---------------------------------------------

# user = input()
# result = pa(user)
# print(f"대칭 문자열 입력 : {result}")

# 문자열 대소문자 바꾸기
# abCdefg >> ABcDeFG
# upper(), lower()


def change_str(s):
    temp = []
    for i in range(len(s)):
        if s[i].isupper():
            temp.append(s[i].lower())
        if s[i].islower():
            temp.append(s[i].upper())


# s.swapcase() 알아서 바꿔주는 메소드

# result = "".join([c.upper() if c.islower() else c.lower() for c in s])

result = change_str("abCdefg")
print(f"{result}")
