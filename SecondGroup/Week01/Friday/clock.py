import pygame
from math import pi, cos, sin
import datetime


width, height = 800, 800
center = width / 2, height / 2
clock_radius = 400

pygame.init()
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Analog Clock')
clock = pygame.time.Clock()
fps = 60


def numbers(number, number_size, position):
    font = pygame.font.SysFont('Arial', number_size, bold=True)
    text = font.render(number, True, pygame.Color('white'))
    text_rect = text.get_rect(center=(position))
    screen.blit(text, text_rect)


def polar_to_cartesian(r, theta):
    x, y = r * sin(pi * theta / 180), r * cos(pi * theta / 180)
    return x + width / 2, -(y - height / 2)


def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour


        screen.fill(pygame.Color('black'))
        pygame.draw.circle(screen, pygame.Color('white'), center, clock_radius - 10, 10)
        pygame.draw.circle(screen, pygame.Color('white'), center, 12)

        for number in range(1, 13):
            numbers(str(number), 80, polar_to_cartesian(clock_radius - 80, number * 30))

        # second
        r = clock_radius - 60
        theta = second * (360 / 60)
        pygame.draw.line(screen, pygame.Color('red'), center, polar_to_cartesian(r, theta), 4)

        # minute
        r = clock_radius - 120
        theta = (minute + second / 60) * (360 / 60)
        pygame.draw.line(screen, pygame.Color('white'), center, polar_to_cartesian(r, theta), 10)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

main()