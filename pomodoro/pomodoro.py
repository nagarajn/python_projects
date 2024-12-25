import customtkinter as ctk
import tkinter as tk
from PIL import Image
import time
import os

"""
Create a pomodoro timer GUI app in python using customtkinter
It will have the following features:
- A "work" timer that counts down from 25 minutes to 0
- A "break" timer that counts down from 5 minutes to 0
- A reset button that resets everything to initial values
- A start button to start work timer
- There will be a background image to make the whole thing more appealing
- When a timer is running it will be highlighted. And the one that is not running should become dull
- Work timer and break timer should be side by side and not one on top of the other
- Work frame and break frame will contain a button that will contain the status of the timer by
  displaying a suitable image in the button.
"""
root = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Create the main window
root.title("Pomodoro Timer")
root.geometry("800x500")
# Create the main frame
frame = ctk.CTkFrame(master=root, fg_color="transparent")
frame.pack(fill="both", expand=True)

timer_frame = ctk.CTkFrame(master=frame)
timer_frame.pack(padx=20, pady=20, fill="both", expand=True)
# work_frame will contain work_label, work_timer and work_progressbar
work_frame = ctk.CTkFrame(master=timer_frame)
work_frame.pack(padx=20, pady=20, fill="both", expand=True, side="left")
work_frame.pack_propagate(False)
# Keep image ready for later use
# Create a CTkImage using done.png
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
done_image = ctk.CTkImage(dark_image=Image.open(os.path.join(image_path, "done.png")))

work_label = ctk.CTkLabel(
    master=work_frame, text="Work Timer", font=("Consolas", 20, "bold")
)
work_label.pack(padx=10, pady=20)

work_timer = ctk.CTkLabel(
    master=work_frame, text="25:00", font=("Consolas", 100, "bold")
)
work_timer.pack(padx=10, pady=20)

work_progressbar = ctk.CTkProgressBar(master=work_frame, orientation="horizontal")
work_progressbar.set(1.0)
work_progressbar.pack(padx=10, pady=20)

done_button = ctk.CTkButton(
    master=work_frame,
    text="Done",
    font=("Consolas", 20, "bold"),
    height=40,
    image=done_image,
    fg_color="transparent",
    bg_color="transparent",
    hover=False,
)
done_button.pack(padx=20, pady=20, side="left", fill="both", expand=True)
done_button.forget()

# break_frame will contain break_label, break_timer and break_progressbar
break_frame = ctk.CTkFrame(master=timer_frame)
break_frame.pack(padx=20, pady=20, fill="both", expand=True, side="right")
break_frame.pack_propagate(False)
break_label = ctk.CTkLabel(
    master=break_frame, text="Break Timer", font=("Consolas", 20, "bold")
)
break_label.pack(padx=10, pady=20)

break_timer = ctk.CTkLabel(
    master=break_frame, text="05:00", font=("Consolas", 100, "bold")
)
break_timer.pack(padx=10, pady=20)

break_progressbar = ctk.CTkProgressBar(
    master=break_frame, orientation="horizontal", progress_color="red"
)
break_progressbar.set(1.0)
break_progressbar.pack(padx=10, pady=20)

break_done_button = ctk.CTkButton(
    master=break_frame,
    text="Done",
    font=("Consolas", 20, "bold"),
    height=40,
    image=done_image,
    fg_color="transparent",
    bg_color="transparent",
    hover=False,
)
break_done_button.pack(padx=20, pady=20, side="left", fill="both", expand=True)
break_done_button.forget()
# Add reset and start buttons
start_button = ctk.CTkButton(
    master=frame,
    text="Start",
    font=("Consolas", 20, "bold"),
    command=lambda: start(),
    height=40,
)
start_button.pack(padx=20, pady=20, side="left", fill="both", expand=True)

reset_button = ctk.CTkButton(
    master=frame,
    text="Reset",
    font=("Consolas", 20, "bold"),
    fg_color="red",
    command=lambda: reset(),
)
reset_button.pack(padx=20, pady=20, side="right", fill="both", expand=True)


# Add reset and start methods
def start():
    """
    Starts the Pomodoro timer.
    Make the break_timer dull
    Make the work_timer highlighted
    Make the work_progressbar 0 and break_progressbar 0
    In a for loop start the work_timer for 25 minutes and break_timer for 5 minutes
    After work timer is done, put a done image in the work_label
    After break timer is done, put a done image in the break_label
    """
    break_timer.configure(text_color="black")
    work_timer.configure(text_color="white")
    for i in range(25 * 60, -1, -5):
        work_timer.configure(text=f"{int(i / 60):02d}:{i % 60:02d}")
        work_progressbar.set(i / (25 * 60))
        root.update()
        time.sleep(0.0001)
    done_button.tkraise()
    done_button.configure(text=f"25 mins done at {time.strftime("%H:%M:%S")}")
    done_button.pack(padx=20, pady=20, side="left", fill="both", expand=True)
    break_timer.configure(text_color="white")
    work_timer.configure(text_color="black")
    for i in range(5 * 60, -1, -1):
        break_timer.configure(text=f"{int(i / 60):02d}:{i % 60:02d}")
        break_progressbar.set(i / (5 * 60))
        root.update()
        time.sleep(0.001)
    break_done_button.tkraise()
    break_done_button.configure(text=f"5 mins done at {time.strftime("%H:%M:%S")}")
    break_done_button.pack(padx=20, pady=20, side="left", fill="both", expand=True)
    break_timer.configure(text_color="black")
    print("start")


def reset():
    """
    Resets the Pomodoro timer back to its initial state.
    """
    break_timer.configure(text_color="white")
    work_timer.configure(text_color="white")
    done_button.forget()
    break_done_button.forget()
    work_timer.configure(text="25:00")
    break_timer.configure(text="05:00")
    work_progressbar.set(1.0)
    break_progressbar.set(1.0)
    print("reset")


root.mainloop()
