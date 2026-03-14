import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


            # pass # pass permit to create a function empty
            #for event in pygame.event.get():  # check for all events
                #if event.type == pygame.QUIT:
                    #pygame.quit()  # close window
                   # quit()  # end pygame
