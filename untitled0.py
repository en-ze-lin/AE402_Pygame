import pygame, random, math
class Ball(pygame.sprite.Sprite):
    dx = 0
    dy = 0
    x = 0
    y = 0
    def __init__(self, speed, srx, sry, radium, color):
        pygame.sprite.Sprite.__init__(self)
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([radium * 2, radium * 2])
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, color, (radium, radium), radium, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (srx, sry)
        direction = random.randint(20, 70)
        radian = math.radians(direction)
        self.dx = speed * math.cos(radian)
        self.dy = -speed * math.sin(radian)
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y
        if (self.rect.left <= 0 or self.rect.right >= screen.get_width()):
            self.dx *= -1
        elif(self.rect.top <= 5 or self.rect.bottom >= screen.get_height() - 5):
            self.dy *= -1
    def collide(self):
        self.dx *= -1
        self.dy *= -1
pygame.init()
screen = pygame.display.set_mode((400, 300))
screen_width = 400
screen_height = 300
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))
screen = pygame.display.set_mode([screen_width, screen_height])
alllist = pygame.sprite.Group()
ball1 = Ball(8, 100, 100, 10, (0, 0, 255))
alllist.add(ball1)
ball2 = Ball(6, 200, 250, 10, (255, 0, 0))
alllist.add(ball2)
done = False
clock = pygame.time.Clock()
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0, 0))
    ball1.update()
    ball2.update()
    alllist.draw(screen)
    result = pygame.sprite.collide_rect(ball1, ball2)
    if result == True:
        ball1.collide()
        ball2.collide()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()