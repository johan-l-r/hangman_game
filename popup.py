import curses 

class Popup: 
  def __init__(self, padding):
    self.padding = padding

  def show(self, message):  
    POPUP_WIDTH = len(message) + (self.padding * 2)

    message_lines = message.splitlines()

    POPUP_HEIGHT = len(message_lines) + self.padding

    popup = curses.newwin(POPUP_HEIGHT, POPUP_WIDTH, 5, 5)

    # center message vertically
    message_y_pos = len(message_lines) // 2

    for i, line in enumerate(message_lines):
      line_x_pos = (POPUP_WIDTH - len(line)) // 2
      popup.addstr(2, line_x_pos, line)

    popup.box()
    popup.getch()

  def confirm(self, event): pass

    
