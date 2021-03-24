import random
import pyperclip
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_field.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    if web_entry.get() == "" or password_field.get() == "":
        messagebox.askokcancel(title="Oops!", message="Please don't leave any fields empty!")
    else:
        with open("data.txt", "a") as file:
            file.write(f"{web_entry.get()} | {user_entry.get()} | {password_field.get()} \n")
        web_entry.delete(0, 'end')
        # user_entry.delete(0, 'end')
        password_field.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website:", font=("arial", 12))
website.grid(column=0, row=1)


web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

username = Label(text="Email/Username:", font=("arial", 12))
username.grid(column=0, row=2)

user_entry = Entry(width=35)
user_entry.insert(0, string="test@email.com")
user_entry.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:", font=("arial", 12))
password.grid(column=0, row=3)

password_field = Entry(width=21)
password_field.grid(column=1, row=3)

gpassword = Button(text="Generate Password", command=generate_password)
gpassword.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()