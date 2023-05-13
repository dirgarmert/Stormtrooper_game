import time
import turtle
import random
bg_pics_list = ["bg.pic.gif", "bg.pic_2.gif","bg.pic_3.gif","bg.pic_4.gif","bg.pic_5.gif","bg.pic_6.gif" ]
x = random.choice(bg_pics_list)
# screen_turtle
kaplumbaga_screen = turtle.Screen()
kaplumbaga_screen.setup(width=729, height=387)
kaplumbaga_screen.title("Catch_The_Turtle")
kaplumbaga_screen.bgpic(x)
kaplumbaga_screen.update()
FONT = ("Arial", 10, "bold")
score = 0
gameover = False
grid_size = 8  # başka projelerde değiştirerek alan yaparsın
turtle_List = []
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
# koordinat vermek
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10, -20]


def setup_score_turtle():
    score_turtle.hideturtle()
    if x =="bg.pic_3.gif":
        score_turtle.color("white")

    else:
        score_turtle.color("white")
    score_turtle.penup()

    top_height = kaplumbaga_screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setpos(0, y)
    score_turtle.write(arg='Score: 0', move=False, align='center', font=FONT)





# kaplumbaga yapmak
def make_kaplumbaga(x, y):
    kaplumbaga = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += +1
        score_turtle.clear()
        score_turtle.write(arg="Score:{}".format(score), move=False, align="center", font=FONT)

    kaplumbaga.onclick(handle_click)
    kaplumbaga.penup()
    kaplumbaga.shape("circle")
    kaplumbaga.shapesize(1, 1)
    kaplumbaga.color("white")
    kaplumbaga.goto(x * grid_size, y * grid_size)
    turtle_List.append(kaplumbaga)


def setup_turtle_positions():
    for x in x_coordinates:
        for y in y_coordinates:
            make_kaplumbaga(x, y)


def hide_turtles():
    for kaplumbaga in turtle_List:
        kaplumbaga.hideturtle()


def show_turtles_randomly():
    if not gameover:
        hide_turtles()
        random.choice(turtle_List).showturtle()
        kaplumbaga_screen.ontimer(show_turtles_randomly, 500)


def countdown(time):
    global gameover
    countdown_turtle.hideturtle()
    countdown_turtle.color("red")
    countdown_turtle.penup()

    top_height = kaplumbaga_screen.window_height() / 2
    y = top_height * 0.9

    countdown_turtle.setpos(0, y - 30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time:{}".format(time), move=False, align="center", font=FONT)
        kaplumbaga_screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        gameover = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over! Try Again", move=False, align="center", font=FONT)


def start_game():
    global gameover
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtle_positions()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)
    kaplumbaga_screen.ontimer(lambda: countdown(30), 30)


start_game()
turtle.mainloop()
