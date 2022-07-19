import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generatePassword():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []
    password_list += [random.choice(letters) for n in range(nr_letters)]
    password_list += [random.choice(symbols) for n in range(nr_symbols)]
    password_list += [random.choice(numbers) for n in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)  # Joins the elements of a list
    entryPass.insert(0, password)
    print(f"Your password is: {password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_File():
    website = entryWebSite.get()
    website = website.lower()
    username = entryUsername.get()
    password = entryPass.get()
    new_Data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showwarning(title="Empty Fields", message="You cant leave empty fields")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Reading old Data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_Data, file, indent=4)
        else:
            # update Data
            data.update(new_Data)
            with open("data.json", mode="w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        entryWebSite.delete(0, END)
        entryPass.delete(0, END)
# ---------------------------- Get Password ------------------------------- #

def searchPassword():
    website = entryWebSite.get()
    username = entryUsername.get()
    if len(website) == 0:
        messagebox.showwarning(title="Empty Website", message="Fill the website field")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
            if website in data:
                p = data[website]["password"]
                messagebox.showinfo(title="Found", message=f"Password for {website} username {username} copied to clipboard")
                pyperclip.copy(p)
            else:
                messagebox.showwarning(title="Website Fail", message="The Website does not exist")

        except:
            messagebox.showwarning(title="File not Found", message="Does not exist any json file")



# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Password Mannager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Labels
WebSite = Label(text="Website", font=("Arial", 11))
WebSite.grid(column=0, row=1)

Email = Label(text="Username", font=("Arial", 11))
Email.grid(column=0, row=2)

Pass = Label(text="Password", font=("Arial", 11))
Pass.grid(column=0, row=3)

# Buttons
generate = Button(text="Generate", command=generatePassword)
generate.grid(column=2, row=3)

search = Button(text="Search", command=searchPassword)
search.grid(column=2, row=1)

addPass = Button(text="Add", width=35, command=write_File)
addPass.grid(column=1, row=4, columnspan=2)

# Entries
entryWebSite = Entry(width=25)
entryWebSite.focus()
entryWebSite.grid(column=1, row=1)

entryUsername = Entry(width=35)
entryUsername.insert(END, string="mura.ivan@hotmail.com")
entryUsername.grid(column=1, row=2, columnspan=2)

entryPass = Entry(width=25)
entryPass.insert(END, string="")
entryPass.grid(column=1, row=3)

window.mainloop()




