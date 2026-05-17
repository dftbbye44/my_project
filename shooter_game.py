from pygame import *
from random import randint
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)




class GameSprite(sprite.Sprite):
    def __init__(self, png, x, y, speed):
        super().__init__()
        self.png = png
        self.x = x
        self.y = y
        self.speed = speed
        self.image = transform.scale(image.load(resource_path(self.png)), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        w.blit(self.image, (self.rect.x, self.rect.y))
    def restart(self):
        w.blit(self.image, (self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y


class Player(GameSprite):
    def update(self):
        if key_pressed[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if key_pressed[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed
    def fire(self):
        for bullet in range(3):
            bullets.add(Bullet('assets/bullet.png', player.rect.centerx, player.rect.top, 5))


class Enemy(GameSprite):
    def update(self):
        if self.rect.y < 427:
            self.rect.y += self.speed
        if self.rect.y >= 427:
            self.rect.y = 0
            self.rect.x = randint(60, 640)
            self.speed = randint(1, 2)

class Bullet(GameSprite):
    def update(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed 




player = Player('assets/rocket.png', 330, 427, 6)


w = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load(resource_path('assets/Black_Hole.jpg')), (700, 500))

bullets = sprite.Group()
monsters = sprite.Group()

for monster in range(5):
    monsters.add(Enemy('assets/ufo.png', randint(60,640), randint(10,40), randint(1,2)))

game = True
finish = False

fps = 60
clock = time.Clock()

while game:
    key_pressed = key.get_pressed()
    if finish != True:
        w.blit(background, (0, 0))
        monsters.draw(w)
        for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == KEYUP:
                if e.key == K_q:
                    player.fire()
        bullets.draw(w)
        bullets.update()
        monsters.update()
        player.reset()
        player.update()
    display.update()
    clock.tick(fps)