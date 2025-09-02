import turtle as t
import random

print("welcome to 4x4 sliding game")
        

sk = t.Turtle()
sk.hideturtle()
sk.speed(0.5)
sk.pensize(5)
sk.pu()
sk.goto(400,400)
sk.pd()
sk.write("4x4 Sliding Number Game" , align = "center",font = ("arial", 50 , "bold"))

wn = t.Screen()
wn.tracer(0)
wn.bgcolor("light green")

   

grid = [
    ["A1","A2","A3","A4"],
    ["B1","B2","B3","B4"],
    ["C1","C2","C3","C4"],
    ["D1","D2","D3","D4"]
]


def make_set(x1, x2, y1, y2):
    return {(x,y) for x in range(x1, x2) for y in range(y1, y2)}

dict_cells = {
    "A1": make_set(-200,-100,100,200),
    "A2": make_set(-100,0,100,200),
    "A3": make_set(0,100,100,200),
    "A4": make_set(100,200,100,200),
    "B1": make_set(-200,-100,0,100),
    "B2": make_set(-100,0,0,100),
    "B3": make_set(0,100,0,100),
    "B4": make_set(100,200,0,100),
    "C1": make_set(-200,-100,-100,0),
    "C2": make_set(-100,0,-100,0),
    "C3": make_set(0,100,-100,0),
    "C4": make_set(100,200,-100,0),
    "D1": make_set(-200,-100,-200,-100),
    "D2": make_set(-100,0,-200,-100),
    "D3": make_set(0,100,-200,-100),
    "D4": make_set(100,200,-200,-100)
}


def get_siders(box):
    for i in range(0,4):
        for j in range(0,4):
            if grid[i][j] == box:
                siders = []
                if i > 0: siders.append(grid[i-1][j])
                if i < 3: siders.append(grid[i+1][j])
                if j > 0: siders.append(grid[i][j-1])
                if j < 3: siders.append(grid[i][j+1])
                return siders
    return []


empty_cell = "D4"
numbers = list(range(1,16))
random.shuffle(numbers)

cell_values = {}
all_cells = [c for row in grid for c in row]
for c in all_cells:
    if c == empty_cell:
        cell_values[c] = None
    else:
        cell_values[c] = numbers.pop()

def draw_cell(box):
    coords = list(dict_cells[box])
    low_x = min(x for x,y in coords)
    high_x = max(x for x,y in coords)
    low_y = min(y for x,y in coords)
    high_y = max(y for x,y in coords)
    cx = (low_x + high_x)//2
    cy = (low_y + high_y)//2

    
    sk.penup()
    sk.goto(low_x, low_y)
    sk.color("light green")
    sk.begin_fill()
    for _ in range(0,4):
        sk.forward(high_x-low_x)
        sk.left(90)
    sk.end_fill()
    
    sk.color("black")
    sk.pendown()
    for _ in range(0,4):
        sk.forward(high_x-low_x)
        sk.left(90)
    sk.penup()

    
    if cell_values[box] is not None:
        sk.goto(cx, cy-50)
        sk.color("blue")
        sk.write(cell_values[box], align="center", font=("arial", 50, "bold"))

def draw_cells():
    for c in all_cells:
        draw_cell(c)

e_cell = "D4"
numb = list(range(1,16))
numb.reverse()

fcell_values = {}
all_cells = [c for row in grid for c in row]
for c in all_cells:
    if c == e_cell:
        fcell_values[c] = None
    else:
        fcell_values[c] = numb.pop()

def check_win():
    if cell_values == fcell_values:
        sk.goto(0, -300)
        sk.color("red")
        sk.write(" You Win! ", align="center", font=("arial", 50, "bold"))
        wn.onclick(None)  


def slide_cells(box):
    global empty_cell
    if empty_cell in get_siders(box):  
        cell_values[empty_cell], cell_values[box] = cell_values[box], None
        draw_cell(empty_cell)
        draw_cell(box)
        empty_cell = box
        check_win()

def click_opt(x, y):
    n = (x,y)
    b = None
    for key, values in dict_cells.items():
        if n in values:
            b = key
            break
    if b and cell_values[b] is not None:
        slide_cells(b)






draw_cells()
wn.onclick(click_opt)
wn.mainloop()












































































    
    

        

        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





















