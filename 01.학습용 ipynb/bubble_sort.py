# 2개씩 비교 - 큰 수는 옆으로 보냄
# 토너먼트 형식임.
#
#

number = [10, 8, 6, 7, 5, 9]
temp = 0
for i in range(len(number) - 1):
    for j in range(len(number) - 1 - i):
        if number[j] > number[j + 1]:
            temp = number[j]
            number[j] = number[j + 1]
            number[j + 1] = temp
            # number[j],number[j+1] = number[j+1], number[j]
print(number)
