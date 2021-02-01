from models.solver import Solver
from models.GUI import GUI
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
          res = solver.solve()
          if res == "QUIT":
            run = False
          elif res == "IMPOSSIBLE":
            run = False

    win.fill((255, 255, 255))
    board_GUI.draw()
    pygame.display.update()

if __name__ == "__main__":
  main()
  pygame.quit()
