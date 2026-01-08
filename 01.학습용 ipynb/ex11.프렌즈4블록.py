EMPTY = "%"


def solution(m, n, board):
    answer = 0

    while True:
        mem = set()

        # 4개, 지울 애를 찾음
        for r in range(m - 1):
            for c in range(n - 1):
                if (
                    board[r][c]
                    == board[r][c + 1]
                    == board[r + 1][c]
                    == board[r + 1][c + 1]
                    and board[r][c] != EMPTY
                ):
                    mem |= set([(r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)])

        # 사라진 블록수 추가
        cnt = len(mem)
        if cnt == 0:
            break
        answer += cnt

        # 지우고 (r, c)
        for r, c in mem:
            board[r] = board[r][0:c] + EMPTY + board[r][c + 1 :]

        # 떨어트리고
        for r in range(m - 2, -1, -1):
            for c in range(n):
                if board[r][c] != EMPTY:
                    for r2 in range(m - 1, r, -1):
                        if board[r2][c] == EMPTY:
                            # SWAP
                            board[r2] = (
                                board[r2][0:c] + board[r][c] + board[r2][c + 1 :]
                            )
                            board[r] = board[r][0:c] + EMPTY + board[r][c + 1 :]

    return answer


board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# CCBDE
# AAADE
# AAABF
# CCBBF
print(solution(4, 5, board))
