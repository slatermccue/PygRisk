import pygame as pg

screen = pg.display.set_mode((800, 600))

class Blob:
    def __init__(self, centerPoint, bgColor):
        self.image = pg.image.load('blob.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect(center=centerPoint)
        self.mask = pg.mask.from_surface(self.image)
        self.bgColor = bgColor

class Country:
    def __init__(self, imageName):
        self.imageNormal = pg.image.load('country'+imageName+'.png')
        #self.imageAttack = pg.image.load('attackingCountry'+imageName+'.png')
        #self.imageDefend = pg.image.load('defendingCountry'+imageName+'.png')
        self.imageHover = pg.image.load('hoverCountry'+imageName+'.png')
        self.rect = self.imageNormal.get_rect()
        self.mask = pg.mask.from_surface(self.imageNormal)
        self.status = "normal" # hover; attacking; defending
        self.image = self.imageNormal

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

#blob = Blob((100,300), blue)
#blob2 = Blob((400,300), red)

#allBlobs = [blob, blob2]
mikem = Country('MikemCcu')
hollyh = Country('HolLyh')
jenniferg = Country('Jenniferg')
paulce = Country('Paulce')
allCountries = [mikem,hollyh,jenniferg,paulce]
background = pg.image.load("mapBackground.png")
#countryMikemCcu = pg.image.load("countryMikemCcu.png")
countryMikemIl = pg.image.load("countryMikemIl.png")
countryPame = pg.image.load("countryPame.png")
#countryPaulce = pg.image.load("countryPaulce.png")
countryTreNeeu = pg.image.load("countryTreNeeu.png")
countryHolLye = pg.image.load("countryHolLye.png")
#countryHolLyh = pg.image.load("countryHolLyh.png")
#countryJenniFerg = pg.image.load("countryJenniFerg.png")
countryJesUsri = pg.image.load("countryJesUsri.png")
countryLap = pg.image.load("countryLap.png")

while running:
    screen.fill(white)
    screen.blit(background, (0,0))
    for country in allCountries:
        country.draw()
    #screen.blit(countryMikemCcu, (0,0))
    screen.blit(countryHolLye, (0,0))
    #screen.blit(countryHolLyh, (0,0))
    #screen.blit(countryJenniFerg, (0,0))
    screen.blit(countryJesUsri, (0,0))
    screen.blit(countryLap, (0,0))
    screen.blit(countryMikemIl, (0,0))
    screen.blit(countryPame, (0,0))
    #screen.blit(countryPaulce, (0,0))
    screen.blit(countryTreNeeu, (0,0))



    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pos = pg.mouse.get_pos()
   # for entity in allBlobs:
   #     pos_in_mask = pos[0] - entity.rect.x, pos[1] - entity.rect.y
   #     touching = entity.rect.collidepoint(*pos) and entity.mask.get_at(pos_in_mask)

    for country in allCountries:
        pos_in_mask = pos[0] - country.rect.x, pos[1] - country.rect.y
        touching = country.rect.collidepoint(*pos) and country.mask.get_at(pos_in_mask)
    
        if (touching):
            #screen.fill(entity.bgColor)
            country.setStatus('hover')
        else:
            country.setStatus('normal')
    

    #screen.blit(blob.image, blob.rect)
    #screen.blit(blob2.image, blob2.rect)
    #card testing below...
    #screen.blit(leftSideIndex, (50,50))
    #screen.blit(rightSideIndex, (160,50))
    pg.display.update()

