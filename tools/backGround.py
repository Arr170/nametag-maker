from PIL import  Image

def make_small_bg(name, color):
    img = Image.new(mode = 'RGB', size = (1044, 655), color = color)
    img.save(name)
    return()

def make_big_bg(name, color):
    img = Image.new(mode = 'RGB', size = (764, 894), color = color)
    img.save(name)
    return()