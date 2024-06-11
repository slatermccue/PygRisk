import pygame as pg

screen = pg.display.set_mode((800, 600))

class Blob:
    def __init__(self):
        self.image = pg.image.load('blob.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect(center=(100, 300))
        self.mask = pg.mask.from_surface(self.image)

running = True

blob = Blob()

red = (255,0,0)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pos = pg.mouse.get_pos()
    pos_in_mask = pos[0] - blob.rect.x, pos[1] - blob.rect.y
    touching = blob.rect.collidepoint(*pos) and blob.mask.get_at(pos_in_mask)

    screen.fill(red if touching else pg.Color('green'))
    screen.blit(blob.image, blob.rect)
    pg.display.update()

