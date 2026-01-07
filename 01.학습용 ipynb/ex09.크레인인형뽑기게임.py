FRIENDS = {"a": 1, "b": 2, "c": 3}


def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for r in range(len(board)):
            if board[r][m - 1] != 0:  # 3 줄 타고 내려가면서 만나는 캐릭터
                if stack and stack[-1] == board[r][m - 1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[r][m - 1])
                board[r][m - 1] = 0
                break
    return answer
