import pygame as pg

screen = pg.display.set_mode((800, 600))

class Blob:
    def __init__(self, centerPoint, bgColor):
        self.image = pg.image.load('blob.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect(center=centerPoint)
        self.mask = pg.mask.from_surface(self.image)
        self.bgColor = bgColor

running = True

white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)

blob = Blob((100,300), blue)
blob2 = Blob((400,300), red)

allBlobs = [blob, blob2]

while running:
    screen.fill(white)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pos = pg.mouse.get_pos()
    for entity in allBlobs:
        pos_in_mask = pos[0] - entity.rect.x, pos[1] - entity.rect.y
        touching = entity.rect.collidepoint(*pos) and entity.mask.get_at(pos_in_mask)

        if (touching):
            screen.fill(entity.bgColor)
    

    screen.blit(blob.image, blob.rect)
    screen.blit(blob2.image, blob2.rect)
    pg.display.update()

