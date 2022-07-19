import turtle
import pandas
from Name import Names


screen = turtle.Screen()
screen.title("US States Game")
image = ("blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_States = data.state.to_list()
guessed = []

while len(guessed) <50:
    a = screen.textinput(f"{len(guessed)}/50 Guess the states", "Whats another state's name?")
    answer_state = a.title()
    if answer_state == "Exit":
        missing_states = [state for state in all_States if state not in guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("New_data.csv")
        break
    if answer_state in all_States:
        guessed.append(answer_state)
        coorX = int(data[data.state == answer_state].x)
        coorY = int(data[data.state == answer_state].y)
        state = Names(answer_state,coorX,coorY)
