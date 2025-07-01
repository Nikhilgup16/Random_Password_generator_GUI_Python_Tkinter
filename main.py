import random
import string
from tkinter import *
window = Tk()
window.geometry("600x250")
window.title("Random Password Generator")

def createPass():
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_character = "~!@#$%^&*()_-+={[}]:;|?/>.<,"

    all_character = uppercase + lowercase + digits + special_character

    password = "".join(random.choices(all_character,k=10))
    passwordLabel.config(text=password)

header = Label(
    window,
    text="Random Password Generator",
    font="Arial 30 bold",
    background="green",
    foreground="yellow",
)
header.pack(fill=X)

Label(
    window,
    text="Create a password by clicking on create button !!!",
).pack(fill=X)

passwordLabel = Label(
    window,
    text="Password",
    width=20,
    height=2,
    font=("Arial", 20, "bold"),
    bg="white",
    fg="black",
)
passwordLabel.pack(pady=20)

createBtn = Button(
    window,
    text="Create",
    font="Arial 15 bold",
    command=createPass,
)
createBtn.pack(pady=20)

window.mainloop()