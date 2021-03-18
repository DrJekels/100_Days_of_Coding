import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. Guessing Game")
screen.setup(width=725, height=491)
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

states = pandas.read_csv("50_states.csv")
state_list = states.state.to_list()
states_guessed = 0
correct_guesses = []

game_on = True
while game_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    if answer_state.capitalize() in state_list and answer_state.capitalize() not in correct_guesses:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state.capitalize())
        states_guessed += 1
        correct_guesses.append(answer_state.capitalize())

    if states_guessed == 50:
        print("You win!")
        game_on = False
    
    if answer_state == "quit":
        game_on = False

screen.exitonclick()