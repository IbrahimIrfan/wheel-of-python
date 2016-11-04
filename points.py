from Tkinter import *

teem1 = 0
teem2 = 0

def yes1(offset):
    global teem1
    global score1
    cv.delete(score1)
    teem1 += offset
    score1 = cv.create_text(100, 45, font=("Arial", 20), text=teem1)
    cv.update()

def yes2(offset):
    global teem2
    global score2
    cv.delete(score2)
    teem2 += offset
    score2 = cv.create_text(500, 45, font=("Arial", 20), text=teem2)
    cv.update()

root = Tk()
mainframe = Frame(root)
cv = Canvas(root, width = 700, height = 150, bg = "white")
cv.pack()

cv.create_text(100, 15, font=("Arial", 24), text="TEAM 1")
score1 = cv.create_text(100, 45, font=("Arial", 20), text=0)

cv.create_text(500, 15, font=("Arial", 24), text="TEAM 2")
score2 = cv.create_text(500, 45, font=("Arial", 20), text=0)

label1 = Label(mainframe, text="Team 1: ")

plusButton1 = Button(mainframe, text = "+", command = lambda: yes1(1))
minusButton1 = Button(mainframe, text = "-", command = lambda: yes1(-1))

label2 = Label(mainframe, text="Team 2: ")
plusButton2 = Button(mainframe, text = "+", command = lambda: yes2(1))
minusButton2 = Button(mainframe, text = "-", command = lambda: yes2(-1))

mainframe.grid()
cv.grid(row=1, column=1)

label1.grid(row=0, column=1, padx=0, pady=0)
plusButton1.grid(row=0, column=2, padx=0, pady=0)
minusButton1.grid(row=0, column=3, padx=0, pady=0)

label2.grid(row=1, column=1, padx=0, pady=0)
plusButton2.grid(row=1, column=2, padx=0, pady=0)
minusButton2.grid(row=1, column=3, padx=0, pady=10)

root.mainloop()
