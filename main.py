import tkinter
import random
c = tkinter.Canvas(width = 400, height = 300)
c.pack()

def klik(event):
    global x, y, farba, circ, r
    r = 50      #circle diameter
    x, y = event.x, event.y     #clicked position
    farba = '#{:06x}'.format(random.randrange(256 ** 3))        #random  color picker
    circ = c.create_oval(x - r, y - r, x + r, y + r, fill=farba)         #print circle
    print(x, y, farba)      #check clicked coordinates, not important
    if r < 50:      #reset size after each circle
        r = 50
    shrink()

def shrink():
    global circ, x, y, r
    print(r)        #check if countdown runs correctly
    if r > 0:
        r -= 1      #diameter shrinking
        c.coords(circ, x-r, y-r, x+r, y+r)      #changing circle size
        c.after(100, shrink)        #timer, size 1pt smaller until size is 0

c.bind('<Button-1>', klik)
tkinter.mainloop()