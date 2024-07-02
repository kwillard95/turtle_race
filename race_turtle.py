import turtle as t
import random


X_AXIS_WINDOW_PADDING = 20
Y_AXIS_WINDOW_PADDING = 70

class RaceTurtle:
    def __init__(self, color, start_position):
        self.turtle = t.Turtle()
        self.color = color
        self.is_racing = False
        self.is_winner = False

        self.turtle.fillcolor(color)
        self.turtle.shape("turtle")
        self.turtle.penup()
        self.turtle.setx(start_position[0])
        self.turtle.sety(start_position[1])

    def is_at_finish_line(self, steps_forward, end_of_screen_pos):
        current_pos = self.turtle.pos()
        return current_pos[0] + steps_forward >= end_of_screen_pos

    def move_forward(self, end_of_screen_pos):
        steps_forward = random.randint(10,99)
        if self.is_at_finish_line(steps_forward, end_of_screen_pos):
            self.turtle.setx(end_of_screen_pos)
            self.is_racing = False
        else:
            self.turtle.forward(steps_forward)
            self.is_racing = True







