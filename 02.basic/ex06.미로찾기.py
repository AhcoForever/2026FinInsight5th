# 1. 지도 만들기
# 2. 움직임
# 3. 그리기
# 도착할 때까지(while) 그리기, 움직임 반복
# 4. 쥐는 왼쪽을 기준으로 감.

# 1 : 벽
# 0 : 길
# 3 : 골
import os
import time

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
]


def print_maze():
    global maze
    global mouse
    os.system("cls" if os.name == "nt" else "clear")
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if i == mouse["y"] and j == mouse["x"]:
                print("🐭", end="")
            elif maze[i][j] == 1:
                print("🧱", end="")
            elif maze[i][j] == 2:
                print("🚩", end="")
            elif maze[i][j] == 3:
                print("🏁", end="")
            else:
                print("  ", end="")
        print("")


N, E, S, W = 100, 101, 102, 103

mouse = {"x": 1, "y": 1, "direction": S}


def move_mouse():
    global mouse
    global maze

    # 남쪽 볼 때
    if mouse["direction"] == S:
        # 동
        if maze[mouse["y"]][mouse["x"] + 1] == 0:
            mouse["x"] = mouse["x"] + 1
            mouse["direction"] = E
        # 남
        elif maze[mouse["y"] + 1][mouse["x"]] == 0:
            mouse["y"] = mouse["y"] + 1
            mouse["direction"] = S
        # 서
        elif maze[mouse["y"]][mouse["x"] - 1] == 0:
            mouse["x"] = mouse["x"] - 1
            mouse["direction"] = W
        # 북
        else:
            mouse["y"] = mouse["y"] - 1
            mouse["direction"] = N
    # 쥐가 서쪽
    elif mouse["direction"] == W:
        # 서 > 남 > 북 > 동
        if maze[mouse["y"]][mouse["x"] + 1] == 0:
            mouse["x"] == mouse["x"] + 1
            mouse["direction"] == E
        elif maze[mouse["y"] + 1][mouse["x"]] == 0:
            mouse["y"] = mouse["y"] + 1
            mouse["direction"] = S
        elif maze[mouse["y"]][mouse["x"] - 1] == 0:
            mouse["x"] == mouse["x"] - 1
            mouse["direction"] == W
        else:
            mouse["y"] = mouse["y"] - 1
            mouse["direction"] == N

    # 쥐가 북쪽
    elif mouse["direction"] == N:
        # 북 > 동 > 남 > 서
        if maze[mouse["y"]][mouse["x"] + 1] == 0 or maze[mouse["y"]][mouse["x"]] == 3:
            mouse["x"] == mouse["x"] + 1
            mouse["direction"] == E
        elif maze[mouse["y"] + 1][mouse["x"]] == 0:
            mouse["y"] = mouse["y"] + 1
            mouse["direction"] = S
        elif maze[mouse["y"]][mouse["x"] - 1] == 0 or maze[mouse["y"]][mouse["x"]] == 3:
            mouse["x"] == mouse["x"] - 1
            mouse["direction"] == W
        else:
            mouse["y"] = mouse["y"] - 1
            mouse["direction"] == N

    # 쥐가 동쪽
    elif mouse["direction"] == E:
        # 북 > 동 > 남 > 서
        if maze[mouse["y" - 1]][mouse["x"]] == 0:
            mouse["y"] == mouse["y"] - 1
            mouse["direction"] == N
        elif maze[mouse["y"]][mouse["x"] + 1] == 0:
            mouse["x"] = mouse["x"] + 1
            mouse["direction"] == E
        elif maze[mouse["y"] + 1][mouse["x"]] == 0:
            mouse["direction"] == S
        else:
            mouse["x"] = mouse["x"] - 1
            mouse["direction"] == W


while maze[mouse["x"]][mouse["y"]] != 3:
    print_maze()
    move_mouse()
    time.sleep(1)
