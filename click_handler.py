import pygame
from winner_checker import WinnerChecker
class ClickHandler():
    POSITION_LIST = []
    X_O = 'X'
    def __init__(self, how_much_blocks):
        for i in range(how_much_blocks):
            list_to_append = []
            for i in range(how_much_blocks):
                list_to_append.append(None)
            ClickHandler.POSITION_LIST.append(list_to_append)

    @staticmethod
    def write_value_to_screen(screen,pos):
        row_col = ClickHandler.get_click_value(pos)
        if ClickHandler.check_value(row_col):
            if ClickHandler.X_O == 'X':
                ClickHandler.write_X(screen, row_col)
            else:
                ClickHandler.write_O(screen, row_col)

            ClickHandler.X_O = ClickHandler.check_next_contender()
        if WinnerChecker.check_for_winner(ClickHandler.POSITION_LIST):
            text = 'won'
            font = pygame.font.Font(None, 30)
            text = font.render(text, True, (255,255,255))
            screen.blit(text,(150,150))
            pygame.display.flip()
            

    @staticmethod
    def write_X(screen,row_col):
        y,x = row_col
        x = x*100
        y = y*100
        pygame.draw.line(screen,(255,255,255),(x,y),(x+100,y+100),1)
        pygame.draw.line(screen,(255,255,255),(x,y+100),(x+100,y),1)
        pygame.display.flip()

    @staticmethod 
    def write_O(screen,row_col):
        y,x = row_col
        x = x*100
        y = y*100
        pygame.draw.circle(screen,(255,255,255),(x+50,y+50),20)
        pygame.display.flip()  



    @staticmethod
    def get_click_value(pos):
        x,y = pos
        col = int(x/100)
        row = int(y/100)
        return (row,col)

    @staticmethod
    def check_value(row_col):
        row,col = row_col
        value = ClickHandler.POSITION_LIST[row][col]
        if value is None:
            ClickHandler.POSITION_LIST[row][col] = ClickHandler.X_O
            return True
        return False

    @staticmethod
    def check_next_contender():
        if ClickHandler.X_O == 'X':
            return ('O')
        return ('X')
        