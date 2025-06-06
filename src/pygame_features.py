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

class TownObj(pygame.sprite.Sprite):
    """town block on screen"""
    def __init__(self, name, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("town_texture.png")
        self.name = name
        self.x = x
        self.y = y
        self.drag_offsetx = None
        self.drag_offsety = None
        self.rect.center = (x,y)
        self.moving = False
        self.interact_priority = 2

    def interact(self, event, main_interacting, _hold_time=0):
        """basic interact func"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self == main_interacting:
            self.moving = True
        if self.moving is True:
            self.update_move()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.moving is True:
                self.moving = False
                self.drag_offsetx = None
                self.drag_offsety = None
                self.update_coords(self.x, self.y + 5)

    def update_move(self):
        """drag and drop for towns"""
        pos = pygame.mouse.get_pos()
        if self.drag_offsety is None:
            self.drag_offsetx = self.x - pos[0]
            self.drag_offsety = self.y - pos[1] - 5
        print(self.x, self.y, self.drag_offsetx, self.drag_offsety)
        x = pos[0] + self.drag_offsetx
        y = pos[1] + self.drag_offsety
        self.update_coords(x, y)

    def update_coords(self, x, y):
        """update the coords of a sprite"""
        self.x = x
        self.y = y
        self.rect.center = (x, y)

def pygame_window_shenedigans():
    """everything about pygame window should be here, probably"""
    screen = pygame.display.set_mode((700,700))
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255,255,255))

    town_list = [TownObj("a", 75, 75), TownObj("b", 150, 150)]
    obj_list = []

    for obj in town_list:
        obj_list.append(obj)
    allsprites = pygame.sprite.LayeredUpdates(set(obj_list))

    interacting = []
    main_interacting = None
    hold_time_mouse = 0
    clock = pygame.time.Clock()
    #mainloop
    while True:
        clock.tick(60)

        #finding objects to interact
        mousex, mousey = pygame.mouse.get_pos()
        pointer_rect = pygame.Rect(mousex, mousey, 1, 1)
        hover_objs = pointer_rect.collideobjectsall(obj_list, key=lambda o: o.rect)
        for obj in hover_objs:
            interacting.append(obj)
        main_interacting = pointer_rect.collideobjects(obj_list, key=lambda o: o.rect)
        if main_interacting is not None:
            allsprites.move_to_front(main_interacting)
        if len(interacting) > 0 and main_interacting in interacting:
            interacting.remove(main_interacting)
        #

        for event in pygame.event.get():
            if len(interacting) > 0:
                for el in interacting:
                    el.interact(event, main_interacting, hold_time_mouse)
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                hold_time_mouse += 1
            if main_interacting is not None:
                main_interacting.interact(event, main_interacting, hold_time_mouse)
            if event.type == pygame.MOUSEBUTTONUP:
                interacting.clear()
                main_interacting = None
                hold_time_mouse = 0
        screen.blit(bg, (0,0))
        allsprites.update()
        allsprites.draw(screen)
        pygame.display.flip()
