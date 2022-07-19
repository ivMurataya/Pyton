import math
from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def ResetTime():
    global reps
    reps = 0
    window.after_cancel( timer  )
    label1.config(text="Timer")
    label2.config(text="")
    canvas.itemconfig(timer_text, text="00:00")



# ---------------------------- TIMER MECHANISM ------------------------------- #
def StartTime():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_Sec = LONG_BREAK_MIN * 60

    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        count_down(work_sec)
        label1.config(text="Work Time", fg=RED, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 24, "bold"))
    elif reps == 1 or reps == 3 or reps == 5:
        count_down(short_break_sec)
        label1.config(text="Break Time", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 24, "bold"))
    elif reps == 7:
        count_down(long_break_Sec)
        label1.config(text="Long Break Time", fg=PINK, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 24, "bold"))
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        StartTime()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        label2.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro technique")
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000, )

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Labels
label1 = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=("Arial", 24, "bold"))
label1.grid(column=1, row=0)

# Button Start Time
button = Button(text="Start", command=StartTime)
button.grid(column=0, row=2)

# Button Reset Time
button = Button(text="Reset", command=ResetTime)
button.grid(column=2, row=2)

# Labels
label2 = Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0, font=("Arial", 24, "bold"))
label2.grid(column=1, row=3)

window.mainloop()
