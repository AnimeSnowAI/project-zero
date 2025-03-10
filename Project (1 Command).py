from pygame import *
from random import randint

class GameSprite(sprite.Spite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 650:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += randint(1,5)
        if self.rect.y > 500:
            self.rect.x = randint(80,600)
            self.rect.y = 0
            
window = display.set_mode((800,600))
display.set_caption("Project Zero")
background = transform.scale(image.load("background.png"),(800,600))
font = font.SysFont('Arial', 80)
pobeda = font.render('Ви виграли, дякуємо за гру!', True, (255, 255, 255))
proigrish = font.render('Нажаль, ви не змогли пройти гру...', True, (180, 0, 0))

PlayerX1 = Player("Player.png", 200,350,50,50,30)
Enemy1 = Enemy("Enemy1.png", randint(80,600), randint(-100,0), 50, randint(1,6)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        if sprite.spritecollide(PlayerX1, Enemy1, False):
            finish = True
            window.blit(proigrish, (200,200))
    display.update()
    
