import pygame as pg

pg.init()
START_X = 0
START_Y = 0
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 400
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (19, 153, 242)
GRAY = (150, 167, 179)
INDIGO = (75, 0, 130)

prev = pg.image.load(
    "/Users/beibarys/Documents/PP2_uhahahahahhaha/lab7/music/mmm1.png"
)
next = pg.image.load(
    "/Users/beibarys/Documents/PP2_uhahahahahhaha/lab7/music/mmm2.png"
)
play = pg.image.load(
    "/Users/beibarys/Documents/PP2_uhahahahahhaha/lab7/music/mmm3.png"
)
pause = pg.image.load(
    "/Users/beibarys/Documents/PP2_uhahahahahhaha/lab7/music/mmm4.png"
)

WIDTH_FONE_MINI = 75
HEIGHT_FONE_MINI = 75
PREV_MINI_ASPECT = 1.09
NEXT_MINI_ASPECT = 0.84
PLAY_MINI_ASPECT = 0.85
PAUSE_MINI_ASPECT = 1.11
HEIGHT_PREV_MINI = HEIGHT_FONE_MINI / PREV_MINI_ASPECT
HEIGHT_NEXT_MINI = HEIGHT_FONE_MINI / NEXT_MINI_ASPECT
HEIGHT_PLAY_MINI = HEIGHT_FONE_MINI / PLAY_MINI_ASPECT
HEIGHT_PAUSE_MINI = HEIGHT_FONE_MINI / PAUSE_MINI_ASPECT
WIDTH_FONE = SCREEN_WIDTH
HEIGHT_FONE = SCREEN_HEIGHT - 100

prev = pg.transform.scale(prev, (WIDTH_FONE_MINI, HEIGHT_FONE_MINI))
next = pg.transform.scale(next, (WIDTH_FONE_MINI, HEIGHT_FONE_MINI))
play = pg.transform.scale(play, (WIDTH_FONE_MINI, HEIGHT_FONE_MINI))
pause = pg.transform.scale(pause, (WIDTH_FONE_MINI, HEIGHT_FONE_MINI))
current_icon = play

FPS = 60
clock = pg.time.Clock()
running = True
screen.fill(GRAY)

ms = [
    "/Users/beibarys/Documents/PP2_uhahahahahhaha/lab7/music/m1.mp3",
    "/Users/beibarys/Documents/PP2_uhahahahahhaha/lab7/music/m2.mp3",
    "/Users/beibarys/Documents/PP2_uhahahahahhaha/lab7/music/m3.mp3",
]
current_track = 0

def play_music(current_track=0):
    pg.mixer.music.load(ms[current_track])
    pg.mixer.music.play()

def change_icon(current_track):
    global current_icon
    if current_icon == play:
        current_icon = pause
        play_music(current_track)
    elif current_icon == pause:
        current_icon = play
        pg.mixer.music.stop()

while running:
    screen.fill(GRAY)

    next_rect = next.get_rect()
    next_rect.left = SCREEN_WIDTH / 2 - WIDTH_FONE_MINI / 2 + 80
    next_rect.top = (SCREEN_HEIGHT / 2 + 150) - HEIGHT_NEXT_MINI / 2
    prev_rect = prev.get_rect()
    prev_rect.left = SCREEN_WIDTH / 2 - WIDTH_FONE_MINI / 2 - 80
    prev_rect.top = (SCREEN_HEIGHT / 2 + 150) - HEIGHT_NEXT_MINI / 2
    play_rect = play.get_rect()
    current_icon_rect = current_icon.get_rect(topleft = (SCREEN_WIDTH / 2 - WIDTH_FONE_MINI / 2 , (SCREEN_HEIGHT / 2 + 150) - HEIGHT_NEXT_MINI / 2))

    screen.blit(current_icon, current_icon_rect)
    screen.blit(next, next_rect)
    screen.blit(prev, prev_rect)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if next_rect.collidepoint(pg.mouse.get_pos()):
                current_track = (current_track + 1) % len(ms)
            if prev_rect.collidepoint(pg.mouse.get_pos()):
                current_track = (current_track - 1) % len(ms)
                if current_track >= 0:
                    current_track = (current_track - 1) % len(ms)
                else:
                    current_track = 3
                    current_track = (current_track - 1) % len(ms)
            if current_icon_rect.collidepoint(pg.mouse.get_pos()):
                change_icon(current_track)

    pressed = pg.key.get_pressed()
    if pressed[pg.K_y]:
        current_track = 0
        play_music(current_track)
    if pressed[pg.K_t]:
        current_track = 1
        play_music(current_track)
    if pressed[pg.K_r]:
        current_track = 2
        play_music(current_track)
    if pressed[pg.K_LEFT]:
        current_track = (current_track - 1) % len(ms)
        if current_track >= 0:
            current_track = (current_track - 1) % len(ms)
            play_music(current_track)
        else:
            current_track = 3
            current_track = (current_track - 1) % len(ms)
    if pressed[pg.K_RIGHT]:
        current_track = (current_track + 1) % len(ms)
        play_music(current_track)
    if pressed[pg.K_SPACE]:
        pg.mixer.music.stop()

    pg.display.flip()
    clock.tick(FPS)