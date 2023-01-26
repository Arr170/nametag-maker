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
            message = "[a] choose background color",
            choices = ['blue', 'green', 'orange', 'custom']
        ),
    ]
    answers = inquirer.prompt(options)
    return(answers['color'])
    #print(answers['color'])


def make_bg(name):
    bg = choose_bg()

    if(bg == 'blue'): bg = blueBG
    if(bg == 'green'): bg = greenBG
    if(bg == 'orange'): bg = orangeBG
    if(bg == 'custom'):
        bg = str(input('[a] enter hex code of color you waht to use (format: #xxxxxx): '))

    img = Image.new(mode = 'RGB', size = (1044, 655), color = bg)
    img.save(name)

    return()


