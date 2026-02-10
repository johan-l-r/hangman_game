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

    self.show_board(word)

    self.stdscr.refresh()

  def show_popup(self, message):
    POPUP_WIDTH = len(message) + 6
    POPUP_HEIGHT = 5

    message_x_pos = (POPUP_WIDTH - len(message)) // 2 
    message_y_pos = POPUP_HEIGHT // 2

    confirmation_popup = curses.newwin(POPUP_HEIGHT, POPUP_WIDTH, 4, 4)

    confirmation_popup.box()
    confirmation_popup.addstr(message_y_pos, message_x_pos, message)
    confirmation_popup.getch()

    # remove popup and wait for input
    confirmation_popup.clear()
    confirmation_popup.refresh()

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

      self.show_popup(f"you typed the letter {ch}")

      if ch not in word:
        ATTEMPTS -= 1
        continue

      # reveal letters
      for i, char in enumerate(word):
        if char == ch:
          board[i] = ch

  def quit(self):
    sys.exit()
