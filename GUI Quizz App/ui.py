from tkinter import  *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self,quizzbrain : QuizBrain):
        self.quiz = quizzbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        #Score Label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1,pady=10)
        #White background
        self.canvasBg = self.canvas.create_image(150, 125)
        self.canvas.grid(column=0, row=1, columnspan=2)
        #Question Text
        self.question_text =  self.canvas.create_text(150, 125,
                                text="Some Question Text",
                                width=280,
                                fill=THEME_COLOR,
                                font=("Arial", 20, "italic"))

        # Wrong Button
        wrong_image = PhotoImage(file="images/false.png")
        self.buttonW = Button(image=wrong_image, highlightthickness=0,command=self.wrong)
        self.buttonW.grid(column=0, row=2, pady=20)
        # Rigth Button
        rigth_image = PhotoImage(file="images/true.png")
        self.buttonR = Button(image=rigth_image, highlightthickness=0,command=self.right)
        self.buttonR.grid(column=1, row=2,pady=20)
        # Main Loop
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="End of the test")
            self.buttonR.config(state="disabled")
            self.buttonW.config(state="disabled")

    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.giveFeedback(is_right)


    def right(self):
        is_right = self.quiz.check_answer("True")
        self.giveFeedback(is_right)


    def giveFeedback(self, is_rigth):
        if is_rigth:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
