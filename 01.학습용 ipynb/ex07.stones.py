# 건널 수 있는 최대 인원은 리스트 안에 있는 최댓값과 같다.
# def solution(stones, k):
#     answer = 0
#     while k != 0:
#         for i in range(len(stones)):
#             while stones[i] == stones[len(stones) - 1]:
#                 k -= 1
#                 answer += 1
#                 # 0이 아닌 돌맹이 밟았을 때,
#                 if stones[i] > 0:
#                     stones[i] -= 1
#                     i+=1
#                 # 넘겨야할 돌맹이
#                 else :


#     return answer


def solutions2(stones, k):
    max_number = []
    for i in range(0, len(stones) - k + 1):
        m = max(stones[i : i + k])
        max_number.append(m)
    return min(max_number)


def solutions3(stones, k):
    left = 0
    right = max(stones)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        count = 0
        possible = True

    for s in stones:
        if s < mid:
            count = +1
            if count == 1:
                possible = False
                break

        else:
            count = 0

    if possible:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
    return answer
