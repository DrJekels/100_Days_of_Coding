from tkinter import *

window = Tk()
window.title("My First tkinter GUI")
window.minsize(width=500, height=500)
window.config(padx=100, pady=200)

# Label
label = Label(text="I am a label.", font=("Arial", 24, "bold"))
label.config(text="New Text")
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

# Button
def butt_touch():
    print("I am pressed.")
    label.config(text=f"{input.get()}")

button = Button(text="Press me.", command=butt_touch)
button.grid(column=1, row=1)
button2 = Button(text="New Button")
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.insert(END, string="Some text to press.")
input.grid(column=3, row=2)

# Text
# text = Text(height=5, width=30)
# text.focus()
# text.insert(END, "Example of multi-line text entry.")
# print(text.get("1.0", END))
# text.pack()

# Spin box
# def spunbox(): print(spinbox.get())

# spinbox = Spinbox(from_=0, to=10, width=5, command=spunbox)
# spinbox.pack()

# Scale
# def scaled(value): print(value)

# scale = Scale(from_=0, to=100, command=scaled)
# scale.pack()

# Check button
# def checkbutts(): print(check_state.get())

# check_state = IntVar()
# checkbutton = Checkbutton(text="Is on?", variable=check_state, command=checkbutts)
# check_state.get()
# checkbutton.pack()

# Radio button
# def ham_radio(): print(radio_state.get())

# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Flavor 1", value=1, variable=radio_state, command=ham_radio)
# radiobutton2 = Radiobutton(text="Flavor 2", value=2, variable=radio_state, command=ham_radio)
# radiobutton1.pack()
# radiobutton2.pack()

# List box
# def listedbox(event): print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listedbox)
# listbox.pack()

window.mainloop()