# https://school.programmers.co.kr/learn/courses/30/lessons/17679


def pop_set(m, n, board):
    pop_set = set()
    for i in range(1, n):
        for j in range(1, m):
            if (
                board[i][j]
                == board[i - 1][j - 1]
                == board[i - 1][j]
                == board[i][j - 1]
                != "_"
            ):
                pop_set |= set([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])

    for i, j in pop_set:
        board[i][j] = 0
    for idx, row in enumerate(board):
        empty = ["_"] * row.count(0)
        board[idx] = empty + [block for block in row if block != 0]
    return len(pop_set)


def solution(m, n, board):
    # board = list(map(list, zip(*board)))
    my_board = []

    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(board[j][i])
        my_board.append(tmp)

    answer = 0
    while True:
        count = pop_set(m, n, my_board)
        if count == 0:
            return answer
        answer += count


if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
