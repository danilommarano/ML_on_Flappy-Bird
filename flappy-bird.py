import os
import random
import pygame as pg
import neat
import time

WIDTH = 600
HEIGHT = 800

# ──────────────────────────────── Load Images ─────────────────────────────── #
BIRD_IMGS =[pg.transform.scale2x(pg.image.load(os.path.join("imgs", "bird1.png"))),
            pg.transform.scale2x(pg.image.load(os.path.join("imgs", "bird2.png"))),
            pg.transform.scale2x(pg.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pg.transform.scale2x(pg.image.load(os.path.join("imgs", "pipe.png")))
FLOOR_IMG = pg.transform.scale2x(pg.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pg.transform.scale2x(pg.image.load(os.path.join("imgs", "bg.png")))

# ──────────────────────────── Object of the Bird ──────────────────────────── #
class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2
