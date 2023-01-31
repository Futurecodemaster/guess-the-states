import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
all_states = data['state'].tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput("States Correct", f"{len(guessed_states)}/50 What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pd.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(*data[data['state'] == answer_state][['x', 'y']].iloc[0].tolist())
        t.write(answer_state)
