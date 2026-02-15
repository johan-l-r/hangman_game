import curses

class Popup: 
  def __init__(self, padding):
    self.padding = padding
    self.popup = None

  def show(self, message):  
    message_lines = message.split("\n")

    max_line_len = max(len(line) for line in message_lines)
    POPUP_WIDTH = max_line_len + (self.padding * 2)
    POPUP_HEIGHT = len(message_lines) + self.padding + 3  

    self.popup = curses.newwin(POPUP_HEIGHT, POPUP_WIDTH, 5, 5)
    self.popup.keypad(True)

    message_y_pos = (POPUP_HEIGHT - len(message_lines) - 2) // 2

    for i, line in enumerate(message_lines):
      line_x_pos = (POPUP_WIDTH - len(line)) // 2
      self.popup.addstr(message_y_pos + i, line_x_pos, line)

    button_text = "< OK >"
    button_y = POPUP_HEIGHT - 2
    button_x = (POPUP_WIDTH - len(button_text)) // 2
    self.popup.addstr(button_y, button_x, button_text, curses.A_REVERSE)

    self.popup.box()
    self.popup.refresh()

  def confirm(self):
    while True:
      key = self.popup.getch()

      if key in (curses.KEY_ENTER, 10, 13):
        self.popup.refresh()
        self.popup.clear()

        return True
      elif key == 27:
        self.popup.refresh()
        self.popup.clear()

        return False

