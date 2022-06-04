# Side-Scroller-Game
Features
    Render_frame
        Prints frame object in screen
    Add character

    @dispatch (int, int, char)
    draw(x,y,symbol):
    @dispatch(int,int,map) { [4,5] : ‘o’, ‘-’ : [[3,3],[3,2],[3.1]}
    draw(x,y, symbols):
    Need global current frame variable, so don’t have to pass it in to functions
Object
    Frame
        Image (type string)
        Width
        Height
        Directory string length (constant int)
        Init_function(background_texture,width, height)
            Initializes frame
            Start with frame filled up with background_texture
f(x,y) = (h-y)*(w)+(x-1)
Scaled_width (constant)
Scaled_height (constant)
Character_hash_map = {[1,1]:’_’, [2,1]:’_’, [3,1]:’_’,[1,2]:’|’,[3,2]:’|’,[1,3]:’_’,[2,3]:’_’, [3,3]:’_’,}

Height = 40 characters
Width = 171 characters


Leaderboard

    Top ten
    Player name
    Enemies destroyed
    Fasted time level completed 
Functions
    Anybody can access and check leaderboard for top 10 players
    Anyone that finished game should have stats logged on leaderboard if top 10
Libraries
    Pipenv
    FastAPI
    Uvicorn






Library
    Opencv2
Brightness Map
    Char_density_ranking: $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.
    k = amount want to skip,s = scale_factor: k(s) = 1/s - 1


Class
    ImageLoader
        generate_hashmap(pixel_height, pixel_width,scaled_multiplier):
            Index_of_char_map= int((len(char_density_ranking) / 256)*gray_scale_value)
