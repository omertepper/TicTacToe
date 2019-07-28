
class WinnerChecker():

    @staticmethod
    def check_for_winner(lst):
        if WinnerChecker.check_line(lst):
            return True
        elif WinnerChecker.check_row(lst):
            return True
        elif WinnerChecker.check_descending_slant(lst):
            return True
        elif WinnerChecker.check_appending_slant(lst):
            return True
        return False
        
        
    @staticmethod 
    def check_line(lst):
        new_list = []
        counter = 0
        for j in lst:
            for i in lst:
                new_list.append(i[counter])
            if WinnerChecker.check_all_same(new_list):
                return True
            new_list = []
        return False

    @staticmethod
    def check_row(lst):
        for row in lst:
            if WinnerChecker.check_all_same(row):
                return True
        return False


    @staticmethod
    def check_descending_slant(lst):
        counter = 0
        descending_slant = []
        for i in lst:
            descending_slant.append(i[counter])
            counter+=1
        if WinnerChecker.check_all_same(descending_slant):
            return True
        return False

    @staticmethod
    def check_appending_slant(lst):
        counter = len(lst) - 1
        appending_slant = []
        for i in lst:
            appending_slant.append(i[counter])
            counter-=1
        if WinnerChecker.check_all_same(appending_slant):
            return True
        return False

    @staticmethod
    def check_all_same(lst):
        if lst.count('O') == len(lst) or lst.count('X') == len(lst):
            return True
        return False
