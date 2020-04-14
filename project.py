

from tkinter import *
import random

root = Tk()
w = Canvas(root, width=1000, height=1000,bg="white")

global pawnr1
global pawng1
global pawny1
global pawnb1

#for main ludo board
w.create_rectangle(50,50,650,650,width=3)


#for red 
w.create_rectangle(410,50,650,290,fill="red",width=3)
w.create_rectangle(450,90,610,250,fill="white",width=3)
w.create_rectangle(490,130,570,210,fill="red",width=3)
w.create_line(530,130,530,210)
w.create_line(490,170,570,170)

#for red pawns
pawnr1=w.create_oval(490,130,530,170,fill="red",width=2)
w.create_oval(530,130,570,170,fill="red",width=2)
w.create_oval(490,170,530,210,fill="red",width=2)
w.create_oval(530,170,570,210,fill="red",width=2)


#for blue
w.create_rectangle(50,50,290,290,fill="blue",width=3)
w.create_rectangle(90,90,250,250,fill="white",width=3)
w.create_rectangle(130,130,210,210,fill="blue",width=3)
w.create_line(170,130,170,210)
w.create_line(130,170,210,170)

#for blue pawns
pawnb1=w.create_oval(130,130,170,170,fill="blue",width=2)
w.create_oval(170,130,210,170,fill="blue",width=2)
w.create_oval(130,170,170,210,fill="blue",width=2)
w.create_oval(170,170,210,210,fill="blue",width=2)


#for yellow 
w.create_rectangle(50,410,290,650,fill="yellow",width=3)
w.create_rectangle(90,450,250,610,fill="white",width=3)
w.create_rectangle(130,490,210,570,fill="yellow",width=3)
w.create_line(170,490,170,570)
w.create_line(130,530,210,530)

#for yellow pawns
pawny1=w.create_oval(130,490,170,530,fill="yellow",width=2)
w.create_oval(170,490,210,530,fill="yellow",width=2)
w.create_oval(130,530,170,570,fill="yellow",width=2)
w.create_oval(170,530,210,570,fill="yellow",width=2)


#for green 
w.create_rectangle(410,410,650,650,fill="green",width=3)
w.create_rectangle(450,450,610,610,fill="white",width=3)
w.create_rectangle(490,490,570,570,fill="green",width=3)
w.create_line(530,490,530,570)
w.create_line(490,530,570,530)

#for green pawns
pawng1=w.create_oval(490,490,530,530,fill="green",width=2)
w.create_oval(530,490,570,530,fill="green",width=2)
w.create_oval(490,530,530,570,fill="green",width=2)
w.create_oval(530,530,570,570,fill="green",width=2)




#for upper middle rectangle
for i in range(50,290,40):
	w.create_rectangle(290,i,330,i+40)

for i in range(50,290,40):
	w.create_rectangle(330,i,370,i+40,fill="red",width=2)

for i in range(50,290,40):
	w.create_rectangle(370,i,410,i+40)

#for colouring start rectangle
w.create_rectangle(370,50,410,90,fill="red",width=2)




#for left side rectangle
for i in range(50,290,40):
	w.create_rectangle(i,290,i+40,330)

for i in range(50,290,40):
	w.create_rectangle(i,330,i+40,370,fill="blue",width=2)

for i in range(50,290,40):
	w.create_rectangle(i,370,i+40,410)

#for colouring start rectangle
w.create_rectangle(50,290,90,330,fill="blue",width=2)	




#for lower middle rectangle
for i in range(410,650,40):
	w.create_rectangle(290,i,330,i+40)


for i in range(410,650,40):
	w.create_rectangle(330,i,370,i+40,fill="yellow",width=2)

for i in range(410,650,40):
	w.create_rectangle(370,i,410,i+40)

#for colouring start rectangle
w.create_rectangle(290,610,330,650,fill="yellow",width=2)	




#for right side rectangle
for i in range(410,650,40):
	w.create_rectangle(i,290,i+40,330)

for i in range(410,650,40):
	w.create_rectangle(i,330,i+40,370,fill="green",width=2)

for i in range(410,650,40):
	w.create_rectangle(i,370,i+40,410)

#for colouring start rectangle
w.create_rectangle(610,370,650,410,fill="green",width=2)	




#for home square
w.create_polygon(290,290,350,350,410,290,fill="red")
w.create_polygon(290,290,350,350,290,410,fill="blue")
w.create_polygon(290,410,350,350,410,410,fill="yellow")
w.create_polygon(410,410,350,350,410,290,fill="green")
w.create_rectangle(290,290,410,410,width=2)
w.create_line(290,290,410,410,width=2)
w.create_line(290,410,410,290,width=2)





l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []
l9 = []
l10 = []
l11 = []
l12 = []

dict1 = {}
dict_red = {}
dict_green = {}
dict_yellow = {}
dict_blue = {}

dict1 = {"red":[330,50,370,90], "green":[610,330,650,370], "yellow":[330,610,370,650], "blue":[50,330,90,370]}                  
#order is red, green, yellow, blue
dict_red = {"red1":[300,290,325,315],"red2":[325,290,350,315],"red3":[350,290,375,315],"red4":[375,290,325,400]}
dict_green = {"green1":[410,300,385,325],"green2":[410,325,385,350],"green3":[410,350,385,375],"green4":[410,375,385,400]}
dict_yellow = {"yellow1":[300,385,325,410],"yellow2":[325,385,350,410],"yellow3":[350,385,375,410],"yellow4":[375,385,400,410]}
dict_blue = {"blue1":[290,300,315,325],"blue2":[290,325,315,350],"blue3":[290,350,315,375],"blue4":[290,375,315,400]}


#Path of 1
for i in range(50,290,40):
    l1.append([370,i,410,i+40])

#Path of 2
for i in range(410,650,40):
    l2.append([i,290,i+40,330])

#Path of 3
for i in range(650,410,-40):
    l3.append([i,370,i-40,410])

#Path of 4
for i in range(410,650,40):
    l4.append([370,i,410,i+40])

#Path of 5
for i in range(650,410,-40):
    l5.append([290,i,330,i-40])

#Path of 6
for i in range(290,50,-40):
    l6.append([i,370,i-40,410])

#Path of 7
for i in range(50,290,40):
    l7.append([i,290,i+40,330])

#Path of 8
for i in range(290,50,-40):
    l8.append([290,i,330,i-40])

#Path of 9
for i in range(50,290,40):
    l9.append([330,i,370,i+40])

#Path of 10
for i in range(650,410,-40):
    l10.append([i,330,i-40,370])

#Path of 11
for i in range(650,410,-40):
    l11.append([330,i,370,i-40])

#Path of 12
for i in range(50,290,40):
    l12.append([i,330,i+40,370])


list_red = []
list_green = []
list_yellow = []
list_blue = []
lr = []
lg = []
ly = []
lb = []

list_red = l1 + l2 + [dict1.get("green")] + l3 + l4 + [dict1.get("yellow")] + l5 + l6 + [dict1.get("blue")] + l7 + l8 + l9 + [dict_red.get("red2")]
list_green = l3 + l4 + [dict1.get("yellow")] + l5 + l6 + [dict1.get("blue")] + l7 + l8 + [dict1.get("red")] + l1 + l2 + l10 + [dict_green.get("green2")] 
list_yellow = l5 + l6 + [dict1.get("blue")] + l7 + l8 + [dict1.get("red")] + l1 + l2 + [dict1.get("green")]+ l3 + l4 + l11 + [dict_yellow.get("yellow2")]
list_blue = l7 + l8 + [dict1.get("red")] + l1 + l2 + [dict1.get("green")] + l3 + l4 + [dict1.get("yellow")] + l5 + l6 + l12 + [dict_blue.get("blue2")]


global list_name
def extract(list_name , n):
    a = len(list_name)

    try:
        if(n <= a):
            for i in range(0,n):
                store_list = list_name[i]
            del list_name[:n]
        else:
            store_list = list_name[0]
    except(Exception):
        print("Pawn reached home!!")
        store_list = list_name
    return store_list



def move_red(event):
    global lr
    global list_red
    global die
    lr = list_red
    die = random.randint(1,6)
    print("Number rolled for red is: ",die)
    global pawnr1
    w.delete(pawnr1)
    var_list = extract(lr,die)
    pawnr1 = w.create_oval(var_list[0],var_list[1],var_list[2],var_list[3],fill="red",width=2)

def move_green(event):
    global lg
    global list_green
    global die
    lg = list_green
    die = random.randint(1,6)
    print("Number rolled for green is: ",die)
    global pawng1
    w.delete(pawng1)
    var_list = extract(lg,die)
    pawng1 = w.create_oval(var_list[0],var_list[1],var_list[2],var_list[3],fill="green",width=2)

def move_yellow(event):
    global ly
    global list_yellow
    global die
    ly = list_yellow
    die = random.randint(1,6)
    print("Number rolled for yellow is: ",die)
    global pawny1
    w.delete(pawny1)
    var_list = extract(ly,die)
    pawny1 = w.create_oval(var_list[0],var_list[1],var_list[2],var_list[3],fill="yellow",width=2)

def move_blue(event):
    global lb
    global list_blue
    global die
    lb = list_blue
    die = random.randint(1,6)
    print("Number rolled for blue is: ",die)
    global pawnb1
    w.delete(pawnb1)
    var_list = extract(lb,die)
    pawnb1 = w.create_oval(var_list[0],var_list[1],var_list[2],var_list[3],fill="blue",width=2)



b1 = Button(root,text="Roll the die for red player")
b1.place(x=900,y=100)
b1.bind('<Button-1>', move_red)
    

b2 = Button(root,text="Roll the die for green player")
b2.place(x=900,y=200)
b2.bind('<Button-1>', move_green)


b3 = Button(root,text="Roll the die for yellow player")
b3.place(x=900,y=300)
b3.bind('<Button-1>', move_yellow)


b4 = Button(root,text="Roll the die for blue player")
b4.place(x=900,y=400)
b4.bind('<Button-1>', move_blue)

w.pack()
root.mainloop()
