# Risk with Pygame

I typically teach a major unit in my Python class with Pygame. I do
not use a lot of pygame calls and constructs which simplify building games;
instead, I prefer the simplification of getting something drawn to the screen
that we can then manipulate and "move". My students are required to learn
how to create a function with parameters, so we build our own collision
detection.  We do use classes, but only because we're figuring out how
to use lists and iterating through the lists to have lots of things
happening in our games.

This game is a bit different, so I will be learning how to make use
of the library's game-making capabilities.  I remember that Risk was
one of the first easy-to-find games on the newly released Macintosh.
Whether it was a Hypercard stack or a compiled program I can't recall, but
it seemed that there were many versions available on the FTP sites.  I have
recently become aware of Kriegsspiel and an article on the topic mentioned
Risk.  I'm not confident I can actually build the game, but I'd like to
explore what I need to learn in order to pull it off.

This is just a summer project.  I will likely not complete it as I am also
changing jobs (and city) for the first time in nearly 15 years, so I will
have lots of events competing for my attention.  I'm writing this
Readme.md June 10, 2024.  Let's see how far we get by August 10!

### Note 8:
- I was emailing a friend about Risk and realized that it would be useful for them
  to actually play it.  Asked the internet and, lo and behold:
  https://jamesfriend.com.au/pce-js/pce-js-apps/ 

- Added all countries to the list.  Need to consider how troop counts will
  be displayed.  Would like to display country names, but that may seem a bit
  crowded.  Also, not going to worry about the fact that some mask overlap.
  We'll just make sure only one country is in hover state before we allow the
  player to activate that country.

### Note 7:
- I am only guessing, but I would think that Pygame has a way to apply
  a color or texture to a surface.  I probably don't need to be making
  separate images for the country statuses (hover, normal, attack, defend).
  - still, here are the colors: defend is blue (80, 174, 206);
    attack is red (206, 80, 80). Hmmm, those are so close, why not go ahead
    and make them seem complementary?  I'll try blue (80, 80, 206) and see how
    it feels.

### Note 6:
- I have begun the process of creating an image for each state a country
  might be in.
  - "hover" - when the mouse is over the country
  - "normal" - when the country is not being accessed in any way
  - "attacking" - when the country has been chosen as the attacker
  - "defending" - when the country has been chosen to be attacked
  
  I'm trying out the pattern for hover that reminds me of the Mac version
  of Risk.  The color red is for the attacking country, and the color blue
  is for the defending country.

### Note 5:
- added map assets
   - drew a map in notebook and imported a photo of it into Krita
   - using stylus, drew each country on its own layer
   - saved each country layer as its own png
  
### Note 4:
- testing changing the mouse to a sword like the original Mac Risk game
  - use testMaskClickerV5.py to see the results
  - the image is built with Krita as a 64x64 png with a transparent background

### Note 3:
- found an archive of the game at https://www.myabandonware.com/game/risk-3pi
  - might be able to replicate some of the images and styling

### Note 2:
TODO list:
- ~~need to add blob images to a list~~
- ~~iterate through the list and checking for mouse collision~~
- incorporate collision detection in object, if possible

### Note 1: 
Because the countries will have irregular edges, I cannot use
a simplified collider.  I believe I will be able to use the image mask
to figure out if I am clicking on a country.  I will build the world
image with something like Krita, with each country on its own layer.  Then
each layer can be exported as an image.  Pygame has the 
pygame.mask.from_surface() method, which I think I can use to have
multiple Mask objects that I can check on to see which one the mouse
is touching.

https://stackoverflow.com/questions/52843879/detect-mouse-event-on-masked-image-pygame
