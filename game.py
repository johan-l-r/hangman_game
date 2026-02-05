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
    ATTEMPTS = 6

    self.show_board(word)

    while ATTEMPTS > 0:
      self.show_popup()
      ATTEMPTS -= 1

    self.stdscr.refresh()

  def show_popup(self):
    letter = self.stdscr.getch()
    message = f"you typed the letter {chr(letter)}"

    POPUP_WIDTH = len(message) + 6
    POPUP_HEIGHT = 5

    message_x_pos = (POPUP_WIDTH - len(message)) // 2 
    message_y_pos = POPUP_HEIGHT // 2

    confirmation_popup = curses.newwin(POPUP_HEIGHT, POPUP_WIDTH, 4, 4)

    confirmation_popup.box()
    confirmation_popup.addstr(message_y_pos, message_x_pos, message)
    confirmation_popup.getch()

  def show_board(self, word):
    for char in word:
      if char == " ":
        self.stdscr.addstr(" ")
      else:
        self.stdscr.addstr("_ ")

  def quit(self):
    sys.exit()
