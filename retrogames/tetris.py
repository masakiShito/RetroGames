# retrogames/tetris.py
import random
import curses

# Define shapes and rotations
shapes = [
    [['.....',
      '.....',
      '..00.',
      '..00.',
      '.....']],
    [['.....',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '0000.',
      '.....',
      '.....']],
    [['.....',
      '..0..',
      '000..',
      '.....',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '000..',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
]

def play_tetris():
    def create_grid(locked_positions={}):
        grid = [['.' for _ in range(10)] for _ in range(20)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in locked_positions:
                    grid[i][j] = '0'
        return grid

    def draw_grid(stdscr, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                stdscr.addstr(i, j, grid[i][j])
    
    def get_shape():
        return random.choice(shapes)
    
    def main(stdscr):
        locked_positions = {}
        grid = create_grid(locked_positions)
        current_piece = get_shape()
        change_piece = False
        while True:
            grid = create_grid(locked_positions)
            draw_grid(stdscr, grid)
            stdscr.refresh()
            stdscr.getch()

    curses.wrapper(main)
