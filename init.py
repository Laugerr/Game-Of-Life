from gametools import Field

def game_create_field():
    input_w = int(input('Enter the width of the field: '))
    input_h = int(input('Enter the hight of the field: '))

    game_field = Field(input_w,input_h)

    game_field.draw_field()

game_create_field()