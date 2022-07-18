class QuizzBrain:  # Create a Class
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.correctAnswers = 0

    def checkAswer(self, userAnswer , correctAnswer):
        if userAnswer == correctAnswer:
            self.correctAnswers +=1
            print(f"You Got it Right.")
        else:
            print(f"You got it wrong.\nThe Rigth answer was {correctAnswer}")
        print(f"Score {self.correctAnswers}/{self.question_number}")

    def getQuestion(self):
        current = self.question_list[self.question_number]
        corrextAnswer = current.attribute
        self.question_number += 1
        userAns = input(f"Q{self.question_number}: {current.text} (True/False) ")
        self.checkAswer(userAns, corrextAnswer)

    def still_has_questions(self):
        total = len(self.question_list)
        if self.question_number < total:
            return True
        else:
            return False
