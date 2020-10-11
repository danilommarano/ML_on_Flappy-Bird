import os
import random
import pygame as pg
import neat
import time

WIDTH = 550
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

        # ─ Physics for the movementation ─ #
        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2

        if d >= 16:
            d = d/abs(d) * 16

        elif d < 0:
            d -= 2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1

        # ─ Set the correct bir image base on the animation time ─ #
        if self.img_count <self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[1]
            self.img_count = 0
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        # ─ Rotate bird image ─ #
        rotated_image = pg.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(
            center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pg.mask.form_surface(self.img)



def draw_window(win,bird):
    win.blit(BG_IMG, (0,0))
    bird.draw(win)
    pg.display.update()

def main():
    bird = Bird(200, 200)
    run = True
    win = pg.display.set_mode((WIDTH, HEIGHT))

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = FALSE

        bird.move()
        draw_window(win, bird)

    pg.quit()
    quit()

main()
