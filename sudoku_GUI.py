from sudoku_solver import Solver
import pygame

pygame.font.init()

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

class GUI:
  def __init__(self, board, rows, size, win):
    self.rows = rows
    self.size = size
    self.board = board
    self.boxes = [[Box(board[i][j], i, j, rows, size, win) for j in range(rows)] for i in range(rows)]
    self.win = win

  def draw(self):
    self.draw_lines()

    for i in range(self.rows):
      for j in range(self.rows):
        self.boxes[i][j].draw()

  def draw_lines(self):
    gap = self.size / self.rows
    for i in range(self.rows + 1):
      pygame.draw.line(self.win, (0, 0, 0), (0, i * gap), (self.size, i * gap))
      pygame.draw.line(self.win, (0, 0, 0), (i * gap, 0), (i * gap, self.size))

  def sleep(self, time):
    pygame.display.update()
    pygame.time.delay(time)

class Box:
  def __init__(self, value, row, col, rows, size, win):
    self.value = value
    self.row = row
    self.col = col
    self.rows = rows
    self.size = size
    self.win = win

  def draw(self):
    font = pygame.font.SysFont("comicsans", 40)

    gap = self.size / self.rows
    pos_x = self.col * gap
    pos_y = self.row * gap

    if not (self.value == 0):
      text = font.render(str(self.value), 1, (0, 0, 0))
      self.win.blit(text, (pos_x + (gap / 2 - text.get_width() / 2), pos_y + (gap / 2 - text.get_height() / 2)))

  def redraw(self):
    font = pygame.font.SysFont("comicsans", 40)

    gap = self.size / self.rows
    pos_x = self.col * gap
    pos_y = self.row * gap

    pygame.draw.rect(self.win, (255, 255, 255), (pos_x, pos_y, gap, gap), 0)

    if not (self.value == 0):
      text = font.render(str(self.value), 1, (0, 0, 0))
      self.win.blit(text, (pos_x + (gap / 2 - text.get_width() / 2), pos_y + (gap / 2 - text.get_height() / 2)))

  def set_value(self, value):
    self.value = value

def main():
  win = pygame.display.set_mode((512, 512))
  pygame.display.set_caption("Sud0ku So1ver")
  board_GUI = GUI(board, len(board), 512, win)
  solver = Solver(board, board_GUI)

  run = True
  solving = False

  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and not solving:
          solving = True
          solver.solve()

    win.fill((255, 255, 255))
    board_GUI.draw()
    pygame.display.update()

if __name__ == "__main__":
  main()
  pygame.quit()
