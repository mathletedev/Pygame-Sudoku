from models.box import Box
import pygame

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