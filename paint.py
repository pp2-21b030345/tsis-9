import pygame as pg

pg.init()                                           #starting pygame
screen = pg.display.set_mode((800, 600))            #creating a screen
screen.fill((255, 255, 255))


def line(screen, start, end, d, color):                 #class of line
    x1 = start[0]                                       #starting point on x
    y1 = start[1]                                       #starting point on y
    x2 = end[0]                                         #ending point on x
    y2 = end[1]                                         #ending point on y

    dx = abs(x1 - x2)                                   #length determination horizontally
    dy = abs(y1 - y2)                                   #length determination vertically

    A = y2 - y1                                         #part of formula
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:                                         #length comparison
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B                            #formula of equation of line
            pg.draw.circle(screen, color, (x, y), d)        #creating line by circles
    else:   
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pg.draw.circle(screen, color, (x, y), d)
        

def rectangle(screen, start, end, d, color):
    x1 = start[0]                                       #starting point on x
    y1 = start[1]                                       #starting point on y
    x2 = end[0]                                         #ending point on x
    y2 = end[1]                                         #ending point on y

    width = abs(x1-x2)                                         #width of rectangle
    height = abs(y1-y2)                                        #height of rectangle

    if x1 <= x2:                                                                #condition that starting point is to the left of the end point
        if y1 < y2:                                                             #condition that starting point is to the left of the end point
            pg.draw.rect(screen, color, (x1, y1, width, height), d)             #creating rectangle with starting positions x1 and y1
        else:
            pg.draw.rect(screen, color, (x1, y2, width, height), d)
    else:
        if y1 < y2:
            pg.draw.rect(screen, color, (x2, y1, width, height), d)
        else:
            pg.draw.rect(screen, color, (x2, y2, width, height), d)


def circle(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1-x2)
    height = abs(y1-y2)

    if x1 <= x2:
        if y1 < y2:
            pg.draw.ellipse(screen, color, (x1, y1, width, height), d)
        else:
            pg.draw.ellipse(screen, color, (x1, y2, width, height), d)
    else:
        if y1 < y2:
            pg.draw.ellipse(screen, color, (x2, y1, width, height), d)
        else:
            pg.draw.ellipse(screen, color, (x2, y2, width, height), d)


def square(screen, start, end, d, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    mn = min(abs(x2 - x1), abs(y2 - y1)) 
 
    if x2 > x1 and y2 > y1: 
        pg.draw.rect(screen, color, (x1, y1, mn, mn), d)
    if y2 > y1 and x1 > x2: 
        pg.draw.rect(screen, color, (x2, y1, mn, mn), d)
    if x1 > x2 and y1 > y2: 
        pg.draw.rect(screen, color, (x2, y2, mn, mn), d)
    if x2 > x1 and y1 > y2: 
        pg.draw.rect(screen, color, (x1, y2, mn, mn),)


def rtri(screen, start, end, d, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    
    if x2 > x1 and y2 > y1: 
        pg.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x1, y2)), d) 
    if y2 > y1 and x1 > x2: 
        pg.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x1, y2)), d) 
    if x1 > x2 and y1 > y2: 
        pg.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x2, y1)), d) 
    if x2 > x1 and y1 > y2: 
        pg.draw.polygon(screen, color, ((x1, y1), (x2, y2), (x2, y1)), d) 


def etri(screen, start, end, d, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
 
    leng = abs(x2 - x1) 
    height = (3**0.5) * leng / 2 
 
    if y2 > y1: 
        pg.draw.polygon(screen, color, ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), d) 
    else: 
        pg.draw.polygon(screen, color, ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)), d) 


def rhom(screen, start, end, d, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1]

    pg.draw.lines(screen, color, True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2),
        ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), d) 


last_pos = (0, 0)                                   #a variable that will take the last coordinates of the shapes
w = 2                                               #the width of the shapes
draw_line = False
erase = False
ed = 50                                             #the scale of the erasure
color = (0, 0, 0)                                   #default color black
d = {
    'line' : True,                                  #default figure line
    'rect': False,
    'circle': False,
    'erase': False,
    'square': False,
    'rtri': False,
    'etri': False,
    'rhom': False
}

running = True                                                      #variable for loop operation
while running:                                                      #starting loop
    pos = pg.mouse.get_pos()                                        #starting position of the mouse
    for event in pg.event.get():
        if event.type == pg.QUIT:                                   #when the screen is closed, the cycle stops
            running = False
        if event.type == pg.KEYDOWN:                                #reaction to button presses
            if event.key == pg.K_1:                                 #press 1 - draw the line
                d['line'] = True                                    #by defautl - is line 
                for k, v in d.items():                              #looping through the dict
                    if k != 'line':                                 #if not line - another is False
                        d[k] = False
            if event.key == pg.K_2:                                 #press 2 - draw rectangle 
                d['rect'] = True
                for k, v in d.items():
                    if k != 'rect':
                        d[k] = False
            if event.key == pg.K_3:                                 #press 3 - draw circle
                d['circle'] = True
                for k, v in d.items():
                    if k != 'circle':
                        d[k] = False
            if event.key == pg.K_4:                                 #press 4 - eraser
                d['erase'] = True
                for k, v in d.items():
                    if k != 'erase':
                        d[k] = False
            if event.key == pg.K_5:                                 #press 5 - square
                d['square'] = True
                for k, v in d.items():
                    if k != 'square':
                        d[k] = False
            if event.key == pg.K_6:                                 #press 6 - right trianle
                d['rtri'] = True
                for k, v in d.items():
                    if k != 'rtri':
                        d[k] = False
            if event.key == pg.K_7:                                 #press 7 - equivalent trianle
                d['etri'] = True
                for k, v in d.items():
                    if k != 'etri':
                        d[k] = False
            if event.key == pg.K_8:                                 #press 8 - rhombus
                d['rhom'] = True
                for k, v in d.items():
                    if k != 'rhom':
                        d[k] = False
            if event.key == pg.K_q:                                 #press q - set green color
                color = (0, 255, 0)
            if event.key == pg.K_w:                                 #press w - set red color
                color = (255, 0, 0)
            if event.key == pg.K_e:                                 #press e - set blue color
                color = (0, 0, 255)
            if event.key == pg.K_r:                                 #press r - set black color
                color = (0, 0, 0)

        if d['line'] == 1:                                          #if line = true
            if event.type == pg.MOUSEBUTTONDOWN:                    #if we press the mouse
                last_pos = pos
                pg.draw.circle(screen, color, pos, w)               #get the mouse pos 
                draw_line = True                                        
            if event.type == pg.MOUSEBUTTONUP:                      #if we unpress the mouse - stop line
                draw_line = False
            if event.type == pg.MOUSEMOTION:                        #movement of the mouse 
                if draw_line:
                    line(screen, last_pos, pos, w, color)           #draw line by the mouse pos 
                last_pos = pos
        elif d['rect'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                rectangle(screen, last_pos, pos, w, color)
        elif d['circle'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                circle(screen, last_pos, pos, w, color)
        elif d['erase'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                (x, y) = pos                                      
                pg.draw.rect(screen, (255, 255, 255), (x, y, ed, ed))   
                erase = True
            if event.type == pg.MOUSEMOTION:
                if erase:
                    pg.draw.rect(screen, (255, 255, 255), (pos[0], pos[1], ed, ed))
            if event.type == pg.MOUSEBUTTONUP:
                erase = False
        elif d['square'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                square(screen, last_pos, pos, w, color)
        elif d['rtri'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                rtri(screen, last_pos, pos, w, color)
        elif d['etri'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                etri(screen, last_pos, pos, w, color)
        elif d['rhom'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                rhom(screen, last_pos, pos, w, color)
    pg.display.update()                                            #updating the screen with changes
pg.quit()                                                          #stopping the code