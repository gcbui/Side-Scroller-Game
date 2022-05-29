import asyncio
import sys
import msvcrt

height = 40 #40 characters
width = 172 #171 characters
skip_lines = 2
height = height - skip_lines
world_x = -20
world_y = 20

def get_input():
    global world_x
    global world_y
    move = msvcrt.getch().decode("ASCII")
    if move == 'd':
        world_x+=1
    elif move == 'w':
        world_y+=1
    elif move == 's':
        world_y-=1
    elif move == 'a':
        world_x-=1
    elif move == 'q':
        quit()



        

class Frame:
    image = ""
    banner = ""
    def __init__(self):
        self.image = ""
        self.banner = ""
    #width = for scaling
    #height = for scaling
    #directory_lenth = may show up for input
    def init_background(self, background_symbol, width, height):
        self.image = ""
        self.banner = ""
        pixel_count = width * height #number of pixels in one frame
        skip_pixel_count = width * skip_lines
        for num in range(skip_pixel_count):
            self.banner += '.'
        for numb in range(pixel_count):
            self.image += background_symbol
      
current_frame = Frame()

def draw(x,y,symbol=None,symbols=None,use_screen_space=False):
    global world_x
    global world_y
    if symbols == None:
        screen_x = x 
        screen_y = y
        if use_screen_space == False:
            screen_x-=world_x
            screen_y-=world_y
        if screen_x <1 or screen_y <1 or screen_x > width or screen_y > height:
            return
        i = int((height-screen_y) * (width) + (screen_x-1))
        current_frame.image = current_frame.image[:i] + symbol + current_frame.image[i + 1:]
    else:
        for symbol in symbols:
            screen_x = x+symbol[0]-1
            screen_y = y+symbol[1]-1
            if use_screen_space == False:
                screen_x-=world_x
                screen_y-=world_y
            if screen_x <1 or screen_y <1 or screen_x > width or screen_y > height:
                continue
            i = int((height-screen_y) * (width) + (screen_x-1))
            current_frame.image = current_frame.image[:i] + symbols[symbol] + current_frame.image[i + 1:]

def render_frame():
    print(current_frame.banner+current_frame.image)

def game():
    global world_x
    global world_y
    character_hash_map = {tuple([2,1]):'|', tuple([8,1]):'|', tuple([3,2]):'_',tuple([4,2]):'_',tuple([5,2]):'|',tuple([6,2]):'_',tuple([7,2]):'_', tuple([1,3]):'|',tuple([5,3]):'|',tuple([9,3]):'|',tuple([2,4]):'_', tuple([3,4]): '_',tuple([4,4]):'_',tuple([5,4]):'|',tuple([6,4]):'_',tuple([7,4]):'_',tuple([8,4]):'_', tuple([5,5]):'>'                        
,tuple([4,6]):'0',tuple([6,6]):'0',tuple([4,7]):'~',tuple([6,7]):'~'}
    object_hash_map = {tuple([1,1]):'_', tuple([2,1]):'_', tuple([3,1]):'_',tuple([1,2]):'|',tuple([3,2]):'|',tuple([1,3]):'_',tuple([2,3]):'_', tuple([3,3]):'_'}
    for num in range(10000):
        current_frame.init_background('*',width, height) 
        get_input()       
        draw(width/2,height/2,symbol='c')
        draw(1,1,symbol='L')
        draw(width,height,symbol='R')
        draw(width,1,symbol='d')
        draw(1,height,symbol='u')
        draw(width/2,height/2,symbols=character_hash_map,use_screen_space=True)
        draw(1,height/2,symbols=object_hash_map)
        render_frame()

       
game()


    



