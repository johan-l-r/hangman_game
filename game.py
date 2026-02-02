import curses

from menu import Menu

class Game:
  def __init__(self, stdscr):
    self.stdscr = stdscr
    self.main_menu = Menu(
      stdscr, 
      ["play", "quit"], 
      curses.COLOR_WHITE, 
      curses.COLOR_BLACK
    )

  def run(self):
    while True:
      self.stdscr.clear()

      self.main_menu.show()
      self.main_menu.iterate()

      self.stdscr.refresh()
