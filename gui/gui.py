import tkinter as tk


root = tk.Tk()
root.geometry("800x600")
root.title("My first GUI in Python")


label = tk.Label(root, text="Hello World", font=("Arial", 24))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=10, width=30, font=("Arial", 12))
textbox.pack(padx=20, pady=20)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=("Arial", 12))
btn2 = tk.Button(buttonframe, text="2", font=("Arial", 12))
btn3 = tk.Button(buttonframe, text="3", font=("Arial", 12))
btn4 = tk.Button(buttonframe, text="4", font=("Arial", 12))
btn5 = tk.Button(buttonframe, text="5", font=("Arial", 12))
btn6 = tk.Button(buttonframe, text="6", font=("Arial", 12))

btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")
print("Starting GUI...")
root.mainloop()
