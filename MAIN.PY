import turtle as t

sk = t.Turtle()
sk.hideturtle()
sk.speed(0.5)
sk.pensize(5)
sk.penup()
sk.goto(-400,-400)
sk.pendown()

for i in range(0,4):
    sk.forward(800)
    sk.left(90)

for i in range(-200,400,200):
    sk.penup()
    sk.goto(-400,i)
    sk.pendown()
    sk.forward(800)

sk.left(90)

for i in range(-200,400,200):
    sk.penup()
    sk.goto(i,-400)
    sk.pendown()
    sk.forward(800)    

sk.penup()
sk.goto(-300,-400)
sk.pendown()    
sk.write(1 , font = ("Arial" , 100 , "bold"))

























    
t.done()    
