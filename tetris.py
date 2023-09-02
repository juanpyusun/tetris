from enum import Enum
import keyboard

SCREEN_SIZE = 10

class Movement(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4
    ROTATE = 5

def tetris():
    screen = [['■','▢','▢','▢','▢','▢','▢','▢','▢','▢'],
              ['■','■','■', '▢','▢','▢','▢','▢','▢','▢'],
              ['▢','▢','▢','▢','▢','▢','▢','▢','▢','▢'],
              ['▢','▢','▢','▢','▢','▢','▢','▢','▢','▢'],
              ['▢','▢','▢','▢','▢','▢','▢','▢','▢','▢'],
              ['▢','▢','▢','▢','▢','▢','▢','▢','▢','▢'],
              ['▢','▢','▢','▢','▢','▢','▢','▢','▢','▢'],
              ['▢','▢','▢','▢','▢','▢','▢','▢','▢','▢'],
              ['▢','▢','▢','▢','▢','▢','▢','▢','▢','▢'],
              ['▢','▢','▢','▢','▢','▢','▢','▢','▢','▢']]
    print_screen(screen)
    rotation = 0
    while True:
        event = keyboard.read_event()
        
        if event.name == "esc":
            break
        elif event.event_type == keyboard.KEY_DOWN:
            if event.name == "w":
                screen, rotation = move_piece(screen, Movement.UP, rotation)
            elif event.name == "s":
                screen, rotation = move_piece(screen, Movement.DOWN, rotation)   
            elif event.name == "d":
                screen, rotation = move_piece(screen, Movement.RIGHT, rotation)  
            elif event.name == "a":
                screen, rotation = move_piece(screen, Movement.LEFT, rotation)  
            elif event.name == "space":
                screen, rotation = move_piece(screen, Movement.ROTATE, rotation)  
    
    
def print_screen(screen: list):
    print("\nPantalla Tetris\n")
    for row in screen:
        print("  ".join(row))
        
def move_piece(screen: list, movement: Movement, rotation: int)-> (list, int):
    new_screen = [['▢'] * 10 for _ in range(10)]
    rotation_item = 0
    rotations = [[(1,1),(0,0),(-2,0),(-1,-1)],  
                 [(0,1),(-1,0),(0,-1),(1,-2)], #primera rotacion
                 [(0,2),(1,1),(-1,1),(-2,0)],  #segunda rotacion
                 [(0,1),(1,0),(2,-1),(1,-2)]] #tercera rotacion
    if movement is Movement.ROTATE:
        rotation = 0 if rotation == 3 else rotation + 1  #if-else inline  <<expr_true if condicional else expr_false>>
    
    new_rotation = rotation
        
    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):
            if item == "■":
                new_row_index = 0
                new_column_index = 0        
                match movement:
                    case Movement.UP:
                        new_row_index = row_index - 1   #sube una fila
                        new_column_index = column_index  #conserva la misma columna
                    case Movement.DOWN:
                        new_row_index = row_index + 1
                        new_column_index = column_index
                    case Movement.LEFT:
                        new_row_index = row_index
                        new_column_index = column_index - 1
                    case Movement.RIGHT:
                        new_row_index = row_index
                        new_column_index = column_index + 1 
                    case Movement.ROTATE:
                        new_row_index = row_index + rotations[new_rotation][rotation_item][0]
                        new_column_index = column_index + rotations[new_rotation][rotation_item][1]
                        rotation_item += 1
                                        
                if (new_row_index > SCREEN_SIZE - 1) or (new_column_index > SCREEN_SIZE - 1) or (new_row_index < 0) or (new_column_index < 0):
                    print_screen(screen)
                    return screen, new_rotation
                else:
                    new_screen[new_row_index][new_column_index] = "■"
    print_screen(new_screen)
    return new_screen, new_rotation

        

tetris()