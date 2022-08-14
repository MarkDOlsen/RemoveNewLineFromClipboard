import tkinter as tk
import pyperclip


def strip_newlines():
    text = pyperclip.paste()  # pull text off clipboard
    text = " ".join([word for word in text.split()])  # strip newlines
    pyperclip.copy(text)  # put text back on clipboard

    text_box.insert(1.0, text)  # display the modified text


#! CREATE AND SET UP WINDOW OBJECT
root = tk.Tk()  # create the window object
canvas = tk.Canvas(root, width=600, height=200)  # resize window
canvas.grid(columnspan=3, rowspan=10)  # initialize grid in window
# set text of window title bar
root.title("Strip Newlines from Clipboard Text")
# remove icon from title bar of window
root.wm_attributes('-toolwindow', 'True')

#! INSTRUCTIONS
instructions_text = "Click the button to strip line breaks from text currently on the clipboard."
instructions = tk.Label(root, text=instructions_text, font=("Garamond", 14))
instructions.grid(columnspan=3, column=0, row=0)

note_text = "Modified text will be on clipboard and displayed below."
note = tk.Label(root, text=note_text, font=("Garamond", 11))
note.grid(columnspan=3, column=0, row=1)

#! BUTTON
strip_text = tk.StringVar()
strip_btn = tk.Button(root, textvariable=strip_text, command=lambda: strip_newlines(),
                      font=("Garamond", 14), bg="#306851", fg="white", height=1, width=15)

strip_text.set("Strip Newlines")  # button text
strip_btn.grid(column=1, row=3, padx=0, pady=10)  # create the button

#! OUTPUT BOX
text_box = tk.Text(root, height=10, width=70, padx=5, pady=5)
text_box.grid(column=1, row=8)
text_box.insert(1.0, "")

# add padding to bottom of window
canvas = tk.Canvas(root, width=600, height=25)
canvas.grid(columnspan=3)

#! INITIALIZE THE WINDOW OBJECT AND DISPLAY IT
root.mainloop()
