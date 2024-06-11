import pygame as pg

screen = pg.display.set_mode((800, 600))

class Blob:
    def __init__(self, centerPoint):
        self.image = pg.image.load('blob.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect(center=centerPoint)
        self.mask = pg.mask.from_surface(self.image)

running = True

blob = Blob((100,300))
blob2 = Blob((400,300))

white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)

while running:
    screen.fill(white)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pos = pg.mouse.get_pos()
    pos_in_mask = pos[0] - blob.rect.x, pos[1] - blob.rect.y
    pos2_in_mask = pos[0] - blob2.rect.x, pos[1] - blob2.rect.y
    touching = blob.rect.collidepoint(*pos) and blob.mask.get_at(pos_in_mask)
    touching2 = blob2.rect.collidepoint(*pos) and blob2.mask.get_at(pos2_in_mask)

    if (touching):
        screen.fill(red)
    if (touching2):
        screen.fill(blue)

    screen.blit(blob.image, blob.rect)
    screen.blit(blob2.image, blob2.rect)
    pg.display.update()

