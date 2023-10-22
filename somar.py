import tkinter as tk

root = tk.Tk()
root.title('Somar')
root.geometry('400x500')
c = tk.Canvas(master=root, width = 400, height = 500)
c.pack()

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


selected = False

def klik(event):
    global r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, select
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
                    else:
                        c.delete(r1)
                        r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                        selected = False
                elif y < r1y - 100 and r1x - 50 < x < r1x + 50:
                    c.delete(r1)
                    r1y = r1y - 100
                    r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                    selected = False
                elif y > r1y + 100 and r1x - 50 < x < r1x + 50:
                    c.delete(r1)
                    r1y = r1y + 100
                    r1 = c.create_rectangle(r1x - 50, r1y - 100, r1x + 50, r1y + 100, fill='red')
                    selected = False
                    
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
                    else:
                        c.delete(r3)
                        r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                        selected = False
                elif y < r3y - 100 and r3x - 50 < x < r3x + 50:
                    c.delete(r3)
                    r3y = r3y - 100
                    r3 = c.create_rectangle(r3x - 50, r3y - 100, r3x + 50, r3y + 100, fill='red')
                    selected = False
                elif y > r3y + 100 and r3x - 50 < x < r3x + 50:
                    c.delete(r3)
                    r3y = r3y + 100
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
                    else:
                        c.delete(r4)
                        r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                        selected = False
                elif y < r4y - 100 and r4x - 50 < x < r4x + 50:
                    c.delete(r4)
                    r4y = r4y - 100
                    r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                    selected = False
                elif y > r4y + 100 and r4x - 50 < x < r4x + 50:
                    c.delete(r4)
                    r4y = r4y + 100
                    r4 = c.create_rectangle(r4x - 50, r4y - 100, r4x + 50, r4y + 100, fill='red')
                    selected = False
                    
        if select == 'r5':
            if r1x - 50 < x < r1x + 50 and r1y - 100 < y < r1y + 100:
                pass
            elif r2x - 100 < x < r2x + 100 and r2y - 100 < y < r2y + 100:
                pass
            elif r3x - 50 < x < r3x + 50 and r3y - 100 < y < r3y + 100:
                pass
            elif r4x - 50 < x < r4x + 50 and r4y - 100 < y < r4y + 100:
                pass
            elif r6x - 100 < x < r6x + 100 and r6y - 100 < y < r6y + 100:
                pass
            elif r7x - 50 < x < r7x + 50 and r7y - 50 < y < r7y + 50:
                pass
            elif r8x - 50 < x < r8x + 50 and r8y - 50 < y < r8y + 50:
                pass
            elif r9x - 50 < x < r9x + 50 and r9y - 50 < y < r9y + 50:
                pass
            elif r10x - 50 < x < r10x + 50 and r10y - 50 < y < r10y + 50:
                pass
            else:
                if x < r5x - 100 and r5y - 50 < y < r5y + 50:
                    c.delete(r5)
                    r5x = r5x - 100
                    r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='red')
                    selected = False
                elif x > r5x + 50 and r5y - 50 < y < r5y + 50:
                    c.delete(r5)
                    r5x = r5x + 100
                    r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='red')
                    selected = False
                elif y < r5y - 50 and r5x - 100 < x < r5x + 100:
                    item = c.find_overlapping(r5x - 90, r5y - 140, r5x + 90, r5y - 60)
                    if item == ():
                        c.delete(r5)
                        r5y = r5y - 100
                        r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='red')
                        selected = False
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
                    else:
                        c.delete(r5)
                        r5 = c.create_rectangle(r5x - 100, r5y - 50, r5x + 100, r5y + 50, fill='red')
                        selected = False
        
        if select == 'r6':
            if r1x - 50 < x < r1x + 50 and r1y - 100 < y < r1y + 100:
                pass
            elif r2x - 100 < x < r2x + 100 and r2y - 100 < y < r2y + 100:
                pass
            elif r3x - 50 < x < r3x + 50 and r3y - 100 < y < r3y + 100:
                pass
            elif r4x - 50 < x < r4x + 50 and r4y - 100 < y < r4y + 100:
                pass
            elif r5x - 100 < x < r5x + 100 and r5y - 50 < y < r5y + 50:
                pass
            elif r7x - 50 < x < r7x + 50 and r7y - 50 < y < r7y + 50:
                pass
            elif r8x - 50 < x < r8x + 50 and r8y - 50 < y < r8y + 50:
                pass
            elif r9x - 50 < x < r9x + 50 and r9y - 50 < y < r9y + 50:
                pass
            elif r10x - 50 < x < r10x + 50 and r10y - 50 < y < r10y + 50:
                pass
            else:
                if x < r6x - 50 and r6y - 100 < y < r6y + 100:
                    item = c.find_overlapping(r6x-140, r6y-90, r6x-90, r6y+90)
                    print(item)
                    if item == ():
                        c.delete(r6)
                        r6x = r6x - 100
                        r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='red')
                        selected = False
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
                    else:
                        c.delete(r6)
                        r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='red')
                        selected = False
                elif y < r6y - 100 and r6x - 50 < x < r6x + 50:
                    c.delete(r6)
                    r6y = r6y - 100
                    r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='red')
                    selected = False
                elif y > r6y + 100 and r6x - 50 < x < r6x + 50:
                    c.delete(r6)
                    r6y = r6y + 100
                    r6 = c.create_rectangle(r6x - 50, r6y - 100, r6x + 50, r6y + 100, fill='red')
                    selected = False
        
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
                elif x > r7x + 50 and r7y - 50 < y < r7y + 50:
                    c.delete(r7)
                    r7x = r7x + 100
                    r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                    selected = False
                elif y < r7y - 50 and r7x - 50 < x < r7x + 50:
                    c.delete(r7)
                    r7y = r7y - 100
                    r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                    selected = False
                elif y > r7y + 50 and r7x - 50 < x < r7x + 50:
                    c.delete(r7)
                    r7y = r7y + 100
                    r7 = c.create_rectangle(r7x - 50, r7y - 50, r7x + 50, r7y + 50, fill='red')
                    selected = False

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
                elif x > r8x + 50 and r8y - 50 < y < r8y + 50:
                    c.delete(r8)
                    r8x = r8x + 100
                    r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                    selected = False
                elif y < r8y - 50 and r8x - 50 < x < r8x + 50:
                    c.delete(r8)
                    r8y = r8y - 100
                    r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                    selected = False
                elif y > r8y + 50 and r8x - 50 < x < r8x + 50:
                    c.delete(r8)
                    r8y = r8y + 100
                    r8 = c.create_rectangle(r8x - 50, r8y - 50, r8x + 50, r8y + 50, fill='red')
                    selected = False
                    
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
                elif x > r9x+50 and r9y-50 < y < r9y+50:
                    c.delete(r9)
                    r9x = r9x + 100
                    r9 = c.create_rectangle(r9x-50, r9y-50, r9x+50, r9y+50, fill='red')
                    selected = False
                elif y < r9y-50 and r9x-50 < x < r9x+50:
                    c.delete(r9)
                    r9y = r9y - 100
                    r9 = c.create_rectangle(r9x-50, r9y-50, r9x+50, r9y+50, fill='red')
                    selected = False
                elif y > r9y+50 and r9x-50 < x < r9x+50:
                    c.delete(r9)
                    r9y = r9y + 100
                    r9 = c.create_rectangle(r9x-50, r9y-50, r9x+50, r9y+50, fill='red')
                    selected = False

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
                elif x > r10x + 50 and r10y - 50 < y < r10y + 50:
                    c.delete(r10)
                    r10x = r10x + 100
                    r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                    selected = False
                elif y < r10y - 50 and r10x - 50 < x < r10x + 50:
                    c.delete(r10)
                    r10y = r10y - 100
                    r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                    selected = False
                elif y > r10y + 50 and r10x - 50 < x < r10x + 50:
                    c.delete(r10)
                    r10y = r10y + 100
                    r10 = c.create_rectangle(r10x - 50, r10y - 50, r10x + 50, r10y + 50, fill='red')
                    selected = False

c.bind('<Button-1>', klik)
tk.mainloop()