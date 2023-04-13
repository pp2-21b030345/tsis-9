import random, time
import pygame as pg

pg.init()                                           #starting pygame

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pg.display.set_mode((800, 600))                                                #creating a screen
background = pg.transform.smoothscale(pg.image.load('snake.jpg'), (800, 600))           #loading an image and overlaying it on the screen
pg.display.set_caption('SNAKE')

font = pg.font.SysFont('Times New Roman', 60)
game_over = font.render("Game Over", True, RED)
font1 = pg.font.SysFont('Times New Roman', 20)
levele = font1.render("LEVEL = ", True, BLACK)
scoree = font1.render("SCORE = ", True, BLACK)
a=[]                                              #points counter

class Snake:
    global level, score                           #global variables
    def __init__(self, x, y):
        self.size = 1                             #initial size
        self.elements = [[x, y]]                  #location of snake`s head`
        self.radius = 10                          #snake size
        self.dx = 5                               #starting direction
        self.dy = 0
        self.is_add = False                       #sign of eating food
        self.speed = 40                           #number of steps
        if len(a) >= 20:                          #Condition for speed increasing
            self.speed +=5

    def draw(self):
        for element in self.elements:
            pg.draw.circle(screen, RED, element, self.radius)           #creating the object

    def add_to_snake(self):                                             #function for updating
        self.size += 1                                                  #size updating
        self.elements.append([0, 0])                                    #adding coordinates for new part of snake
        self.is_add = False
        if score % 5 == 0:
            self.speed += 5                                             #speed increasing

    def move(self):
        if self.is_add:                                                 #if true
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]               #movement of each part of snake
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx                                  #constant repeating
        self.elements[0][1] += self.dy

        if self.elements[0][0] > 795 or self.elements[0][0] < 5:        #conditions of gameover by x
            screen.fill(BLACK)
            screen.blit(game_over, (220, 250))                          #label output
            pg.display.update()                                         #updating the screen with changes
            time.sleep(2)                                               #time of new screen
            pg.quit()                                                   #stoping game
            pg.exit()                                                   #closing game

        if self.elements[0][1] > 595 or self.elements[0][1] < 5:
            
            screen.fill(BLACK)
            screen.blit(game_over, (220, 250))
            pg.display.update()
            time.sleep(2)
            pg.quit()
            pg.exit()

    def eat(self, foodx, foody):                                        #function for eating food
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx <= x <= foodx + 20 and foody <= y <= foody + 20:       #condition when snake have same position with food
            return True
        return False

class Food:
    def __init__(self):
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 500)

    def gen(self):
        self.x = random.randint(0, 700)                                 #random apearance in range of x
        self.y = random.randint(0, 500)                                 #random apearance in range of y

    def draw(self):
        pg.draw.rect(screen, BLUE, (self.x, self.y, 12, 12))            #creatind food

score = 0                                                               #count of number of score
level = 0                                                               #count of level

def show_level(x, y):
    global level
    s = font1.render(f'{level}', True, BLACK)                           #label output
    screen.blit(s, (x, y))

def show_score(x, y):
    global score
    s = font1.render(f'{score}', True, BLACK)
    screen.blit(s, (x, y))

snake1 = Snake(100, 100)                                                #assigning a class to a variable, initial position of snake
food = Food()                                                           #assigning a class to a variable

running = True                                                          #variable for loop operation
FPS = 30                                                                #number of frames per second
step = 5                                                                #number of steps

clock = pg.time.Clock()

while running:                                                          #starting loop
    clock.tick(snake1.speed)                                            #initial movement
    show_score(795, 20)                                                 #position of labels
    for event in pg.event.get():
        if event.type == pg.QUIT:                                       #when the screen is closed, the cycle stops
            running = False

        if event.type == pg.KEYDOWN:                                    #reaction to button presses
            if event.key == pg.K_RIGHT and snake1.dx != -step:          #condition that pressed right button and snake don`t move to the left
                snake1.dx = step                                        #changing direction horizontally
                snake1.dy = 0                                           #canceling the movement verticaly
            if event.key == pg.K_LEFT and snake1.dx != step:
                snake1.dx = -step
                snake1.dy = 0
            if event.key == pg.K_UP and snake1.dy != step:
                snake1.dx = 0
                snake1.dy = -step
            if event.key == pg.K_DOWN and snake1.dy != -step:
                snake1.dx = 0
                snake1.dy = step

    if snake1.eat(food.x, food.y):                                      #function call
        snake1.is_add = True                                            #sign for updating snake
        score += random.randint(1, 5)                                   #Adding the score
        food.gen()                                                      #creating new food
        if score % 4 == 0:                                              #condition of level up
            level += 1
            a.append(1)                                                 #Speed increasing

    snake1.move()
    screen.fill(BLACK)
    screen.blit(background, (0, 0))                                     #image overlay
    snake1.draw()
    food.draw()
    screen.blit(levele, (690, 0))                                       #label location
    screen.blit(scoree, (690, 20))
    show_score(775, 20)
    show_level(775, 0)
    pg.display.update()                                             #updating the screen with changes
pg.quit()                                                           #stopping the code