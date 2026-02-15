import curses
import sys

from menu import Menu
import word_generator
from popup import Popup

class Game:
  def __init__(self, stdscr):
    self.stdscr = stdscr
    self.main_menu = Menu(
      stdscr, 
      ["PLAY", "QUIT"], 
      curses.COLOR_WHITE, 
      curses.COLOR_BLACK
    )

    self.popup = Popup(4)
    self.used_letters = []

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

    self.show_board(word)

    self.stdscr.refresh()

  def show_board(self, word):
    ATTEMPTS = 6

    board = ["_"] * len(word)

    while ATTEMPTS > 0:
      self.stdscr.clear()
      self.stdscr.addstr(0, 0, "  ".join(board))
      self.stdscr.refresh()

      letter = self.stdscr.getch()

      if letter == -1:
        continue

      ch = chr(letter)

      self.popup.show(f"\nyou typed the letter {ch}")

      if not self.popup.confirm(): continue

      if ch in self.used_letters: 
        self.popup.show("you already used this letter")
        if not self.popup.confirm(): continue

        continue

      if ch not in word:
        ATTEMPTS -= 1
        self.used_letters.append(ch)

        continue

      # reveal letters
      self.used_letters.append(ch)

      for i, char in enumerate(word):
        if char == ch:
          board[i] = ch

  def quit(self):
    sys.exit()
