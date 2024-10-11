import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US State Guessing Game")
image = "Day-25/us-states-game/blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)

data_states = pd.read_csv("Day-25/us-states-game/50_states.csv")
all_states = data_states.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_state)}/50 Guess the state.", prompt= "What's the state name guess is:")

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = data_states[data_states.state == answer_state]
        t.goto(state_row.x.item(), state_row.y.item())
        t.write(state_row.state.item())

    if answer_state == "end":
        states_to_learn = [state for state in all_states if state not in guessed_state] 

        game_outcome_analysis = pd.DataFrame(states_to_learn)
        print(game_outcome_analysis)

        game_outcome_analysis.to_csv("Day-25/us-states-game/Game_Outcome_Analysis.csv")
        break

screen.exitonclick()