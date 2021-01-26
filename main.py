from turtle import Turtle, Screen
import  random
# instances of object, e.g of objects
# each instance of an object can have different state
# timmy.color = green
# tommy.color = red
# timmy and tommy have different states w.r.t colour

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which Turtle Will Win The Race? Enter a color: ")
print(user_bet)

color = ["red", "pink", "yellow", "blue", "black", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle])
    new_turtle.goto(x=-230, y=y_positions[turtle])
    all_turtles.append(new_turtle)


if user_bet:
    hello_kitty = True


while hello_kitty:
    for turtle in all_turtles:
        if turtle.xcor() > +230:
            hello_kitty = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You Won {winning_colour} ")

            else:
                print("You Loose")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()