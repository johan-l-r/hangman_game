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

      self.stdscr.refresh()

  def play(self): 
    self.stdscr.clear()

    word = word_generator.get_random_word()
    self.show_board(word, len(word))
    self.stdscr.getch()

    self.stdscr.refresh()

  def show_board(self, word,  length):
    for char in word:
      if char == " ":
        self.stdscr.addstr(" ")
      else:
        self.stdscr.addstr("_ ")

  def quit(self):
    sys.exit()
