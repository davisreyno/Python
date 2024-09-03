import turtle
import pandas

# Creates screen with blank states image
screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    # Pop up block for user input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    print(answer_state)

    # If answer state is one of the states in all the states of the 50 states
    # If user is correct, create a turtle to write the name of the state at respective coor
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

screen.exitclick()

# # Keeps screen open
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
