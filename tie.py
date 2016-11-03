from Tkinter import *
import math, time, random, sys

def spin(event):
    count = -0.5
    delay = 0.01
    random.shuffle(colours)
    while (count < 30):
        cv.delete("all")
        count += 0.5
        cv.create_oval(200, 200, 600, 600, outline='black', width='10')
        cv.create_text(380,100,fill="blue",font="Calibri 50 bold",
            text="THE WHEEL OF PYTHON")
        cv.create_polygon(375,150,400,200,425,150, fill='black')
        if count == 15:
            delay = delay * 2
        if count == 20:
            delay = delay * 2
        if count == 25:
            delay = delay * 2
        time.sleep(delay)
        for i in range (0, 2):
            add = -1.57
            while (add < 1.57):
                angle = math.pi*(i * 180)/180 + count + add
                x = 400 + 200 * math.cos(angle)
                y = 400 + 200 * math.sin(angle)
                cv.create_line(400, 400, x,y, fill=colours[i], width='5')
                add += 0.01
        cv.create_oval(380, 380, 420, 420, fill='black', width='5')
        cv.update()
        cv.create_text(395,700,fill="blue",font="Calibri 40 bold",
            text="Press Enter to Spin")
        cv.bind_all('<Return>', spin)

root = Tk()
mainframe = Frame(root) #create a mainframe frame

# gloabl vars
global w, h, cv

w = 800
h = 800
cv = Canvas(root, width = w, height = h, bg = "white")

cv.pack()
quitPressed = False
colours = ["blue", "red"]
cv.create_text(380,100,fill="blue",font="Calibri 50 bold",
    text="THE WHEEL OF PYTHON")
cv.create_text(395,700,fill="blue",font="Calibri 40 bold",
    text="Press Enter to Spin")
cv.create_polygon(375,150,400,200,425,150, fill='black')
cv.create_oval(200, 200, 600, 600, outline='black', width='10')

count = -0.5
for i in range (0, 2):
    add = -1.57
    while (add < 1.57):
        angle = math.pi*(i * 180)/180 + count + add
        x = 400 + 200 * math.cos(angle)
        y = 400 + 200 * math.sin(angle)
        cv.create_line(400, 400, x,y, fill=colours[i], width='5')
        add += 0.01
cv.create_oval(380, 380, 420, 420, fill='black', width='5')
cv.update()
cv.bind_all('<Return>', spin)




root.mainloop()
