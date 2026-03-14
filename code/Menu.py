import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE



class Menu:
    def __init__(self,window):
        self.window = window # open window
        self.surf = pygame.image.load('./asset/MenuBg.png') # surf save an image: background image
        self.rect = self.surf.get_rect(left=0, top=0) # Create a rectangle from self.surf to position the image.

    def run(self,):
        pygame.mixer_music.load('./asset/Menu.mp3')  # load the music
        pygame.mixer_music.play(-1)  # play the music in loop
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # draw the image from self.surf and the destiny is self.rect
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 180 + 30 * i))

            pygame.display.flip() # display the data



            for event in pygame.event.get():  # check for all events
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect) #texts

# pass # pass permit to create a function empty