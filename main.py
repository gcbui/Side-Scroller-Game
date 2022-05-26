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

def draw(x,y,symbol):
    i = int((height-y) * (width) + (x-1))
    current_frame.image = current_frame.image[:i] + symbol + current_frame.image[i + 1:]

    
def render_frame():
    print(current_frame.banner+current_frame.image)


def game():
    for num in range(10000):
        current_frame.init_background('*',width, height)        
        draw(width/2,height/2,'c')
        draw(1,1,'L')
        draw(width,height,'R')
        draw(width,1,'d')
        draw(1,height,'u')
        render_frame()
       

game()


    



