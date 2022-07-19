from tkinter import *
import pandas
import time
import random

BACKGROUND_COLOR = "#B1DDC6"
TIME_ANS = 3
timer = None
count = TIME_ANS
current_Card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.cvs")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# ---------------------------- Card Generator ------------------------------- #
def newCard():
    global current_Card
    global flip_timer
    window.after_cancel(flip_timer)
    current_Card = random.choice(to_learn)
    canvas.itemconfig(text1, text="French", fill="black")
    canvas.itemconfig(text2, text=current_Card["French"], fill="black")
    canvas.itemconfig(canvasBg, image=imgFre)
    flip_timer = window.after(3000, flipCard)

# ---------------------------- Time SETUP ------------------------------- #

def flipCard():
    canvas.itemconfig(text1, text="English" ,fill="white")
    canvas.itemconfig(text2, text=current_Card["English"],fill="white")
    canvas.itemconfig(canvasBg, image=imgEng)

def is_known():
    to_learn.remove(current_Card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.cvs",index=False)
    print(len(to_learn))
    newCard()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flipCard)

# Main Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
imgFre = PhotoImage(file="files/card_front.png")
imgEng = PhotoImage(file="files/card_back.png")
canvasBg = canvas.create_image(400, 263, image=imgFre)
canvas.grid(column=0, row=0, columnspan=2)

text1 = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
text2 = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

# Wrong Button
wrong_image = PhotoImage(file="files/wrong.png")
buttonW = Button(image=wrong_image, highlightthickness=0, command=newCard)
buttonW.grid(column=0, row=1)

# Rigth Button
rigth_image = PhotoImage(file="files/right.png")
buttonR = Button(image=rigth_image, highlightthickness=0, command=is_known)
buttonR.grid(column=1, row=1)

newCard()

window.mainloop()
