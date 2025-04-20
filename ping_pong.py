from pygame import*


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < HEIGHT - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < HEIGHT - 150:
            self.rect.y += self.speed


WIDTH = 600
HEIGHT = 500
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('ping pong')
background = transform.scale(image.load('back.jpg'), (WIDTH, HEIGHT))


game = True
finish = False

clock = time.Clock()
FPS = 120


raketka1 = Player('raketka.png', 5, 200, 50, 80, 10)
raketka2 = Player('raketka.png', 550, 200, 50, 150, 4)
ball = GameSprite('ball.png', 200, 200, 50, 50, 4)


font.init()
font = font.Font(None, 35)
lose1 = font.render('fndjfbbsbf', True, (180, 0, 0))
lose2 = font.render('frgfwrehytegre', True, (180, 0, 0))


speed_x = 3
speed_y = 3


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if finish != True:
            window.blit(background, (0,0))


            ball.rect.x += speed_x
            ball.rect.y += speed_y


            raketka1.update_l()
            raketka2.update_r()


            if sprite.collide_rect(raketka1, ball) or sprite.collide_rect(raketka2, ball):
                speed_x *= -1


            if ball.rect.y > HEIGHT - 50 or ball.rect.y < 0:
                speed_y *= -1


            if ball.rect.x > WIDTH:
                finish = True
                window.blit(lose2, (100, 200))


            if ball.rect.x < WIDTH:
                finish = True
                window.blit(lose1, (100, 200))



            raketka1.reset()
            raketka2.reset()
            ball.reset()
    
    
    
    
    
    
    
    
    
    
    
    display.update()
    clock.tick(FPS)