import pygame
import os

size = (1024 // 2, 614 // 2)
fps = 60
musics = []
left, right, mid = False, False, False
played = 0

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Player MP3')
playerIcon = pygame.transform.scale(pygame.image.load('player_mp3.jpg'), size)

for i in os.listdir('C:\\Users\\wupsi\\Desktop\\Folders\\Courses\\PP2_COURSE\\SecondGroup\\Week02\\Tuesday\\Player\\The Weeknd - Starboy'):
    music = pygame.mixer.Sound('C:\\Users\\wupsi\\Desktop\\Folders\\Courses\\PP2_COURSE\\SecondGroup\\Week02\\Tuesday\\Player\\The Weeknd - Starboy\\' + str(i))
    musics.append(music)

musics[played].play()
while True:
    for event in pygame.event.get():
        mx, my = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and 30 <= mx <= 165 and 105 <= my <= 190:
            left = True
        if event.type == pygame.MOUSEBUTTONDOWN and 230 <= mx <= 275 and 105 <= my <= 190:
            mid = True
        if event.type == pygame.MOUSEBUTTONDOWN and 340 <= mx <= 480 and 105 <= my <= 190:
            right = True
        
    # drawing
    screen.blit(playerIcon, (0, 0))

    # pressing
    if left:
        musics[played].stop()
        played -= 1
        if played <= -1:
            played = 17
        musics[played].play()
        left = False
    
    if right:
        musics[played].stop()
        played += 1
        if played >= 18:
            played = 0
        musics[played].play()
        right = False

    if mid:
        if not pygame.mixer.pause():
            pygame.mixer.pause()
        else:
            pygame.mixer.unpause()
        mid = False


    # display
    pygame.display.flip()
    clock.tick(fps)

# <
# x = 30 - 165 
# y = 105 - 190

# | |
# x = 230 - 275
# y = 105 - 190

# >
# x = 340 - 480
# y = 105 - 190
