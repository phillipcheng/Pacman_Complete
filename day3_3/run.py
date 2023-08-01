import pygame
from pygame.locals import *
from constants import *
from day3_3.nodes import NodeGroup
from day3_3.pacman import Pacman
from day3_3.pellets import PelletGroup


class GameController(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None
        self.clock = pygame.time.Clock()

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def startGame(self):      
        self.setBackground()
        self.nodes = NodeGroup("maze1.txt")
        self.pacman = Pacman(self.nodes.getStartTempNode())
        self.nodes.setPortalPair((0, 17), (27, 17))
        self.pellets = PelletGroup("maze1.txt")



    def update(self):
        dt = self.clock.tick(30) / 1000.0
        self.pacman.update(dt)
        self.pellets.update(dt)
        self.checkPelletEvents()
        self.checkEvents()
        self.render()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.nodes.render(self.screen)
        self.pellets.render(self.screen)
        self.pacman.render(self.screen)
        pygame.display.update()

    def checkPelletEvents(self):
        pellet = self.pacman.eatPellets(self.pellets.pelletList)
        if pellet:
            self.pellets.numEaten += 1
            self.pellets.pelletList.remove(pellet)

if __name__ == "__main__":
    game = GameController()
    game.startGame()
    while True:
        game.update()



