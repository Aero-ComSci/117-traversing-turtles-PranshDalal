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



    def __str__(self):
        return "\n".join([f"Turtle Shape: {t.shape()}, Color: {t.color()[0]}" for t in self.turtles])


turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

drawer = TurtleThing(turtle_shapes, turtle_colors)
print(drawer)

drawer.draw_spiral_outward()

wn = trtl.Screen()
wn.mainloop()
