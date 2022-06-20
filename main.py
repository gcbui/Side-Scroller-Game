import msvcrt
import os
from re import X #for obtaining terminal dimensions   
from image_loader import ImageLoader

HEIGHT = 0 #40 characters
WIDTH = 0 #172 characters
SKIP_LINES = 1
HEIGHT -= SKIP_LINES
WORLD_X = 5
WORLD_Y = 5
CHAR_SCREEN_SPACE = False
X = 0
Y = 0
      
class Frame:
    #WIDTH = for scaling
    #HEIGHT = for scaling
    #directory_lenth = may show up for input
    image = ""
    banner = ""

    def __init__(self):
        self.image = ""
        self.banner = ""

    def init_background(self, background_symbol, WIDTH, HEIGHT):
        self.image = ""
        self.banner = ""
        pixel_count = WIDTH * HEIGHT #number of pixels in one frame
        skip_pixel_count = WIDTH * SKIP_LINES
        for num in range(skip_pixel_count):
            self.banner += '.'
        for numb in range(pixel_count):
            self.image += background_symbol

def update_frame_dimensions():
    # Get the size
    # of the terminal
    global WIDTH
    global HEIGHT
    size = os.get_terminal_size()   # gets width and length of terminal in terms of number of characters
    WIDTH = size[0]
    HEIGHT = size[1]

def get_input():
    global WORLD_X
    global WORLD_Y
    global HEIGHT
    global WIDTH
    global X
    global Y
    move = msvcrt.getch().decode("ASCII")
    if move == 'd':
        if X > WIDTH-3:
            X = WIDTH-3
            WORLD_X-=1
        WORLD_X-=1
    elif move == 'w':
        if Y > HEIGHT-3:
            Y = HEIGHT - 3
            WORLD_Y -= 1
        WORLD_Y-=1
    elif move == 's':
        if Y < 3:
            Y = 3
            WORLD_Y += 1
        WORLD_Y+=1
    elif move == 'a':
        if X < 3:
            X = 3
            WORLD_X+=1
        WORLD_X+=1
    elif move == 'q':
        quit()


current_frame = Frame()

def draw(x,y,symbol=None,symbols=None,use_screen_space=False):
    global WORLD_X
    global WORLD_Y
    if symbols is None:
        screen_x = x 
        screen_y = y
        if not use_screen_space:
            screen_x-=WORLD_X
            screen_y-=WORLD_Y
        if screen_x <1 or screen_y <1 or screen_x > WIDTH or screen_y > HEIGHT:
            return
        i = int((HEIGHT-screen_y) * (WIDTH) + (screen_x-1))
        current_frame.image = current_frame.image[:i] + symbol + current_frame.image[i + 1:]
    else:
        for symbol in symbols:
            screen_x = x+symbol[0]-1
            screen_y = y+symbol[1]-1
            if not use_screen_space:
                screen_x-=WORLD_X
                screen_y-=WORLD_Y
            if screen_x <1 or screen_y <1 or screen_x > WIDTH or screen_y > HEIGHT:
                continue
            i = int((HEIGHT-screen_y) * (WIDTH) + (screen_x-1))
            current_frame.image = current_frame.image[:i] + symbols[symbol] + current_frame.image[i + 1:]


def draw_character(X,Y,symbol=None,symbols=None):
    global WORLD_X
    global WORLD_Y
    if symbols is None:
        screen_x = X 
        screen_y = Y
        if not CHAR_SCREEN_SPACE:
            screen_x-=WORLD_X
            screen_y-=WORLD_Y
        if screen_x <1 or screen_y <1 or screen_x > WIDTH or screen_y > HEIGHT:
            return
        i = int((HEIGHT-screen_y) * (WIDTH) + (screen_x-1))
        current_frame.image = current_frame.image[:i] + symbol + current_frame.image[i + 1:]
    else:
        for symbol in symbols:
            screen_x = X+symbol[0]-1
            screen_y = Y+symbol[1]-1
            if not CHAR_SCREEN_SPACE:
                screen_x-=WORLD_X
                screen_y-=WORLD_Y               
            #if screen_x <1 or screen_y <1 or screen_x > (WIDTH-1) or screen_y > (HEIGHT-1):
                #continue    
           
            i = int((HEIGHT-screen_y) * (WIDTH) + (screen_x-1))
            current_frame.image = current_frame.image[:i] + symbols[symbol] + current_frame.image[i + 1:]

def render_frame():
    print(current_frame.banner+current_frame.image)

#def use_screen_space():
 #   if screen_x <1 or screen_y <1 or screen_x > WIDTH or screen_y > HEIGHT:
        

def game():
    '''core game logic'''
    global POINTER
    global CHAR_SCREEN_SPACE
    global X
    global Y
    character_hash_map = {tuple([2,1]):'|', tuple([8,1]):'|', tuple([3,2]):'_',tuple([4,2]):'_',tuple([5,2]):'|',tuple([6,2]):'_',tuple([7,2]):'_', tuple([1,3]):'|',tuple([5,3]):'|',tuple([9,3]):'|',tuple([2,4]):'_', tuple([3,4]): '_',tuple([4,4]):'_',tuple([5,4]):'|',tuple([6,4]):'_',tuple([7,4]):'_',tuple([8,4]):'_', tuple([5,5]):'>',                        
                          tuple([4,6]):'0',tuple([6,6]):'0',tuple([4,7]):'~',tuple([6,7]):'~'}
    object_hash_map = {tuple([1,1]):'_', tuple([2,1]):'_', tuple([3,1]):'_',tuple([1,2]):'|',tuple([3,2]):'|',tuple([1,3]):'_',tuple([2,3]):'_', tuple([3,3]):'_'}
    print("--------------LOADING LEVEL--------------")
    #mario_background_image_loader = ImageLoader(path = "image_data/unnamed.png")
    #mario_level_image_loader = ImageLoader(path = "image_data/mario_background.jpg")
    test = ImageLoader(path = "image_data/94-946065_dog-pixel-art-easy-hd-png-download.png")

    #mario_level_hash_map = mario_level_image_loader.generate_hashmap(invert_colors = True,scale_x=0.5, scale_y=0.3)
    #mario_background_hash_map = mario_background_image_loader.generate_hashmap(invert_colors = False,scale_x=1, scale_y=1)
    test_hash_map = test.generate_hashmap(invert_colors = False,scale_x=.2, scale_y=.3)
    update_frame_dimensions()
    X= WIDTH/2
    Y= HEIGHT/2
    while True:
        update_frame_dimensions()
        current_frame.init_background('*',WIDTH, HEIGHT) 
        get_input()    
        #draw(0,0,symbols=mario_level_hash_map)   
        #draw(0,0,symbols=mario_background_hash_map)    
        draw(0,0,symbols=test_hash_map)   
        draw(WIDTH/2,HEIGHT/2,symbol='c')
        draw(WIDTH/5, HEIGHT/3, symbol='k')
        draw(1,1,symbol='L')
        draw(WIDTH,HEIGHT,symbol='R')
        draw(WIDTH,1,symbol='d')
        draw(1,HEIGHT,symbol='u')
        '''if (POINTER[0] > WIDTH-3) or (POINTER[0] <3) or (POINTER[1] > HEIGHT-3) or (POINTER[1] < 3):
            CHAR_SCREEN_SPACE = True
            if POINTER[0] > WIDTH-3:
                POINTER[0] = WIDTH-3
            if POINTER[0] < 3 :
                POINTER[0] = 3
            if POINTER[1] > HEIGHT-3:
                POINTER[1] = HEIGHT-3
            if POINTER[1] < 3:
               POINTER[1] = 3
        else:
            CHAR_SCREEN_SPACE = False'''
        draw_character(X,Y,symbols=character_hash_map)
        draw(1,HEIGHT/2,symbols=object_hash_map)
        render_frame()




game()
    



