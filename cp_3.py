import turtle as t
import random

print("welcome to 4x4 sliding game")
k = input("press 'enter' to start : ")

if k=="enter":
        


    sk = t.Turtle()
    sk.hideturtle()
    sk.speed(0.5)
    sk.pensize(5)

    wn = t.Screen()
    wn.bgcolor("light green")

    sk.penup()
    sk.goto(-300,300)
    sk.pendown()
    sk.write("4x4 Sliding Game" , align = "left" , font = ("arial" , 60 , "bold"))

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
    
    s1 = set()
    for x in range(-200,-100):
        for y in range(100,200):
            k = (x,y)
            s1.add(k)
    s2 = set()
    for x in range(-100,0):
        for y in range(100,200):
            k = (x,y)
            s2.add(k)
    s3 = set()
    for x in range(0,100):
        for y in range(100,200):
            k = (x,y)
            s3.add(k)
    s4 = set()
    for x in range(100,200):
        for y in range(100,200):
            k = (x,y)
            s4.add(k)
    s5 = set()
    for x in range(-200,-100):
        for y in range(0,100):
            k = (x,y)
            s5.add(k)
    s6 = set()
    for x in range(-100,0):
        for y in range(0,100):
            k = (x,y)
            s6.add(k)
    s7 = set()
    for x in range(0,100):
        for y in range(0,100):
            k = (x,y)
            s7.add(k)
    s8 = set()
    for x in range(100,200):
        for y in range(0,100):
            k = (x,y)
            s8.add(k)
    s9 = set()
    for x in range(-200,-100):
        for y in range(-100,0):
            k = (x,y)
            s9.add(k)
    s10 = set()
    for x in range(-100,0):
        for y in range(-100,0):
            k = (x,y)
            s10.add(k)
    s11 = set()
    for x in range(0,100):
        for y in range(-100,0):
            k = (x,y)
            s11.add(k)
    s12 = set()
    for x in range(100,200):
        for y in range(-100,0):
            k = (x,y)
            s12.add(k)
    s13 = set()
    for x in range(-200,-100):
        for y in range(-200,-100):
            k = (x,y)
            s13.add(k)
    s14 = set()
    for x in range(-100,0):
        for y in range(-200,-100):
            k = (x,y)
            s14.add(k)
    s15 = set()
    for x in range(0,100):
        for y in range(-200,-100):
            k = (x,y)
            s15.add(k)
    s16 = set()
    for x in range(100,200):
        for y in range(-200,-100):
            k = (x,y)
            s16.add(k)

    
    dict = {
        "A1" : s1 ,
        "A2" : s2 , 
        "A3" : s3 , 
        "A4" : s4 ,
        "B1" : s5 ,
        "B2" : s6 , 
        "B3" : s7 ,
        "B4" : s8 ,
        "C1" : s9 , 
        "C2" : s10 ,
        "C3" : s11 ,
        "C4" : s12 , 
        "D1" : s13 ,
        "D2" : s14 ,
        "D3" : s15 , 
        "D4" : s16 
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    t.done()





















