from tkinter import *

window = Tk()
window.title("Speed convertor")
window.minsize(width=100, height=200)
window.config(padx=100, pady=200)

def convert():
    new_speed = int(input.get()) * 1.60934
    converted_speed.config(text=f"{new_speed}")

input = Entry(width=10)
input.grid(column=1, row=0)

speedM = Label(text="Miles")
speedM.grid(column=2, row=0)

convert_text = Label(text="is equal to")
convert_text.grid(column=0, row=1)

converted_speed = Label(text="0")
converted_speed.grid(column=1, row=1)

speedKm = Label(text="Km")
speedKm.grid(column=2, row=1)

calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)

window.mainloop()