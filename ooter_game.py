from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, png, x, y, speed):
        super().__init__()
        self.png = png
        self.x = x
        self.y = y
        self.speed = speed
        self.image = transform.scale(image.load(self.png), (60, 60))
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
        pass


class Enemy(GameSprite):
    def update(self):
        if self.rect.y < 427:
            self.rect.y += 1

player = Player('rocket.png', 330, 427, 6)


w = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load('Black_Hole.jpg'), (700, 500))








game = True
finish = False

fps = 60
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    key_pressed = key.get_pressed()
    if finish != True:
        w.blit(background, (0, 0))
        player.reset()
        player.update()
        display.update()
        clock.tick(fps)