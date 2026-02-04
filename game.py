import curses
import sys

from menu import Menu
import word_generator

class Game:
  def __init__(self, stdscr):
    self.stdscr = stdscr
    self.main_menu = Menu(
      stdscr, 
      ["PLAY", "QUIT"], 
      curses.COLOR_WHITE, 
      curses.COLOR_BLACK
    )
    self.main_menu.add_event(self.play)
    self.main_menu.add_event(self.quit)

  def run(self):
    while True:
      self.stdscr.clear()

      self.main_menu.show()
      self.main_menu.iterate()

      self.stdscr.refresh()

  def play(self): 
    self.stdscr.clear()
    self.stdscr.addstr(4, 4, str(word_generator.get_random_word()))
    self.stdscr.refresh()
    self.stdscr.getch()

  def quit(self):
    sys.exit()
