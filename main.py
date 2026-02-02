import curses
from game import Game

from curses import wrapper

def main(stdscr):
  game = Game(stdscr)
  game.run()

wrapper(main)
