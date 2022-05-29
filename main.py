height = 40 #40 characters
width = 172 #171 characters
skip_lines = 2
height = height - skip_lines

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

def draw(x,y,symbol=None,symbols=None):
    if symbols == None:
        i = int((height-y) * (width) + (x-1))
        current_frame.image = current_frame.image[:i] + symbol + current_frame.image[i + 1:]
    else:
        for symbol in symbols:
            i = int((height-y-symbol[1]-1) * (width) + (x+symbol[0]-2))
            current_frame.image = current_frame.image[:i] + symbols[symbol] + current_frame.image[i + 1:]

def render_frame():
    print(current_frame.banner+current_frame.image)

def game():
    character_hash_map = {tuple([2,1]):'|', tuple([8,1]):'|', tuple([3,2]):'_',tuple([4,2]):'_',tuple([5,2]):'|',tuple([6,2]):'_',tuple([7,2]):'_', tuple([1,3]):'|',tuple([5,3]):'|',tuple([9,3]):'|',tuple([2,4]):'_', tuple([3,4]): '_',tuple([4,4]):'_',tuple([5,4]):'|',tuple([6,4]):'_',tuple([7,4]):'_',tuple([8,4]):'_', tuple([5,5]):'>'                        
,tuple([4,6]):'0',tuple([6,6]):'0',tuple([4,7]):'~',tuple([6,7]):'~'}

    for num in range(10000):
        current_frame.init_background('*',width, height)        
        draw(width/2,height/2,symbol='c')
        draw(1,1,symbol='L')
        draw(width,height,symbol='R')
        draw(width,1,symbol='d')
        draw(1,height,symbol='u')
        draw(width/2,height/2,symbols=character_hash_map)
        render_frame()
       
game()


    



