import turtle
import pandas as pd

FONT = ('arial', 10, 'bold')

def normalize(name):
    """Convert the guess to Title case"""
    return name[0].upper() + name[1:].lower()


def write_on_map(name):
    info = data[data["state"] == name]
    x = int(info.x)
    y = int(info.y)
    tim.penup()
    tim.hideturtle()
    tim.goto(x, y)
    tim.write(name, font=FONT, align='center')


# def count_guess_number():
#     screen.title(f"{}/50 States Correct")


screen = turtle.Screen()
tim = turtle.Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
df = pd.DataFrame(data)
state_list = []
correct_guesses = []
for i in df["state"]:
    state_list.append(i)
game_on = True
count = 0
while game_on:
    answer_state = screen.textinput(title=f"{count}/50 State Correct", prompt="What's another state's name?")
    user_ans = normalize(answer_state)

    if user_ans == "Exit":
        learn = []
        # states to learn.csv
        for i in state_list:
            if i not in correct_guesses:
                learn.append(i)
        new_data = pd.DataFrame(learn)
        new_data.to_csv("need_learn.csv")
        game_on = False
    if user_ans in state_list:
        write_on_map(user_ans)
        count += 1
        correct_guesses.append(user_ans)





# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()   # keep the screen open

screen.exitonclick()
