# Объявление переменных
# шрифт с размером fontsize и со скачанным шрифтом fontname
font = pygame.font.Font('fontname.ttf', fontsize)

# шрифт с размером fontsize и с шрифтом fontname
# bold=True - жирный шрифт
font = pygame.font.SysFont('fontname', fontsize, bold=True)

# Открываем рисунок filename.jpg
img = pygame.image.load('filename.jpg').convert()

# Открываем звук с названием 'soundname.mp3'
music = pygame.mixer.Sound('soundname.mp3')
music.play() # - включение звука
music.stop() # - отключение звука

# нажатия мышкой
for event in pygame.event.get():
    mx, my = pygame.mouse.get_pos()

    if event.type == pygame.QUIT:
        exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        print(mx, my)

    if event.type == pygame.MOUSEBUTTONDOWN and 430 <= mx <= 550 and 570 <= my <= 600:
        menu = False
