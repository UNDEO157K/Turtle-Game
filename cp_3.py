import turtle as t
import random



sk = t.Turtle()
sk.hideturtle()
sk.speed(0.5)
sk.pensize(5)

wn = t.Screen()
wn.bgcolor("light green")


sk.penup()
sk.goto(-200,-200)
sk.pendown()

for i in range(0,4):
    sk.forward(400)
    sk.left(90)

for i in range(-100,200,100):
    sk.penup()
    sk.goto(-200,i)
    sk.pendown()
    sk.forward(400)

sk.left(90)

for j in range(-100,200,100):
    sk.penup()
    sk.goto(j,-200)
    sk.pendown()
    sk.forward(400)  

sk.penup()      

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] 

s=[]
for x in range(-150,250,100):
    for y in range(-200,200,100):
        s.append((x,y))
  
s.remove((150,-200))

for j in l:    
    k = random.choice(s)
    s.remove(k)
    sk.goto(k)
    sk.color("blue")
    sk.begin_fill()    
    sk.write(j,align = "center",font = ("arial", 50, "bold"))
    sk.end_fill()
    if(s==[]):
        break
m=[]
for x in range(-150,250,100):
    for y in range(-150,250,100):
        m.append((x,y))
  

m.remove((150,-150))

k1 = ((-200,200),(-200,100),(-100,200),(-100,100))
k2 = ((-100,200),(-100,100),(0,200),(0,100))
k3 = ((0,200),(0,100),(100,200),(100,100))
k4 = ((100,200),(100,100),(200,200),(200,100))
k5 = ((-200,100),(-200,0),(-100,100),(-100,0))
k6 = ((-100,100),(-100,0),(0,100),(0,0))
k7 = ((0,100),(0,0),(100,100),(100,0))
k8 = ((100,100),(100,0),(200,100),(200,0))
k9 = ((-200,0),(-200,-100),(-100,0),(-100,-100))
k10 = ((-200,0),(-200,-100),(-100,0),(-100,-100))
k11 = ((-200,0),(-200,-100),(-100,0),(-100,-100))
k12 = ((-200,0),(-200,-100),(-100,0),(-100,-100))
k13 = ((-200,-100),(-200,-200),(-100,-100),(-100,-200))
k14 = ((-100,-100),(-100,-200),(0,-100),(0,-200))
k15 = ((0,-100),(0,-200),(100,-100),(100,-200))
k16 = ((100,-100),(100,-200),(200,-100),(200,-200))


























t.done()






