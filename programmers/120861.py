"""
[0, 0]은 board의 정 중앙에 위치한다.
-1, 0 / 0, 0 / 0, 1 / 1, 1 / 2, 1
입력이 벗어나면 무시하자

"""
def solution(keyinput, board):
    answer = 0
    curr = [0, 0]
    for k in keyinput:
        if k == 'left' and abs(curr[0] - 1) <= board[0] / 2:
            curr[0] -= 1
        elif k == 'right'and abs(curr[0] + 1) <= board[0] / 2:
            curr[0] += 1
        elif k == 'up' and abs(curr[1] + 1) <= board[1] / 2:
            curr[1] += 1
        elif k == 'down' and abs(curr[1] - 1) <= board[1] / 2:
            curr[1] -= 1
        else:
            pass


    return curr

keyinput = ["down", "down", "down", "down", "down"]
board = [7, 9]
answer = solution(keyinput, board)
print(f"answer >> {answer}")