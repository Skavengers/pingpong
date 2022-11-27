
from .. import tools
import pygame as pg
import os

class Battle:
    def __init__(self, x, y, width, height, facing=tools.CONTROLLER_DICT['down']):
        self.surface = pg.Surface([width, height])
        self.rect = self.surface.get_rect()
        self.x = 500
        self.y = 500
        self.score = 0, 0
        self.width = width
        self.height = height
        self.hero = pg.image.load(os.path.abspath(r"resources\graphics\hero.png")).convert()
        self.hero.set_colorkey((255,) * 3)
        #self.background = pg.image.load(os.path.abspath(r"resources\maps\battle_background\background.jpg"))
    def get_event(self,keys,event):
        #pg.draw.rect(self.screen,(255,0,0),pg.Rect(200,200,200,200))
        #pg.display.flip()
        #Handle events pertaining to player control.
        move_setup = [[0,1,0],[0,0,0]]
        if event.type == pg.K_LEFT:
            self.x = 200
        if event.type == pg.KEYDOWN:
            self.y = 300
        if event.type == pg.KEYUP:
            self.y =500
        if event.type == pg.K_LEFT:
            self.x = 700
            #self.add_direction(event.key)

            #self.pop_direction(event.key)
    def render(self, screen):
        print(type(screen))
        screen.blit(self.hero, (self.x, self.y))
