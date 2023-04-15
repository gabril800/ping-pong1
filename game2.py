RED = (255, 0, 0)
GREEN = (0, 255, 51)
BlUE = (200, 255, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (200, 255, 255)

import pygame
from random import randint
from time import time
pygame.init()
class Area():
    def __init__(self,x,y,width,height,fill_color):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = fill_color
    def change_color(self,new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(scene,self.fill_color,self.rect)
    def draw_frame(self,frame_color,frame_width):
        pygame.draw.rect(window,frame_color,self.rect,frame_width)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
    def colliderect(self,sprite):
        return self.rect.colliderect(sprite.rect)
class Label(Area):
    def set_text(self,font_size,text,text_color):
        self.image = pygame.font.SysFont('Times New Roman',font_size).render(text,True,text_color)
    def draw(self,shiftx,shifty):
        self.fill()
        scene.blit(self.image,(self.rect.x+shiftx,self.rect.y+shifty))

class Picture(Area):
    def __init__(self,filename,x,y,width,height,fill_color):
        super().__init__(x,y,width,height,fill_color)
        self.image = pygame.image.load(filename)
    def draw(self):
        scene.blit(self.image,(self.rect.x,self.rect.y))
scene = pygame.display.set_mode((500,500))
scene.fill(BlUE)
clock = pygame.time.Clock()
platform = Picture('сосиска.png',200,330,100,46,BlUE)
ball = Picture('кот.png',150,200,50,57,BlUE)
mx = 5
my = 5
n = 9
#что-то
game_over = False
move_down = False
move_up = False
dx = 3
dy = 3
while not game_over:
    platform.fill()
    ball.fill()
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_UP:
                move_up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_UP:
                move_up = False
    if move_down:
        platform.rect.y += 4
    if move_up:
        platform.rect.y -= 4
    if platform.rect.y <0:
        platform.rect.y +=4
    if platform.rect.y > 400:
        platform.rect.y -=4
    ball.rect.x += dx
    ball.rect.y += dy

    if ball.colliderect(platform):
        dy *= -1
    if ball.rect.y <0 or ball.rect.y >450:
        dx*= -1
    if ball.rect.y <0:
        dy*= -1

    platform.draw()
    ball.draw()
    clock.tick(40)
    pygame.display.update()
pygame.display.update()

