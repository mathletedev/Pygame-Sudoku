from time import time
from copy import deepcopy

class Solver:
  def __init__(self, board, GUI=None):
    self.board = board
    self.timer = None
    self.GUI = GUI

  def solve(self):
    tmp = deepcopy(self.board)

    pointer = 0
    direction = 1

    while True:
      if (pointer < 0):
        return None

      pos_x = pointer % 9
      pos_y = pointer // 9

      if (pointer > len(tmp) ** 2 - 1):
        return tmp

      if (self.board[pos_y][pos_x] > 0):
        pointer += direction
        continue

      if tmp[pos_y][pos_x] < 9:
        if self.valid(tmp, tmp[pos_y][pos_x] + 1, (pos_x, pos_y)):
          tmp[pos_y][pos_x] += 1
          pointer += 1
          direction = 1
          continue

        tmp[pos_y][pos_x] += 1
      else:
        tmp[pos_y][pos_x] = 0
        pointer -= 1
        direction = -1

  def valid(self, tmp, num, pos):
    for i in range(len(self.board)):
      if (tmp[pos[1]][i] == num or tmp[i][pos[0]] == num):
        return False

    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
      for j in range(box_x * 3, box_x * 3 + 3):
        if (tmp[i][j] == num):
          return False

    return True

  def parse_board(self, board):
    joined = []

    for i in range(len(board)):
      joined.append(" | ".join([str(s) for s in board[i]]))

    return ("\n" + "-" * 33 + "\n").join(joined)

  def start_timer(self):
    self.timer = round(time() * 1000)

  def get_time(self):
    return round(time() * 1000) - self.timer

if __name__ == "__main__":
  board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
  ]

  solver = Solver(board)

  solver.start_timer()
  res = solver.solve()
  current = solver.get_time()

  print(solver.parse_board(res))
  print("Solved in " + str(current) + "ms")