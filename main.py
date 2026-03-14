import pygame

print('Setup Star')
pygame.init()
window = pygame.display.set_mode((800,600))
print('Setup Finish')

print('Loop Start')
while True:
    # pass # pass permit to create a function empaty
    for event in pygame.event.get(): # check for all events
        if event.type == pygame.QUIT:
            pygame.quit() #close window
            quit() #end pygame
