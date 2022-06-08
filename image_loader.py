import cv2

class ImageLoader:
    def __init__(self,path="image_data/unnamed.png"):

        self.char_density_ranking= "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "    #highest to lowest based on ascii density

        self.path = path
        self.img = cv2.imread(self.path)
        self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.height, self.width, self.channels = self.img.shape
        

    def generate_hashmap(self,scale_x:float=1, scale_y:float=1,invert_colors=False,transparency_x=1,transparency_y=1): 
        height = len(self.img_gray)
        width = len(self.img_gray[0])
        image_to_object_map = {}
        amount_to_skip_x=int(1/transparency_x) 
        amount_to_skip_y=int(1/transparency_y) 
        amount_to_skip_x = max(0,amount_to_skip_x)
        amount_to_skip_y = max(0,amount_to_skip_y)
        for y in range(0,height,amount_to_skip_y):
            for x in range(0,width,amount_to_skip_x):
                gray_scale_value = self.img_gray[y][x]
                if invert_colors:
                    gray_scale_value = 255- gray_scale_value
                index_of_char_map = int((len(self.char_density_ranking) / 256)*gray_scale_value)
                image_to_object_map[tuple([int(scale_x*x),int(scale_y*-1*y)])] = self.char_density_ranking[index_of_char_map]
        return image_to_object_map


 



