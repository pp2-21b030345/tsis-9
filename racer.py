import pygame as pg
import random, time

WIDTH = 800                         #width of screen
HEIGHT = 600                        #height of screen
FPS = 60                            #number of frames per second
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
score = 0                           #counter that counting the number of points

pg.init()                                            #starting pygame
screen = pg.display.set_mode((WIDTH, HEIGHT))        #creating a screen
clock = pg.time.Clock()                              #frequency of updates
pg.display.set_caption("RACER")                      #screen name
road = pg.image.load('./trace.png')                  #background loading
font = pg.font.SysFont('Times New Roman', 50)        #characteristics of the of scores label
a = []                                               #points counter

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('./car2.png')               #loading the player's car
        self.surf = pg.Surface((50, 75))                       #creating a surface for an object with size
        self.rect = self.surf.get_rect(center=(400, 500))      #creating a rectangle superimposed on the surface of an object
        self.speed = 5                                         #number of steps on which car will move

    def move(self):                                            #machine movement function
        keys = pg.key.get_pressed()                            #a variable that will accept keystrokes on the keyboard
        if keys[pg.K_UP] and self.rect.top > 0:                #the condition when the up button is pressed and the car is not located on the upper border of the screen
            self.rect.move_ip(0, -self.speed)                  #moving the object up the specified number of steps vertically
        if keys[pg.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.move_ip(0, self.speed)
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(self.speed, 0)
   
    def draw(self):                                                            #function for inserting an object
        self.surf.blit(pg.transform.scale(self.image, (50, 75)), (0, 0))       #resizing the image
        screen.blit(self.surf, (self.rect.x, self.rect.y))                     #superimposing a photo on a rectangle of an object


class Enemy(pg.sprite.Sprite):                                                         #a class for controlling the enemies
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('./car1.png')
        self.surf = pg.Surface((40, 60))
        self.rect = self.surf.get_rect(center=(random.randint(0, WIDTH - 40), -100))   #the appearance of objects outside the screen
        self.speed = random.randint(3, 5)                                              #random speed in the specified range
        if len(a) > 5:                                                                 #checking for the score to increase the speed
            self.speed += 3                                                            #enemy`s speed increase

    def move(self):
        self.rect.move_ip(0, self.speed)                  #the movement of an object with a constant vertical velocity
       
    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (40, 60)), (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def kil(self):                                        #object deletion function
        if self.rect.top > HEIGHT:                        #conditions that the coordinates of the object exceed the height of the screen
            self.kill()                                   #object deletion


class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((20, 20))
        self.rect = self.surf.get_rect(center=(random.randint(0, WIDTH - 40), -100))
        self.speed = random.randint(1, 8)
        self.random_number = random.randint(0, 9)
        self.images = [pg.image.load('./coin.png'), pg.image.load('./megacoin.png')]
        self.megacoin()

    def move(self):
        self.rect.move_ip(0, self.speed)

    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (20, 20)), (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def kil(self):
        if self.rect.top > HEIGHT:
            self.kill()

    def megacoin(self):
        if self.random_number == 7:
            self.image = self.images[1]                          #creating a megacoin
        else:
            self.image = self.images[0]
    def ismegacoin(self):
        return self.random_number == 7


P1 = Player()                                                    #assigning a class to a variable
enemies = pg.sprite.Group([Enemy() for _ in range(4)])           #assigning a class to a variable, determining the number of objects
coins = pg.sprite.Group([Coin() for _ in range(6)])              #assigning a class to a variable, determining the number of objects

running = True                                              #variable for loop operation
while running:                                              #start of the cycle
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:                           #when the screen is closed, the cycle stops
            running = False
       
    screen.fill(WHITE)
    screen.blit(pg.transform.scale(road, (WIDTH, HEIGHT)), (0, 0 % HEIGHT))      #stretching an image to fit the screen

    P1.draw()                                       #function call
    P1.move()

    for enemy in enemies:
        enemy.draw()
        enemy.move()
        enemy.kil()

    for coin in coins:
        coin.draw()
        coin.move()
        coin.kil()

    if enemies.__len__() < 4:
        enemies.add(Enemy())                                #creating new objects

    if coins.__len__() < 6:
        coins.add(Coin())

    if pg.sprite.spritecollide(P1, enemies, True):         #conditions for stopping the cycle
        running = False

    for coin in pg.sprite.spritecollide(P1, coins, True):
        score += 1                                          #increasing the number of points
        a.append(1)                                         #counter increasing
        if coin.ismegacoin():
            score += 20


    text = font.render(f'{score}', True, BLACK)            #displaying the number of points on the screen
    screen.blit(text, (750, 20))

    pg.display.update()                                    #updating the screen with changes
pg.quit()                                                  #stopping the code