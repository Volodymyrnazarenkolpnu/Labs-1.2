"""module for all that is pygame"""
import sys
import os
import pygame
#region objs
path = os.path.split(os.path.abspath(__file__))[0]
resource_path = os.path.join(path, "resources")

def load_image(name, colorkey=None, scale=1):
    """loading images for making them into sprites"""
    img_name = os.path.join(resource_path, name)
    image = pygame.image.load(img_name)

    img_size = image.get_size()
    img_size = (img_size[0] * scale, img_size[1] * scale)
    image = pygame.transform.scale(image, img_size)
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

class TownObj():
    """town block on screen"""
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rectangle = load_image("town_texture")
        self.name = name
    def update_move(self):
        pos = pygame.mouse.get_pos()
        #self.rectangle.

def pygame_window_shenedigans():
    """everything about pygame window should be here, probably"""
    screen = pygame.display.set_mode((1280,720))
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255,255,255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(bg, (0,0))
        pygame.display.flip()
