import pygame
from screen_start_write import ScreenStartWrite
from click_handler import ClickHandler
class ScreenStarter:

    @staticmethod
    def start(how_much_blocks=3):
        pygame.init()
        screen = ScreenStarter.screen_details(how_much_blocks)
        ScreenStartWrite.write(screen,how_much_blocks)
        click_handler = ClickHandler(how_much_blocks)
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    ClickHandler.write_value_to_screen(screen,pos)

                elif event.type == pygame.QUIT:
                    crashed = True

    @staticmethod
    def screen_details(how_much_blocks):
        screen = pygame.display.set_mode((how_much_blocks*100, how_much_blocks*100))
        pygame.display.set_caption('Tic Tac Toe')
        return screen


