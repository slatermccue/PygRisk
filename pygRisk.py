import pygame as pg

screen = pg.display.set_mode((800, 600))

class Country:
    def __init__(self, imageName, name):
        self.imageNormal = pg.image.load('country'+imageName+'.png')
        #self.imageAttack = pg.image.load('attackingCountry'+imageName+'.png')
        #self.imageDefend = pg.image.load('defendingCountry'+imageName+'.png')
        self.imageHover = pg.image.load('hoverCountry'+imageName+'.png')
        self.rect = self.imageNormal.get_rect()
        self.mask = pg.mask.from_surface(self.imageNormal)
        self.status = "normal" # hover; attacking; defending
        self.image = self.imageNormal
        self.name = name

    def setStatus(self, status):
        self.status = status
    
    def draw(self):
        if (self.status == "normal"):
            self.image = self.imageNormal
        if (self.status == "hover"):
            self.image = self.imageHover
        if (self.status == "attacking"):
            self.image = self.imageAttack
        if (self.status == "defending"):
            self.image = self.imageDefend
        screen.blit(self.image, (0,0))


leftSideIndex = pg.image.load('LeftSideList.png')
rightSideIndex = pg.image.load('RightSideList.png')
swordImg = pg.image.load('mouseTest.png')
swordCursor = pg.cursors.Cursor((0,0), swordImg)
pg.mouse.set_cursor(swordCursor)
running = True

white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)

mikem = Country('MikemCcu', 'mikemccu')
hollyh = Country('HolLyh', 'hollyh')
jenniferg = Country('Jenniferg', 'jenniferg')
paulce = Country('Paulce', 'paulce')
allCountries = [mikem,hollyh,jenniferg,paulce]
background = pg.image.load("mapBackground.png")

countryMikemIl = pg.image.load("countryMikemIl.png")
countryPame = pg.image.load("countryPame.png")
countryTreNeeu = pg.image.load("countryTreNeeu.png")
countryHolLye = pg.image.load("countryHolLye.png")
countryJesUsri = pg.image.load("countryJesUsri.png")
countryLap = pg.image.load("countryLap.png")

while running:
    screen.fill(white)
    screen.blit(background, (0,0))
    for country in allCountries:
        country.draw()
    screen.blit(countryHolLye, (0,0))
    screen.blit(countryJesUsri, (0,0))
    screen.blit(countryLap, (0,0))
    screen.blit(countryMikemIl, (0,0))
    screen.blit(countryPame, (0,0))
    screen.blit(countryTreNeeu, (0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pos = pg.mouse.get_pos()

    for country in allCountries:
        pos_in_mask = pos[0] - country.rect.x, pos[1] - country.rect.y
        touching = country.rect.collidepoint(*pos) and country.mask.get_at(pos_in_mask)
    
        if (touching):
            country.setStatus('hover')
        else:
            country.setStatus('normal')
    

    #card testing below...
    #screen.blit(leftSideIndex, (50,50))
    #screen.blit(rightSideIndex, (160,50))
    pg.display.update()

