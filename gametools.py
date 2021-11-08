class Cell:
    def get_print_character(self):
        return ' 0'

class Field:
    def __init__(self , width , hight):
        self._width = width
        self._hight = hight   
        self._grid = [[Cell() for h_cells in range(self._hight)] for w_cells in range(self._width)]

    def draw_field(self):
        print('\n'*5)
        print('--------------Game Field--------------')
        for w in self._grid:
            for h in w:
                print (h.get_print_character(),end='')
            print ()
