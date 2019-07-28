import pygame

class ScreenStartWrite():

    @staticmethod
    def write(screen,how_much_blocks):
        ScreenStartWrite._write_horizontal(screen,how_much_blocks)
        ScreenStartWrite._write_vertical(screen,how_much_blocks)


    @staticmethod
    def _write_horizontal(screen,how_much_blocks):
        y = 100
        for i in range(how_much_blocks-1):
            pygame.draw.lines(screen, (255,255,255), False, [(0,y),(how_much_blocks*100,y)], 1)
            pygame.display.flip()
            y = y+100

    @staticmethod
    def _write_vertical(screen,how_much_blocks):
        x = 100
        for i in range(how_much_blocks-1):
            pygame.draw.lines(screen, (255,255,255), False, [(x,0),(x,how_much_blocks*100)], 1)
            pygame.display.flip()
            x = x+100