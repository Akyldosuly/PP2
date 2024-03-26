import pygame as pg
import datetime as dt

pg.init()
START_X = 0
START_Y = 0
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pg.SCALED, vsync=1)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (19, 153, 242)

FPS = 60
clock = pg.time.Clock()

bg = pg.image.load(
    """/Users/beibarys/Documents/PP2_uhahahahahhaha/lab7/clock/mickey-clock.jpg"""
)
WIDTH_X_BG = 500
HEIGHT_Y_BG = 500
CENTER_X_POS = SCREEN_WIDTH / 2 - WIDTH_X_BG / 2
CENTER_Y_POS = SCREEN_HEIGHT / 2 - HEIGHT_Y_BG / 2

big_arrow = pg.image.load(
    "/Users/beibarys/Documents/PP2_uhahahahahhaha/lab7/clock/big-arrow.png"
)
BIG_ARROW_WIDTH = 35
BIG_ARROW_ASPECT_RATIO = 0.13
BIG_ARROW_HEIGHT = BIG_ARROW_WIDTH / BIG_ARROW_ASPECT_RATIO
big_arrow = pg.transform.scale(big_arrow, (BIG_ARROW_WIDTH, BIG_ARROW_HEIGHT))

big_arrow_rect = big_arrow.get_rect()
big_arrow_rect.center = CENTER

small_arrow = pg.image.load(
    "/Users/beibarys/Documents/PP2_uhahahahahhaha/lab7/clock/small-arrow.png"
)
SMALL_ARROW_WIDTH = 35
SMALL_ARROW_ASPECT_RATIO = 0.305
SMALL_ARROW_HEIGHT = SMALL_ARROW_WIDTH / SMALL_ARROW_ASPECT_RATIO
small_arrow = pg.transform.scale(small_arrow, (SMALL_ARROW_WIDTH, SMALL_ARROW_HEIGHT))

small_arrow_rect = small_arrow.get_rect()
small_arrow_rect.center = CENTER


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    angle_second = dt.datetime.now().second * (-6)
    angel_minute = dt.datetime.now().minute * (-6)
    screen.fill(BLACK)
    screen.blit(bg, (CENTER_X_POS, CENTER_Y_POS))
    rotated_big_arrow = pg.transform.rotate(big_arrow, angle_second)
    rotated_big_arrow_rect = rotated_big_arrow.get_rect()
    rotated_big_arrow_rect.center = big_arrow_rect.center
    screen.blit(rotated_big_arrow, rotated_big_arrow_rect)
    rotated_small_arrow = pg.transform.rotate(small_arrow, angel_minute)
    rotated_small_arrow_rect = rotated_small_arrow.get_rect()
    rotated_small_arrow_rect.center = small_arrow_rect.center
    screen.blit(rotated_small_arrow, rotated_small_arrow_rect)

    pg.display.flip()
    clock.tick(FPS)