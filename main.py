import turtle as trtl
import random

class TurtleThing:
    def __init__(self, shapes, colors):
        
        self.turtles = [trtl.Turtle(shape=s) for s in shapes]
        self.colors = colors

        for turtle in self.turtles:
            turtle.color(random.choice(self.colors))
        
        self.x = 0
        self.y = 0

    def move_turtles(self):
        for i, turtle in enumerate(self.turtles):
            turtle.goto(self.x + (i * 50), self.y + (i * 50))
            turtle.right(45)
            turtle.forward(50)
            if i == 4:
                break

    def draw_rando_shape(self):
        direction = 50
        for i, turtle in enumerate(self.turtles):
            turtle.penup()
            turtle.setheading(direction)
            turtle.goto(self.x, self.y)
            turtle.pendown()
            turtle.forward(100)
            direction += 45
            self.x, self.y = turtle.pos()

    def draw_spiral_outward(self):
        direction = 50
        step_increment = 20  
        forward_distance = 100  
        for i, turtle in enumerate(self.turtles):
            turtle.penup()
            turtle.setheading(direction)
            turtle.goto(self.x, self.y)
            turtle.pendown()
            turtle.forward(forward_distance)
            forward_distance += step_increment
            direction += 45
            self.x, self.y = turtle.pos()
            if i == 15:
                break
  
    def draw_with_lengths(self, lengths):
        for i, turtle in enumerate(self.turtles):
            turtle.penup()
            turtle.goto(self.x, self.y)
            turtle.pendown()
            turtle.forward(lengths[i % len(lengths)])
            if i == 10:
                break

    def draw_with_headings(self, headings):
        for i, turtle in enumerate(self.turtles):
            turtle.penup()
            turtle.goto(self.x, self.y)
            turtle.pendown()
            turtle.setheading(headings[i % len(headings)])
            turtle.forward(100)
            if i == 10:
                break

    def draw_with_pen_sizes(self, pen_sizes):
        for i, turtle in enumerate(self.turtles):
            turtle.penup()
            turtle.goto(self.x, self.y)
            turtle.pendown()
            turtle.pensize(pen_sizes[i % len(pen_sizes)])
            turtle.forward(100)
            if i == 10:
                break



    def __str__(self):
        return "\n".join([f"Turtle Shape: {t.shape()}, Color: {t.color()[0]}" for t in self.turtles])


turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

drawer = TurtleThing(turtle_shapes, turtle_colors)
print(drawer)

wn = trtl.Screen()
#drawer.move_turtles()
#drawer.draw_rando_shape()
#drawer.draw_spiral_outward()
#drawer.draw_with_lengths([50, 100, 150, 200, 250, 300])
#drawer.draw_with_headings([0, 90, 180, 270])
#drawer.draw_with_pen_sizes([1, 2, 3, 4, 5, 6])


wn.mainloop()
