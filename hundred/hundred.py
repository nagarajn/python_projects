import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from config_frame import ConfigFrame
from center_frame import CenterFrame
from status_frame import StatusFrame


# The hundred is a resolution tracker app.
# If the user wants to track their resolution they can use this app.
# The app uses hundred.json file in the same directory. It creates this json if it doesn't exist.
# The json file is used to store the user information and as a database to keep track
# of their resolutions.
# Each time the app starts the hundred.json is loaded, incase it is not available, create it.

# There will be a top_frame that contains three frames: left_frame, center_frame[] and right_frame
# left_frame will contain
# a dropdown
#   The resolution chosen in the dropdown is the center_frame element that gets displayed,
#   rest of them are hidden.
# a + button so that we can add new target resolutions
# a - button so that we can remove target resolutions
# a ? button to display help
# Any change should be saved to json file automatically.

# Each element of center_frame array will contain 100 single_frame elements.
# They are arranged in a 10x10 grid.
# On clicking a single_frame, the user will be presented with an option to pick a date of completion.
# If the user picks a date, the resolution will be marked as completed.
# If the user doesn't pick a date, the resolution will be marked as not completed.
# Any change should be saved to json file automatically.
# The user will also have the option of clearing that single_frame if required.
# If the chosen date is later than what has been present in one of the earlier set single_frame
# ,then it is ok, else don't allow it.

# right_frame will contain a summary of the resolution
# how many days are done, how many are not done, how many are left to do.

# Ok, main code starts here


# top_frame
class TopFrame:
    def __init__(self, window):
        self.top_frame = ttk.Frame(window)
        self.top_frame.pack(side="left", expand=True, fill="both")


if __name__ == "__main__":
    # window
    window = ttk.Window(themename="darkly")
    window.title("100")
    window.geometry("800x600")
    top_frame = TopFrame(window)
    top_frame.top_frame.columnconfigure(0, weight=2, uniform="a")  # 200px
    top_frame.top_frame.columnconfigure(1, weight=6, uniform="a")  # 600px
    top_frame.top_frame.rowconfigure((0, 1), weight=1, uniform="a")
    # left_frame
    left_frame = ConfigFrame(top_frame.top_frame)
    left_frame.config_frame.grid(row=0, column=0, sticky="news")
    # center_frame
    center_frame = CenterFrame(top_frame.top_frame)
    center_frame.center_frame.grid(row=0, column=1, sticky="news", rowspan=2)
    # right_frame
    status_frame = StatusFrame(top_frame.top_frame)
    status_frame.status_frame.grid(row=1, column=0, sticky="news")
    window.mainloop()
