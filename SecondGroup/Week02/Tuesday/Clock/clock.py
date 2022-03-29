import pygame
import datetime
from math import sin, cos, pi


size = 800
center = size / 2, size / 2
clockRadius = 400
fps = 60
digits = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    11: 'XI',
    12: 'XII'
}


pygame.init()
screen = pygame.display.set_mode([size, size])
pygame.display.set_caption('Analog Clock')
clock = pygame.time.Clock()
mickey = pygame.image.load('mickey.png')
leftHand = pygame.transform.scale(pygame.image.load('left hand.png'), (770 // 2, 230 // 2))
rightHand = pygame.transform.scale(pygame.image.load('right hand.png'), (594 // 2, 322 // 2))

def numbers(number, number_size, position):
    font = pygame.font.SysFont('Arial', number_size, bold=True)
    text = font.render(number, True, pygame.Color('black'))
    text_rect = text.get_rect(center=(position))
    screen.blit(text, text_rect)


def polar_to_cartesian(r, theta):
    x, y = r * sin(pi * theta / 180), r * cos(pi * theta / 180)
    return x + size / 2, -(y - size / 2)


def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0]- originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset_center_to_pivot.rotate(angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # drawing
    screen.fill(pygame.Color('white'))
    pygame.draw.circle(screen, pygame.Color('black'), center, clockRadius - 10, 10)
    pygame.draw.circle(screen, pygame.Color('gray'), center, clockRadius - 20)
    pygame.draw.circle(screen, pygame.Color('black'), center, 10)
    [numbers(digits[i], 80, polar_to_cartesian(clockRadius - 80, i * 30)) for i in range(1, 13)]
    for number in range(0, 360, 6):
        if number % 5 != 0:
            pygame.draw.line(screen, pygame.Color('black'), polar_to_cartesian(clockRadius - 15, number), polar_to_cartesian(clockRadius - 30, number), 2)
        else:
            pygame.draw.line(screen, pygame.Color('black'), polar_to_cartesian(clockRadius - 15, number), polar_to_cartesian(clockRadius - 30, number), 6)
    screen.blit(mickey, (95, 130))

    # time
    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute

    # minute
    theta = (minute + second / 60) * (360 / 60)
    blitRotate(screen, rightHand, center, (rightHand.get_width() / 2 + 110, leftHand.get_height() / 2 + 75), theta + 75)

    # second
    theta = second * (360 / 60)
    blitRotate(screen, leftHand, center, (leftHand.get_width() / 2 - 145, leftHand.get_height() / 2), theta - 87)


    # display
    pygame.display.flip()
    clock.tick(fps)