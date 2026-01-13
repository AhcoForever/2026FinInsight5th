def solution(numbers):
    answer = -1
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # range(0,10)
    for c in list:
        if c not in numbers:
            answer += c
    return answer
