## Risk with Pygame

I typically teach a major unit in my Python class with Pygame. I do
not use a lot of pygame calls and constructs which simplify bulding games;
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

# Note 1: 
Because the countries will have irregular edges, I cannot use
a simplified collider.  I believe I will be able to use the image mask
to figure out if I am clicking on a country.  I will build the world
image with something like Krita, with each country on its own layer.  Then
each layer can be exported as an image.  Pygame has the 
pygame.mask.from_surface() method, which I think I can use to have
multiple Mask objects that I can check on to see which one the mouse
is touching.

https://stackoverflow.com/questions/52843879/detect-mouse-event-on-masked-image-pygame
