from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # self.tail = self.segments[len(self.segments)-1]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_length(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        # new_x = self.tail.xcor()
        # new_y = self.tail.ycor()
        # direction =  self.tail.heading()
        # if direction == RIGHT:
        #     new_segment.goto(new_x - 20,new_y)
        # elif direction == UP:
        #     new_segment.goto(new_x , new_y - 20)
        # elif direction == LEFT:
        #     new_segment.goto(new_x + 20, new_y )
        # else:
        #     new_segment.goto(new_x, new_y + 20)
        # self.tail = new_segment
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
