EMPTY = 100
BLACK = 0
WHITE = 1
def init_board():
    board = [[EMPTY] * 8 for _ in range(8)]
    board[3][3], board [4][4] = BLACK, BLACK
    board[4][4], board[3][4] = WHITE, WHITE
    return board


def print_board(board):
    print("=" * 20)
    numbers = ["0", "1","2","3","4","5","6","7"]
    for i, r in enumerate(board):
        
def check_reverse(y,x,turn,board):
    directions=[
        (-1,-1), (0, -1), (1, -1),
        (-1,0),     (1,0),
        (-1,1),  (0, 1), (1, 1)
    ]
    
    result = set()
    
    for dx, dy in directions:
        dx = -1
        dy = 0
        px = x + dx
        py = y + dy
        target = []
        is_catch=False
        while 0 <= px < 8 and 0 <= py < 8:
            if board[py][px] != turn and board[py][px] != EMPTY: # 다른 돌
                target.append((py, px))
                px += dx
                py += dy
            elif board[py][px] == EMPTY:
                break
            elif board[py][px] == turn:
                is_catch= True
                break
        if is_catch:
            result = result | set(target)
            
    return list(target)

    # return [(1,3)] # 뒤집을 수 없을 때 결과값
def drop_doll(y,x,turn, board):
    if board[y][x] != EMPTY:
        return False
    result = check_reverse(y,x,turn,board)
    if result: # 뒤집을 수 있다. 
        board[y][x] = turn
        for r, c in result:
            board[r][c] = turn
        return True
    else: # 뒤집을 수 있는게 없다
        return False
    
    
if __name__ == "__main__":
    board = init_board()
    turn = BLACK
    
    while True:
        print_board(board)
        user = input(f"{"⚫️" if turn == BLACK else "⚪️"}(yx):")
    