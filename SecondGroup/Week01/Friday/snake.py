import pygame
from random import randrange


size = width, height = 1050, 650
block = 50

x, y = randrange(0, width, block), randrange(0, height, block)
apple = randrange(0, width, block), randrange(0, height, block)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
score = 0
snake = [(x, y)]
dx, dy = 0, 0
fps = 10

pygame.init()
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_menu = pygame.font.Font('font.ttf', 85)    
game_background = pygame.image.load('game_background.jpg').convert()
menu_background = pygame.image.load('menu_background.jpg').convert()
gamemenu = pygame.mixer.Sound("gamemenu.mp3")


def Player1():
    while True:
        screen.fill(pygame.Color('purple'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.flip()


def main_menu():
    # gamemenu.play()
    menu = True
    while menu:
        screen.blit(menu_background, (0, 0))
        
        # menu text
        render_menu = font_menu.render('CLICK', True, pygame.Color('black'))
        screen.blit(render_menu, (430, 550))

        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mx, my)

            if event.type == pygame.MOUSEBUTTONDOWN and 430 <= mx <= 550 and 570 <= my <= 600:
                menu = False

        pygame.display.flip()

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]: # K_RETURN - нажатие на Enter
            # gamemenu.stop()
            break
        if key[pygame.K_SPACE]:
            Player1()

main_menu()


while True:
    screen.blit(game_background, (0, 0))

    # drawing snake, apple
    for i, j in snake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, block - 1, block - 1))
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, block, block))

    # show score
    render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))    

    # snake movement
    x += dx * block
    y += dy * block
    snake.append((x, y))
    snake = snake[-length:]

    # game over
    if x < -block or x > width or y < -block or y > height or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', True, pygame.Color('orange'))
            screen.blit(render_end, (335, 300))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    # eating apple
    if snake[-1] == apple:
        apple = randrange(0, width, block), randrange(0, height, block)
        length += 1
        score += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(fps)

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}

