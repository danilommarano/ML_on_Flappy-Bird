import os
import random
import pygame as pg
import neat
import time

WIDTH = 600
HEIGHT = 800

# ─────────────────────────────── Load Images ─────────────────────────────── #
BIRD_IMGS =[pg.transform.scale2x(pg.image.load(os.path.join("imgs", "bird1.png"))),
            pg.transform.scale2x(pg.image.load(os.path.join("imgs", "bird2.png"))),
            pg.transform.scale2x(pg.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pg.transform.scale2x(pg.image.load(os.path.join("imgs", "pipe.png")))
FLOOR_IMG = pg.transform.scale2x(pg.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pg.transform.scale2x(pg.image.load(os.path.join("imgs", "bg.png")))
