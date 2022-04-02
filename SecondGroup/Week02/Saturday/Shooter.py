import pygame

# variables
WIDTH, HEIGHT = 800, 640
FPS = 60

# moving
moving_left = False
moving_right = False

# init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BG = (144, 201, 120)


class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed, person):
        pygame.sprite.Sprite.__init__(self)
        self.flip = False
        self.direction = 1
        self.speed = speed
        self.animation = []
        self.frameIndex = 0
        self.updateTime = pygame.time.get_ticks()
        for i in range(5):
            img = pygame.image.load(f'img/{person}/Idle/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.animation.append(img)
        self.image = self.animation[self.frameIndex]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def move(self, moving_left, moving_right):
        dx, dy = 0, 0
       
        if moving_left:
            dx = -self.speed
            self.direction = -1
            self.flip = True
        if moving_right:
            dx = self.speed
            self.direction = 1
            self.flip = False

        self.rect.x += dx
        self.rect.y += dy

    def updateAnimation(self):
        cooldown = 100
        self.image = self.animation[self.frameIndex]
        if pygame.time.get_ticks() - self.updateTime > cooldown:
            self.frameIndex += 1
            self.updateTime = pygame.time.get_ticks()

        if self.frameIndex >= len(self.animation):
            self.frameIndex = 0

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


Player = Soldier(200, 200, 3, 5, 'player')

while True:

    # draw
    screen.fill(BG)
    Player.draw()
    Player.updateAnimation()
    Player.move(moving_left, moving_right)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False

    # display
    pygame.display.flip()
    clock.tick(FPS)

# 1. -Создание окна
# 2. -Создание класса солдата
# 3. -Создание метода draw
# 4. -Движение игрока в игре
# 5. -Создание класса move
# 6. -Направление спрайта
# 7. -Анимация
