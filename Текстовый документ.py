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
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(loops=-1)
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
scene.fill(LIGHT_RED)
clock = pygame.time.Clock()
platform = Picture('сосиска.png',450,450,50,100,BlUE)
platform2 = Picture('сосиска — копия.png',0,0,50,100,BlUE)
ball = Picture('кот.png',150,200,50,57,BlUE)
button_s = Picture('start_button.png',200,200,25,25,WHITE)
button_b = Picture('button-ball.png',10,10,25,25,WHITE)
button_skins = Picture('skins_button.png',190,10,25,25,WHITE)
balls_menu = Picture('меню_котиков.png',0,0,0,0,WHITE)
skins_menu = Picture('скины.png',0,0,0,0,WHITE)
mx = 5
my = 5
n = 9
#что-то
game_over = False
move_down = False
move_up = False
move_down2 = False
move_up2 = False
start = False
dx = 3
dy = 3
balls = False
skins = False
button_s.fill()
button_s.draw()
button_b.fill()
button_b.draw()
button_skins.fill()
button_skins.draw()
pygame.display.update()
while not game_over:
    for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if balls == False and skins == False and event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 200 and event.pos[1] > 200 and event.pos[0] < 300 and event.pos[1] < 300:
                if event.button == 1:  #  левая кнопка мыши
                    start = True
            if start == False and skins == False and event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 10 and event.pos[1] > 25 and event.pos[0] < 159 and event.pos[1] < 131:
                if event.button == 1:  #  левая кнопка мыши
                    balls = True
            if start == False and balls == False and event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 190 and event.pos[1] > 10 and event.pos[0] < 155+190 and event.pos[1] < 115:
                if event.button == 1:  #  левая кнопка мыши
                    skins = True
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if balls and event.key == pygame.K_0:
                    balls = False
                    scene.fill(LIGHT_RED)
                    button_s.fill()
                    button_s.draw()
                    button_b.fill()
                    button_b.draw()
                    button_skins.fill()
                    button_skins.draw()
                if skins and event.key == pygame.K_0:
                    skins = False
                    scene.fill(LIGHT_RED)
                    button_s.fill()
                    button_s.draw()
                    button_b.fill()
                    button_b.draw()
                    button_skins.fill()
                    button_skins.draw()
                if balls and event.key == pygame.K_1:
                    ball = Picture('кот.png',150,200,50,57,BlUE)
                if balls and event.key == pygame.K_2:
                    ball = Picture('кот2.png',150,200,50,57,BlUE)
                if balls and event.key == pygame.K_3:
                    ball = Picture('кот3.png',150,200,50,57,BlUE)
                if skins and event.key == pygame.K_1:
                    platform = Picture('сосиска.png',450,450,50,100,BlUE)
                    platform2 = Picture('сосиска — копия.png',0,0,50,100,BlUE)
                if skins and event.key == pygame.K_2:
                    platform = Picture('веник.png',450,450,50,100,BlUE)
                    platform2 = Picture('веник.png',0,0,50,100,BlUE)
                if skins and event.key == pygame.K_3:
                    platform = Picture('лапка.png',450,450,50,100,BlUE)
                    platform2 = Picture('лапка.png',0,0,50,100,BlUE)
                if event.key == pygame.K_DOWN:
                    move_down = True
                if event.key == pygame.K_UP:
                    move_up = True
                if event.key == pygame.K_s:
                    move_down2 = True
                if event.key == pygame.K_w:
                    move_up2 = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    move_down = False
                if event.key == pygame.K_UP:
                    move_up = False
                if event.key == pygame.K_s:
                    move_down2 = False
                if event.key == pygame.K_w:
                    move_up2 = False
    if start:
        
        scene.fill(BlUE)
        platform.fill()
        platform2.fill()
        ball.fill()
            
        if move_down:
            platform.rect.y += 4
        if move_up:
            platform.rect.y -= 4
        if platform.rect.y < 0:
            platform.rect.y += 4
        if platform.rect.y > 400:
            platform.rect.y -= 4

        if move_down2:
            platform2.rect.y -= -4
        if move_up2:
            platform2.rect.y += -4
        if platform2.rect.y <0:
            platform2.rect.y += 4
        if platform2.rect.y > 400:
            platform2.rect.y -=4
        ball.rect.x += dx
        ball.rect.y += dy

        if ball.colliderect(platform):
            dx *= -1
            ball.rect.x -= 2
        if ball.colliderect(platform2):
            dx *= -1
            ball.rect.x += 2
        if ball.rect.y < 0 or ball.rect.y > 450:
            dy*= -1
        if ball.rect.x<0:
            platform = Picture('сосиска.png',450,450,50,100,BlUE)
            platform2 = Picture('сосиска — копия.png',0,0,50,100,BlUE)
            ball = Picture('кот.png',150,200,50,57,BlUE)
            scene.fill(BlUE)
            scene.blit(pygame.font.SysFont(None, 70).render('Player 1 lose!', True, RED),(100,160))
            scene.blit(pygame.font.SysFont(None, 60).render('restarting game...', True, RED),(100,220))
            pygame.display.update()
            pygame.time.delay(3000)
            scene.fill(LIGHT_RED)
            button_s.fill()
            button_s.draw()
            button_b.fill()
            button_b.draw()
            button_skins.fill()
            button_skins.draw()
            start = False
        if ball.rect.x>500:
            platform = Picture('сосиска.png',450,450,50,100,BlUE)
            platform2 = Picture('сосиска — копия.png',0,0,50,100,BlUE)
            ball = Picture('кот.png',150,200,50,57,BlUE)
            scene.fill(BlUE)
            scene.blit(pygame.font.SysFont(None, 70).render('Player 2 lose!', True, RED),(100,160))
            scene.blit(pygame.font.SysFont(None, 60).render('restarting game...', True, RED),(100,220))
            pygame.display.update()
            pygame.time.delay(3000)
            scene.fill(LIGHT_RED)
            button_s.fill()
            button_s.draw()
            button_b.fill()
            button_b.draw()
            button_skins.fill()
            button_skins.draw()
            start = False    
            
        if start:
            platform.draw()
            platform2.draw()
            ball.draw()
        clock.tick(40)
    if balls:
        balls_menu.fill()
        balls_menu.draw()
    if skins:
        skins_menu.fill()
        skins_menu.draw()
    pygame.display.update()
pygame.display.update()
