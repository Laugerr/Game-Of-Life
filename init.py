from random import randint as rand

def game_create_field() -> list[int]:
    print(' ╔' + '═'*55 + '╗')
    width = int(input('     ╔Enter the width of the field: '))
    height = int(input('     ╚Enter the hight of the field: '))
    print(' ╚' + '═'*55 + '╝')

    while width <= 0 or height <= 0:
        print('\n'*3 + " ▓!▓ Invalid dimensions inputs. Insert only Natural number ▓!▓\n " + "═"*61 + '\n'*3)
        print(' ╔' + '═'*55 + '╗')
        width = int(input('     ╔Enter the width of the field: '))
        height = int(input('     ╚Enter the hight of the field: '))
        print(' ╚' + '═'*55 + '╝')

    return [width, height]
        
def game_init_field(width, height) -> list[list[int]]:
        return [ [ 0 for w in range(width) ] for h in range(height) ]

def game_print_field(game_field) -> list[list[int]]:
    for h in range(len(game_field)):
        print('\n'*5)
        print('--------------Game Field--------------')
        print(game_field[h])

# game_create_field()
