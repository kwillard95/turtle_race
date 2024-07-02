from turtle import Screen
from race_turtle import RaceTurtle, X_AXIS_WINDOW_PADDING, Y_AXIS_WINDOW_PADDING

screen = Screen()

turtle_colors = ["red", "blue", "yellow", "green", "purple"]

turtles = []

users_bet = ""
winner = None


def set_turtles():
    screen_height = screen.window_height()
    screen_width = screen.window_width()
    position_increment = screen_height / 5
    start_x_position = ((screen_width / 2) - X_AXIS_WINDOW_PADDING) * -1
    start_y_position = (screen_height / 2) - Y_AXIS_WINDOW_PADDING

    for color in turtle_colors:
        start_position = (start_x_position, start_y_position)
        race_turtle = RaceTurtle(color=color, start_position=start_position)
        turtles.append(race_turtle)
        start_y_position -= position_increment


def start_race():
    global winner
    end_of_screen_pos = (screen.window_width() / 2) - X_AXIS_WINDOW_PADDING
    for turtle in turtles:
        turtle.is_racing = True
    while winner is None:
        for turtle in turtles:
            if not turtle.is_racing and not winner:
                turtle.is_winner = True
                winner = turtle
            else:
                turtle.move_forward(end_of_screen_pos)
    for turtle in turtles:
        turtle.turtle.setx(end_of_screen_pos)


def start_game():
    global users_bet
    global winner
    set_turtles()
    while users_bet not in turtle_colors:
        users_bet = screen.textinput("Bet on who is going to win the race!",
                                     f"Type one of the following colors to place your bet: {', '.join(turtle_colors)}")

    start_race()
    if winner is not None:
        if winner != users_bet:
            print(f"You lose! The winner was {winner.color}.")
        else:
            print(f"You win! {winner.color.title()} won the race!")


start_game()
screen.exitonclick()
