from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []

for q in question_data[0]["results"]:
    # print(q["question"])
    # print(q["correct_answer"])
    new = Question(q["question"], q["correct_answer"])
    question_bank.append(new)

game = QuizzBrain(question_bank)

while game.still_has_questions():
    game.getQuestion()
