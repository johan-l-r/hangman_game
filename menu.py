import curses


class Menu:
  def __init__(
      self, 
      stdscr, 
      menu, 
      SELECTED_BG_COLOR, 
      SELECTED_FG_COLOR
    ):
    self.stdscr = stdscr
    self.menu = menu
    self.selected_index = 0

    curses.init_pair(1, SELECTED_FG_COLOR, SELECTED_BG_COLOR)

  def iterate(self): 
    key = self.stdscr.getch()

    if key == ord("j") and self.selected_index < len(self.menu) - 1:
      self.selected_index += 1 

    if key == ord("k") and self.selected_index > 0:
      self.selected_index -= 1 
    
  def show(self):
    self.stdscr.clear()
    for i, item in enumerate(self.menu):
      if self.selected_index == i:
        self.stdscr.attron(curses.color_pair(1))
        self.stdscr.addstr(i, 0, str(item))
        self.stdscr.attroff(curses.color_pair(1))
      else:
        self.stdscr.addstr(i, 0, str(item))

    self.stdscr.refresh()

  def get_menu_length(self): return len(self.menu)
