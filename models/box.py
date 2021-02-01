import pygame

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