import tkinter as tk

root = tk.Tk()
root.title('Somár')
root.geometry('403x576')
root.resizable(width='False', height='False')
c = tk.Canvas(master=root, width = 400, height = 500)
c.grid(row=0, column=1, sticky='NE')
frame1 = tk.Frame(master=root, width=399, height=70, bg='grey')
frame1.grid(row=1, column=1, sticky='N')
# window = tk.Canvas(master=root, width=screen_x-558, height=screen_y-50, bg='white')
# window.grid(row=0, column=1, sticky='N')
# frame1 = tk.Frame(master=root, width=558, height=screen_y-50, bg='grey')
# frame1.grid(row=0, column=0, sticky='N')
global T
T = tk.Entry(master=frame1, width=3, bg='Light grey', bd=3, justify='center', insertontime=0)
T.configure(font=("Courier", 32, 'bold'))
# T = Text(master=frame1, height=13, width=58, bg='Light grey', bd=3, padx=10, yscrollcommand=v.set)
# text_font = font(family="Helvetica", size=32)
T.place(x=302, y=6)
T.delete(0, tk.END)
T.insert(tk.END, '0')

# c.pack()

global r1, r2, r3, r4, r5, r6, r7, r8, r9, r10
global r1x, r1y, r2x, r2y, r3x, r3y, r4x, r4y, r5x, r5y, r6x, r6y, r7x, r7y, r8x, r8y, r9x, r9y, r10x, r10y, selected

r1x = 50
r1y = 100
r1 = c.create_rectangle(r1x-50, r1y-100, r1x+50, r1y+100, fill='red')

r2x = 200
r2y = 100
r2 = c.create_rectangle(r2x-100, r2y-100, r2x+100, r2y+100, fill='blue')

r3x = 350
r3y = 100
r3 = c.create_rectangle(r3x-50, r3y-100, r3x+50, r3y+100, fill='red')

r4x = 50
r4y = 300
r4 = c.create_rectangle(r4x-50, r4y-100, r4x+50, r4y+100, fill='red')

r5x = 200
r5y = 250
r5 = c.create_rectangle(r5x-100, r5y-50, r5x+100, r5y+50, fill='red')

r6x = 350
r6y = 300
r6 = c.create_rectangle(r6x-50, r6y-100, r6x+50, r6y+100, fill='red')

r7x = 150
r7y = 350
r7 = c.create_rectangle(r7x-50, r7y-50, r7x+50, r7y+50, fill='red')

r8x = 250
r8y = 350
r8 = c.create_rectangle(r8x-50, r8y-50, r8x+50, r8y+50, fill='red')

r9x = 50
r9y = 450
r9 = c.create_rectangle(r9x-50, r9y-50, r9x+50, r9y+50, fill='red')

r10x = 350
r10y = 450
r10 = c.create_rectangle(r10x-50, r10y-50, r10x+50, r10y+50, fill='red')

global turns
turns = 0
selected = False

def turncount():
    global turns, T
    turns = turns + 1
    T.delete(0, tk.END)
    T.insert(tk.END, turns)

def klik(event):
    global r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, select, turns
    global r1x, r1y, r2x, r2y, r3x, r3y, r4x, r4y, r5x, r5y, r6x, r6y, r7x, r7y, r8x, r8y, r9x, r9y, r10x, r10y, selected
    x, y = event.x, event.y     #clicked position
    item = c.find_closest(x, y)
    current_color = c.itemcget(item, 'fill')
    print(current_color)

    if selected == False:
        if r1x - 50 < x < r1x + 50 and r1y - 100 < y < r1y + 100:
            c.delete(r1)
            r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='yellow')
            select = 'r1'
            selected = True
        if r2x - 100 < x < r2x + 100 and r2y - 100 < y < r2y + 100:
            c.delete(r2)
            r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='yellow')
            select = 'r2'
            selected = True
        if r3x - 50 < x < r3x + 50 and r3y - 100 < y < r3y + 100:
            c.delete(r3)
            r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='yellow')
            select = 'r3'
            selected = True
        if r4x - 50 < x < r4x + 50 and r4y - 100 < y < r4y + 100:
            c.delete(r4)
            r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='yellow')
            select = 'r4'
            selected = True
        if r5x - 100 < x < r5x + 100 and r5y - 50 < y < r5y + 50:
            c.delete(r5)
            r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='yellow')
            select = 'r5'
            selected = True
        if r6x - 50 < x < r6x + 50 and r6y - 100 < y < r6y + 100:
            c.delete(r6)
            r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='yellow')
            select = 'r6'
            selected = True
        if r7x - 50 < x < r7x + 50 and r7y - 50 < y < r7y + 50:
            c.delete(r7)
            r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='yellow')
            select = 'r7'
            selected = True
        if r8x - 50 < x < r8x + 50 and r8y - 50 < y < r8y + 50:
            c.delete(r8)
            r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='yellow')
            select = 'r8'
            selected = True
        if r9x - 50 < x < r9x + 50 and r9y - 50 < y < r9y + 50:
            c.delete(r9)
            r9 = c.create_rectangle(r9x - 50, r9y - 50, r9x + 50, r9y + 50, fill='yellow')
            select = 'r9'
            selected = True
        if r10x - 50 < x < r10x + 50 and r10y - 50 < y < r10y + 50:
            c.delete(r10)
            r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='yellow')
            select = 'r10'
            selected = True

    elif selected == True:
        if select == 'r1':
            if r2x - 100 < x < r2x + 100 and r2y - 100 < y < r2y + 100:
                c.delete(r1)
                r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                selected = False
            elif r3x - 50 < x < r3x + 50 and r3y - 100 < y < r3y + 100:
                c.delete(r1)
                r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                selected = False
            elif r4x - 50 < x < r4x + 50 and r4y - 100 < y < r4y + 100:
                c.delete(r1)
                r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                selected = False
            elif r5x - 100 < x < r5x + 100 and r5y - 50 < y < r5y + 50:
                c.delete(r1)
                r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                selected = False
            elif r6x - 50 < x < r6x + 50 and r6y - 100 < y < r6y + 100:
                c.delete(r1)
                r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                selected = False
            elif r7x - 50 < x < r7x + 50 and r7y - 50 < y < r7y + 50:
                c.delete(r1)
                r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                selected = False
            elif r8x - 50 < x < r8x + 50 and r8y - 50 < y < r8y + 50:
                c.delete(r1)
                r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                selected = False
            elif r9x - 50 < x < r9x + 50 and r9y - 50 < y < r9y + 50:
                c.delete(r1)
                r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                selected = False
            elif r10x - 50 < x < r10x + 50 and r10y - 50 < y < r10y + 50:
                c.delete(r1)
                r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                selected = False
            else:
                if x < r1x - 50 and r1y - 100 < y < r1y + 100:
                    item = c.find_overlapping(r1x - 140, r1y - 90, r1x - 90, r1y + 90)
                    print(item)
                    if item == ():
                        c.delete(r1)
                        r1x = r1x - 100
                        r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                        selected = False
                        turncount()
                    else:
                        c.delete(r1)
                        r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                        selected = False
                elif x > r1x + 50 and r1y - 100 < y < r1y + 100:
                    item = c.find_overlapping(r1x + 60, r1y - 90, r1x + 140, r1y + 90)
                    print(item)
                    if item == ():
                        c.delete(r1)
                        r1x = r1x + 100
                        r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                        selected = False
                        turncount()
                    else:
                        c.delete(r1)
                        r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                        selected = False
                elif y < r1y - 100 and r1x - 50 < x < r1x + 50:
                    c.delete(r1)
                    r1y = r1y - 100
                    r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                    selected = False
                    turncount()
                elif y > r1y + 100 and r1x - 50 < x < r1x + 50:
                    c.delete(r1)
                    r1y = r1y + 100
                    r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                    selected = False
                    turncount()

        if select == 'r2':
            if r1x - 50 < x < r1x + 50 and r1y - 100 < y < r1y + 100:
                c.delete(r2)
                r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                selected = False
            elif r3x - 50 < x < r3x + 50 and r3y - 100 < y < r3y + 100:
                c.delete(r2)
                r2 = c.create_rectangle(r2x-100, r2y-100, r2x+100, r2y+100, fill='blue')
                selected = False
            elif r4x - 50 < x < r4x + 50 and r4y - 100 < y < r4y + 100:
                c.delete(r2)
                r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                selected = False
            elif r5x - 100 < x < r5x + 100 and r5y - 50 < y < r5y + 50:
                c.delete(r2)
                r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                selected = False
            elif r6x - 50 < x < r6x + 50 and r6y - 100 < y < r6y + 100:
                c.delete(r2)
                r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                selected = False
            elif r7x - 50 < x < r7x + 50 and r7y - 50 < y < r7y + 50:
                c.delete(r2)
                r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                selected = False
            elif r8x - 50 < x < r8x + 50 and r8y - 50 < y < r8y + 50:
                c.delete(r2)
                r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                selected = False
            elif r9x - 50 < x < r9x + 50 and r9y - 50 < y < r9y + 50:
                c.delete(r2)
                r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                selected = False
            elif r10x - 50 < x < r10x + 50 and r10y - 50 < y < r10y + 50:
                c.delete(r2)
                r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                selected = False
            else:
                if x < r2x - 100 and r2y - 100 < y < r2y + 100:
                    item = c.find_overlapping(r2x - 190, r2y - 90, r2x - 110, r2y + 90)
                    print(item)
                    if item == ():
                        c.delete(r2)
                        r2x = r2x - 100
                        r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                        selected = False
                        turncount()
                    else:
                        c.delete(r2)
                        r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                        selected = False
                elif x > r2x + 100 and r2y - 100 < y < r2y + 100:
                    item = c.find_overlapping(r2x + 110, r2y - 90, r2x + 190, r2y + 90)
                    print(item)
                    if item == ():
                        c.delete(r2)
                        r2x = r2x + 100
                        r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                        selected = False
                        turncount()
                    else:
                        c.delete(r2)
                        r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                        selected = False
                elif y < r2y - 100 and r2x - 100 < x < r2x + 100:
                    item = c.find_overlapping(r2x - 90, r2y - 190, r2x + 90, r2y - 110)
                    print(item)
                    if item == ():
                        c.delete(r2)
                        r2y = r2y - 100
                        r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                        selected = False
                        turncount()
                    else:
                        c.delete(r2)
                        r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                        selected = False
                elif y > r2y + 100 and r2x - 100 < x < r2x + 100:
                    item = c.find_overlapping(r2x - 90, r2y + 110, r2x + 90, r2y + 190)
                    print(item)
                    if item == ():
                        c.delete(r2)
                        r2y = r2y + 100
                        r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                        selected = False
                        turncount()
                    else:
                        c.delete(r2)
                        r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
                        selected = False
        
        if select == 'r3':
            if r1x - 50 < x < r1x + 50 and r1y - 100 < y < r1y + 100:
                c.delete(r3)
                r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                selected = False
            elif r2x - 100 < x < r2x + 100 and r2y - 100 < y < r2y + 100:
                c.delete(r3)
                r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                selected = False
            elif r4x - 50 < x < r4x + 50 and r4y - 100 < y < r4y + 100:
                c.delete(r3)
                r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                selected = False
            elif r5x - 100 < x < r5x + 100 and r5y - 50 < y < r5y + 50:
                c.delete(r3)
                r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                selected = False
            elif r6x - 50 < x < r6x + 50 and r6y - 100 < y < r6y + 100:
                c.delete(r3)
                r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                selected = False
            elif r7x - 50 < x < r7x + 50 and r7y - 50 < y < r7y + 50:
                c.delete(r3)
                r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                selected = False
            elif r8x - 50 < x < r8x + 50 and r8y - 50 < y < r8y + 50:
                c.delete(r3)
                r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                selected = False
            elif r9x - 50 < x < r9x + 50 and r9y - 50 < y < r9y + 50:
                c.delete(r3)
                r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                selected = False
            elif r10x - 50 < x < r10x + 50 and r10y - 50 < y < r10y + 50:
                c.delete(r3)
                r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                selected = False
            else:
                if x < r3x - 50 and r3y - 100 < y < r3y + 100:
                    # c.create_rectangle(r3x - 30, r3y - 30, r3x + 30, r3y + 30, fill='blue')
                    item = c.find_overlapping(r3x - 140, r3y - 90, r3x - 60, r3y + 90)
                    print(item)
                    if item == ():
                        c.delete(r3)
                        r3x = r3x - 100
                        r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                        selected = False
                        turncount()
                    else:
                        c.delete(r3)
                        r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                        selected = False
                elif x > r3x + 50 and r3y - 100 < y < r3y + 100:
                    item = c.find_overlapping(r3x + 60, r3y - 90, r3x + 140, r3y + 90)
                    print(item)
                    if item == ():
                        c.delete(r3)
                        r3x = r3x + 100
                        r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                        selected = False
                        turncount()
                    else:
                        c.delete(r3)
                        r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                        selected = False
                elif y < r3y - 100 and r3x - 50 < x < r3x + 50:
                    c.delete(r3)
                    r3y = r3y - 100
                    r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                    selected = False
                    turncount()
                elif y > r3y + 100 and r3x - 50 < x < r3x + 50:
                    c.delete(r3)
                    r3y = r3y + 100
                    turncount()
                    r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                    selected = False
        
        if select == 'r4':
            if r1x - 50 < x < r1x + 50 and r1y - 100 < y < r1y + 100:
                c.delete(r4)
                r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                selected = False
            elif r2x - 100 < x < r2x + 100 and r2y - 100 < y < r2y + 100:
                c.delete(r4)
                r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                selected = False
            elif r3x - 50 < x < r3x + 50 and r3y - 100 < y < r3y + 100:
                c.delete(r4)
                r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                selected = False
            elif r5x - 100 < x < r5x + 100 and r5y - 50 < y < r5y + 50:
                c.delete(r4)
                r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                selected = False
            elif r6x - 50 < x < r6x + 50 and r6y - 100 < y < r6y + 100:
                c.delete(r4)
                r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                selected = False
            elif r7x - 50 < x < r7x + 50 and r7y - 50 < y < r7y + 50:
                c.delete(r4)
                r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                selected = False
            elif r8x - 50 < x < r8x + 50 and r8y - 50 < y < r8y + 50:
                c.delete(r4)
                r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                selected = False
            elif r9x - 50 < x < r9x + 50 and r9y - 50 < y < r9y + 50:
                c.delete(r4)
                r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                selected = False
            elif r10x - 50 < x < r10x + 50 and r10y - 50 < y < r10y + 50:
                c.delete(r4)
                r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                selected = False
            else:
                if x < r4x - 50 and r4y - 100 < y < r4y + 100:
                    item = c.find_overlapping(r4x-140, r4y-90, r4x-90, r4y+90)
                    print(item)
                    if item == ():
                        c.delete(r4)
                        r4x = r4x - 100
                        r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                        selected = False
                        turncount()
                    else:
                        c.delete(r4)
                        r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                        selected = False
                elif x > r4x + 50 and r4y - 100 < y < r4y + 100:
                    item = c.find_overlapping(r4x+60, r4y-90, r4x+140, r4y+90)
                    print(item)
                    if item == ():
                        c.delete(r4)
                        r4x = r4x + 100
                        r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                        selected = False
                        turncount()
                    else:
                        c.delete(r4)
                        r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                        selected = False
                elif y < r4y - 100 and r4x - 50 < x < r4x + 50:
                    c.delete(r4)
                    r4y = r4y - 100
                    r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                    selected = False
                    turncount()
                elif y > r4y + 100 and r4x - 50 < x < r4x + 50:
                    c.delete(r4)
                    r4y = r4y + 100
                    r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                    selected = False
                    turncount()
                    
        if select == 'r5':
            if r1x - 50 < x < r1x + 50 and r1y - 100 < y < r1y + 100:
                c.delete(r5)
                r5 = c.create_rectangle(r5x-100, r5y-50, r5x+100, r5y+50, fill='red')
                selected = False
            elif r2x - 100 < x < r2x + 100 and r2y - 100 < y < r2y + 100:
                c.delete(r5)
                r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='red')
                selected = False
            elif r3x - 50 < x < r3x + 50 and r3y - 100 < y < r3y + 100:
                c.delete(r5)
                r5 = c.create_rectangle(r5x-100, r5y-50, r5x+100, r5y+50, fill='red')
                selected = False
            elif r4x - 50 < x < r4x + 50 and r4y - 100 < y < r4y + 100:
                c.delete(r5)
                r5 = c.create_rectangle(r5x-100, r5y-50, r5x+100, r5y+50, fill='red')
                selected = False
            elif r6x - 100 < x < r6x + 100 and r6y - 100 < y < r6y + 100:
                c.delete(r5)
                r5 = c.create_rectangle(r5x-100, r5y-50, r5x+100, r5y+50, fill='red')
                selected = False
            elif r7x - 50 < x < r7x + 50 and r7y - 50 < y < r7y + 50:
                c.delete(r5)
                r5 = c.create_rectangle(r5x-100, r5y-50, r5x+100, r5y+50, fill='red')
                selected = False
            elif r8x - 50 < x < r8x + 50 and r8y - 50 < y < r8y + 50:
                c.delete(r5)
                r5 = c.create_rectangle(r5x-100, r5y-50, r5x+100, r5y+50, fill='red')
                selected = False
            elif r9x - 50 < x < r9x + 50 and r9y - 50 < y < r9y + 50:
                c.delete(r5)
                r5 = c.create_rectangle(r5x-100, r5y-50, r5x+100, r5y+50, fill='red')
                selected = False
            elif r10x - 50 < x < r10x + 50 and r10y - 50 < y < r10y + 50:
                c.delete(r5)
                r5 = c.create_rectangle(r5x-100, r5y-50, r5x+100, r5y+50, fill='red')
                selected = False

            else:
                if x < r5x - 100 and r5y - 50 < y < r5y + 50:
                    c.delete(r5)
                    r5x = r5x - 100
                    r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='red')
                    selected = False
                    turncount()
                elif x > r5x + 100 and r5y - 50 < y < r5y + 50:
                    c.delete(r5)
                    r5x = r5x + 100
                    r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='red')
                    selected = False
                    turncount()
                elif y < r5y - 50 and r5x - 100 < x < r5x + 100:
                    item = c.find_overlapping(r5x - 90, r5y - 140, r5x + 90, r5y - 60)
                    if item == ():
                        c.delete(r5)
                        r5y = r5y - 100
                        r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='red')
                        selected = False
                        turncount()
                    else:
                        c.delete(r5)
                        r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='red')
                        selected = False
                elif y > r5y + 50 and r5x - 100 < x < r5x + 100:
                    item = c.find_overlapping(r5x-90, r5y+60, r5x+90, r5y+140)
                    print(item)
                    if item == ():
                        c.delete(r5)
                        r5y = r5y + 100
                        r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='red')
                        selected = False
                        turncount()
                    else:
                        c.delete(r5)
                        r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='red')
                        selected = False
        
        if select == 'r6':
            if r1x - 50 < x < r1x + 50 and r1y - 100 < y < r1y + 100:
                c.delete(r6)
                r6 = c.create_rectangle(r6x-50, r6y-100, r6x+50, r6y+100, fill='red')
                selected = False
            elif r2x - 100 < x < r2x + 100 and r2y - 100 < y < r2y + 100:
                c.delete(r6)
                r6 = c.create_rectangle(r6x-50, r6y-100, r6x+50, r6y+100, fill='red')
                selected = False
            elif r3x - 50 < x < r3x + 50 and r3y - 100 < y < r3y + 100:
                c.delete(r6)
                r6 = c.create_rectangle(r6x-50, r6y-100, r6x+50, r6y+100, fill='red')
                selected = False
            elif r4x - 50 < x < r4x + 50 and r4y - 100 < y < r4y + 100:
                c.delete(r6)
                r6 = c.create_rectangle(r6x-50, r6y-100, r6x+50, r6y+100, fill='red')
                selected = False
            elif r5x - 100 < x < r5x + 100 and r5y - 50 < y < r5y + 50:
                c.delete(r6)
                r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='red')
                selected = False
            elif r7x - 50 < x < r7x + 50 and r7y - 50 < y < r7y + 50:
                c.delete(r6)
                r6 = c.create_rectangle(r6x-50, r6y-100, r6x+50, r6y+100, fill='red')
                selected = False
            elif r8x - 50 < x < r8x + 50 and r8y - 50 < y < r8y + 50:
                c.delete(r6)
                r6 = c.create_rectangle(r6x-50, r6y-100, r6x+50, r6y+100, fill='red')
                selected = False
            elif r9x - 50 < x < r9x + 50 and r9y - 50 < y < r9y + 50:
                c.delete(r6)
                r6 = c.create_rectangle(r6x-50, r6y-100, r6x+50, r6y+100, fill='red')
                selected = False
            elif r10x - 50 < x < r10x + 50 and r10y - 50 < y < r10y + 50:
                c.delete(r6)
                r6 = c.create_rectangle(r6x-50, r6y-100, r6x+50, r6y+100, fill='red')
                selected = False

            else:
                if x < r6x - 50 and r6y - 100 < y < r6y + 100:
                    item = c.find_overlapping(r6x-140, r6y-90, r6x-90, r6y+90)
                    print(item)
                    if item == ():
                        c.delete(r6)
                        r6x = r6x - 100
                        r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='red')
                        selected = False
                        turncount()
                    else:
                        c.delete(r6)
                        r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='red')
                        selected = False
                elif x > r6x + 50 and r6y - 100 < y < r6y + 100:
                    item = c.find_overlapping(r6x+60, r6y-90, r6x+140, r6y+90)
                    print(item)
                    if item == ():
                        c.delete(r6)
                        r6x = r6x + 100
                        r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='red')
                        selected = False
                        turncount()
                    else:
                        c.delete(r6)
                        r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='red')
                        selected = False
                elif y < r6y - 100 and r6x - 50 < x < r6x + 50:
                    c.delete(r6)
                    r6y = r6y - 100
                    r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='red')
                    selected = False
                    turncount()
                elif y > r6y + 100 and r6x - 50 < x < r6x + 50:
                    c.delete(r6)
                    r6y = r6y + 100
                    r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='red')
                    selected = False
                    turncount()
        
        if select == 'r7':
            if r1x - 50 < x < r1x + 50 and r1y - 100 < y < r1y + 100:
                c.delete(r7)
                r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                selected = False
            elif r2x - 100 < x < r2x + 100 and r2y - 100 < y < r2y + 100:
                c.delete(r7)
                r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                selected = False
            elif r3x - 50 < x < r3x + 50 and r3y - 100 < y < r3y + 100:
                c.delete(r7)
                r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                selected = False
            elif r4x - 50 < x < r4x + 50 and r4y - 100 < y < r4y + 100:
                c.delete(r7)
                r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                selected = False
            elif r5x - 100 < x < r5x + 100 and r5y - 50 < y < r5y + 50:
                c.delete(r7)
                r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                selected = False
            elif r6x - 50 < x < r6x + 50 and r6y - 100 < y < r6y + 100:
                c.delete(r7)
                r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                selected = False
            elif r7x - 50 < x < r7x + 50 and r7y - 50 < y < r7y + 50:
                c.delete(r7)
                r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                selected = False
            elif r9x - 50 < x < r9x + 50 and r9y - 50 < y < r9y + 50:
                c.delete(r7)
                r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                selected = False
            elif r10x - 50 < x < r10x + 50 and r10y - 50 < y < r10y + 50:
                c.delete(r7)
                r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                selected = False
            else:
                if x < r7x - 50 and r7y - 50 < y < r7y + 50:
                    c.delete(r7)
                    r7x = r7x - 100
                    r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                    selected = False
                    turncount()
                elif x > r7x + 50 and r7y - 50 < y < r7y + 50:
                    c.delete(r7)
                    r7x = r7x + 100
                    r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                    selected = False
                    turncount()
                elif y < r7y - 50 and r7x - 50 < x < r7x + 50:
                    c.delete(r7)
                    r7y = r7y - 100
                    r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                    selected = False
                    turncount()
                elif y > r7y + 50 and r7x - 50 < x < r7x + 50:
                    c.delete(r7)
                    r7y = r7y + 100
                    r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                    selected = False
                    turncount()

        if select == 'r8':
            if r1x - 50 < x < r1x + 50 and r1y - 100 < y < r1y + 100:
                c.delete(r8)
                r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                selected = False
            elif r2x - 100 < x < r2x + 100 and r2y - 100 < y < r2y + 100:
                c.delete(r8)
                r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                selected = False
            elif r3x - 50 < x < r3x + 50 and r3y - 100 < y < r3y + 100:
                c.delete(r8)
                r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                selected = False
            elif r4x - 50 < x < r4x + 50 and r4y - 100 < y < r4y + 100:
                c.delete(r8)
                r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                selected = False
            elif r5x - 100 < x < r5x + 100 and r5y - 50 < y < r5y + 50:
                c.delete(r8)
                r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                selected = False
            elif r6x - 50 < x < r6x + 50 and r6y - 100 < y < r6y + 100:
                c.delete(r8)
                r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                selected = False
            elif r7x - 50 < x < r7x + 50 and r7y - 50 < y < r7y + 50:
                c.delete(r8)
                r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                selected = False
            elif r9x - 50 < x < r9x + 50 and r9y - 50 < y < r9y + 50:
                c.delete(r8)
                r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                selected = False
            elif r10x - 50 < x < r10x + 50 and r10y - 50 < y < r10y + 50:
                c.delete(r8)
                r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                selected = False
            else:
                if x < r8x - 50 and r8y - 50 < y < r8y + 50:
                    c.delete(r8)
                    r8x = r8x - 100
                    r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                    selected = False
                    turncount()
                elif x > r8x + 50 and r8y - 50 < y < r8y + 50:
                    c.delete(r8)
                    r8x = r8x + 100
                    r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                    selected = False
                    turncount()
                elif y < r8y - 50 and r8x - 50 < x < r8x + 50:
                    c.delete(r8)
                    r8y = r8y - 100
                    r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                    selected = False
                    turncount()
                elif y > r8y + 50 and r8x - 50 < x < r8x + 50:
                    c.delete(r8)
                    r8y = r8y + 100
                    r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                    selected = False
                    turncount()
                    
        if select == 'r9':
            if r1x - 50 < x < r1x + 50 and r1y - 100 < y < r1y + 100:
                c.delete(r9)
                r9 = c.create_rectangle(r9x-50, r9y-50, r9x+50, r9y+50, fill='red')
                selected = False
            elif r2x - 100 < x < r2x + 100 and r2y - 100 < y < r2y + 100:
                c.delete(r9)
                r9 = c.create_rectangle(r9x - 50, r9y - 50, r9x + 50, r9y + 50, fill='red')
                selected = False
            elif r3x - 50 < x < r3x + 50 and r3y - 100 < y < r3y + 100:
                c.delete(r9)
                r9 = c.create_rectangle(r9x - 50, r9y - 50, r9x + 50, r9y + 50, fill='red')
                selected = False
            elif r4x - 50 < x < r4x + 50 and r4y - 100 < y < r4y + 100:
                c.delete(r9)
                r9 = c.create_rectangle(r9x - 50, r9y - 50, r9x + 50, r9y + 50, fill='red')
                selected = False
            elif r5x - 100 < x < r5x + 100 and r5y - 50 < y < r5y + 50:
                c.delete(r9)
                r9 = c.create_rectangle(r9x - 50, r9y - 50, r9x + 50, r9y + 50, fill='red')
                selected = False
            elif r6x - 50 < x < r6x + 50 and r6y - 100 < y < r6y + 100:
                c.delete(r9)
                r9 = c.create_rectangle(r9x - 50, r9y - 50, r9x + 50, r9y + 50, fill='red')
                selected = False
            elif r7x - 50 < x < r7x + 50 and r7y - 50 < y < r7y + 50:
                c.delete(r9)
                r9 = c.create_rectangle(r9x - 50, r9y - 50, r9x + 50, r9y + 50, fill='red')
                selected = False
            elif r8x - 50 < x < r8x + 50 and r8y - 50 < y < r8y + 50:
                c.delete(r9)
                r9 = c.create_rectangle(r9x - 50, r9y - 50, r9x + 50, r9y + 50, fill='red')
                selected = False
            elif r10x - 50 < x < r10x + 50 and r10y - 50 < y < r10y + 50:
                c.delete(r9)
                r9 = c.create_rectangle(r9x - 50, r9y - 50, r9x + 50, r9y + 50, fill='red')
                selected = False
            else:
                if x < r9x-50 and r9y-50 < y < r9y+50:
                    c.delete(r9)
                    r9x = r9x - 100
                    r9 = c.create_rectangle(r9x-50, r9y-50, r9x+50, r9y+50, fill='red')
                    selected = False
                    turncount()
                elif x > r9x+50 and r9y-50 < y < r9y+50:
                    c.delete(r9)
                    r9x = r9x + 100
                    r9 = c.create_rectangle(r9x-50, r9y-50, r9x+50, r9y+50, fill='red')
                    selected = False
                    turncount()
                elif y < r9y-50 and r9x-50 < x < r9x+50:
                    c.delete(r9)
                    r9y = r9y - 100
                    r9 = c.create_rectangle(r9x-50, r9y-50, r9x+50, r9y+50, fill='red')
                    selected = False
                    turncount()
                elif y > r9y+50 and r9x-50 < x < r9x+50:
                    c.delete(r9)
                    r9y = r9y + 100
                    r9 = c.create_rectangle(r9x-50, r9y-50, r9x+50, r9y+50, fill='red')
                    selected = False
                    turncount()

        if select == 'r10':
            if r1x - 50 < x < r1x + 50 and r1y - 100 < y < r1y + 100:
                c.delete(r10)
                r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                selected = False
            elif r2x - 100 < x < r2x + 100 and r2y - 100 < y < r2y + 100:
                c.delete(r10)
                r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                selected = False
            elif r3x - 50 < x < r3x + 50 and r3y - 100 < y < r3y + 100:
                c.delete(r10)
                r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                selected = False
            elif r4x - 50 < x < r4x + 50 and r4y - 100 < y < r4y + 100:
                c.delete(r10)
                r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                selected = False
            elif r5x - 100 < x < r5x + 100 and r5y - 50 < y < r5y + 50:
                c.delete(r10)
                r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                selected = False
            elif r6x - 50 < x < r6x + 50 and r6y - 100 < y < r6y + 100:
                c.delete(r10)
                r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                selected = False
            elif r7x - 50 < x < r7x + 50 and r7y - 50 < y < r7y + 50:
                c.delete(r10)
                r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                selected = False
            elif r8x - 50 < x < r8x + 50 and r8y - 50 < y < r8y + 50:
                c.delete(r10)
                r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                selected = False
            elif r9x - 50 < x < r9x + 50 and r9y - 50 < y < r9y + 50:
                c.delete(r10)
                r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                selected = False
            else:
                if x < r10x - 50 and r10y - 50 < y < r10y + 50:
                    c.delete(r10)
                    r10x = r10x - 100
                    r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                    selected = False
                    turncount()
                elif x > r10x + 50 and r10y - 50 < y < r10y + 50:
                    c.delete(r10)
                    r10x = r10x + 100
                    r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                    selected = False
                    turncount()
                elif y < r10y - 50 and r10x - 50 < x < r10x + 50:
                    c.delete(r10)
                    r10y = r10y - 100
                    r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                    selected = False
                    turncount()
                elif y > r10y + 50 and r10x - 50 < x < r10x + 50:
                    c.delete(r10)
                    r10y = r10y + 100
                    r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                    selected = False
                    turncount()

    if r2x == 200 and r2y == 400:
        vict = tk.Label(master=frame1, text='YOU WON!', font=("Courier", 24, 'bold'), bg='yellow')
        vict.place(x=120, y=10)


def newgame():

    global r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, turns
    global r1x, r1y, r2x, r2y, r3x, r3y, r4x, r4y, r5x, r5y, r6x, r6y, r7x, r7y, r8x, r8y, r9x, r9y, r10x, r10y
    c.delete(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10)

    turns = 0
    T.delete(0, tk.END)
    T.insert(tk.END, turns)

    r1x = 50
    r1y = 100
    r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')

    r2x = 200
    r2y = 100
    r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')

    r3x = 350
    r3y = 100
    r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')

    r4x = 50
    r4y = 300
    r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')

    r5x = 200
    r5y = 250
    r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='red')

    r6x = 350
    r6y = 300
    r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='red')

    r7x = 150
    r7y = 350
    r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')

    r8x = 250
    r8y = 350
    r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')

    r9x = 50
    r9y = 450
    r9 = c.create_rectangle(r9x - 50, r9y - 50, r9x + 50, r9y + 50, fill='red')

    r10x = 350
    r10y = 450
    r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
    
def savegame():
    global r1x, r1y, r2x, r2y, r3x, r3y, r4x, r4y, r5x, r5y, r6x, r6y, r7x, r7y, r8x, r8y, r9x, r9y, r10x, r10y
    file = open('save.txt', 'w')
    file.write(str(r1x)+'\n')
    file.write(str(r1y)+'\n')
    file.write(str(r2x)+'\n')
    file.write(str(r2y)+'\n')
    file.write(str(r3x)+'\n')
    file.write(str(r3y)+'\n')    
    file.write(str(r4x)+'\n')
    file.write(str(r4y)+'\n')
    file.write(str(r5x)+'\n')
    file.write(str(r5y)+'\n')
    file.write(str(r6x)+'\n')
    file.write(str(r6y)+'\n')
    file.write(str(r7x)+'\n')
    file.write(str(r7y)+'\n')
    file.write(str(r8x)+'\n')
    file.write(str(r8y)+'\n')
    file.write(str(r9x)+'\n')
    file.write(str(r9y)+'\n')
    file.write(str(r10x)+'\n')
    file.write(str(r10y)+'\n')
    file.write(str(turns)+'\n')
    file.close()

def loadgame():

    global r1, r2, r3, r4, r5, r6, r7, r8, r9, r10
    global r1x, r1y, r2x, r2y, r3x, r3y, r4x, r4y, r5x, r5y, r6x, r6y, r7x, r7y, r8x, r8y, r9x, r9y, r10x, r10y
    c.delete(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10)

    file = open('save.txt', 'r')
    lines = file.readlines()
    r1x = int(lines[0])
    r1y = int(lines[1])
    print(r1x, r1y)
    r2x = int(lines[2])
    r2y = int(lines[3])
    r3x = int(lines[4])
    r3y = int(lines[5])
    r4x = int(lines[6])
    r4y = int(lines[7])
    r5x = int(lines[8])
    r5y = int(lines[9])
    r6x = int(lines[10])
    r6y = int(lines[11])
    r7x = int(lines[12])
    r7y = int(lines[13])
    r8x = int(lines[14])
    r8y = int(lines[15])
    r9x = int(lines[16])
    r9y = int(lines[17])
    r10x = int(lines[18])
    r10y = int(lines[19])
    turns = int(lines[20])
    T.delete(0, tk.END)
    T.insert(tk.END, turns)

    r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
    r2 = c.create_rectangle(r2x - 100, r2y - 100, r2x + 100, r2y + 100, fill='blue')
    r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
    r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
    r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='red')
    r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='red')
    r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
    r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
    r9 = c.create_rectangle(r9x - 50, r9y - 50, r9x + 50, r9y + 50, fill='red')
    r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
    

NewButton = tk.Button(master = frame1, text ="NEW", width = 10, command=newgame)
NewButton.place(x=5,y=5)

SaveButton = tk.Button(master = frame1, text ="SAVE", width = 4, command=savegame)
SaveButton.place(x=5,y=35)

LoadButton = tk.Button(master = frame1, text ="LOAD", width = 4, command=loadgame)
LoadButton.place(x=46,y=35)



c.bind('<Button-1>', klik)
tk.mainloop()