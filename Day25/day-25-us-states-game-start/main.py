import pandas
import turtle

#crearting screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
#creating turtle with the picture as the shape
turtle.shape(image)

correct_guess = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="Name a State")
    answer_state = answer_state.title()

    data = pandas.read_csv("50_states.csv")
    if (data["state"] == answer_state).any() and answer_state not in correct_guess:
        correct_guess.append(answer_state)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        x = data.loc[data['state'] == answer_state, 'x'].values[0]
        y = data.loc[data['state'] == answer_state, 'y'].values[0]
        state.setpos(x, y)
        state.write(answer_state, align="center", font=("Arial", 11, "normal"))

    if len(correct_guess) == 50:
        game_over = turtle.Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.setpos(0, 0)
        game_over.write("You Win!", align="center", font=("Arial", 22, "normal"))
        game_is_on = False







screen.exitonclick()