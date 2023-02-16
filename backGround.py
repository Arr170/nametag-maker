from PIL import  Image

import inquirer

blueBG = '#77C3FB'
greenBG = '#B3C87B'
orangeBG = '#F0BA3D'


#color_mod = str(input('[a] choose color for your background (b=blue/g=green/o=orange/c=custom'))
def choose_bg():
    options = [
        inquirer.List(
            "color",
            message = "choose background color",
            choices = ['blue', 'green', 'orange', 'custom']
        ),
    ]
    answers = inquirer.prompt(options)
    if(answers['color'] == 'blue'): bg = blueBG
    if(answers['color'] == 'green'): bg = greenBG
    if(answers['color'] == 'orange'): bg = orangeBG
    if(answers['color'] == 'custom'):
        bg = str(input('[a] enter hex code of color you waht to use (format: #xxxxxx): '))
    return(bg)


def make_bg(name, bg):

    img = Image.new(mode = 'RGB', size = (1044, 655), color = bg)
    img.save(name)

    return()

def make_big_bg(name, bg):
    img = Image.new(mode = 'RGB', size = (2100, 3000), color = bg)
    img.save(name)

    return()

