from PIL import  Image, ImageDraw, ImageFont
from backGround import make_bg
from svglib import svg2rlg

def make_card(compN, name, statN1, stat1, date, bg):

    if(stat1 == '\t' or stat1 != stat1): stat1 = 'Coming soon...'
    if(type(stat1) == float): stat1 = int(stat1)

    textFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 80)
    nameFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 90)
    statFont = ImageFont.truetype('fonts/Inconsolata_Condensed-Regular.ttf', size = 60)
    signsFont = ImageFont.truetype('fonts/Neucha.ttf', size = 50)
    copmNameFont = ImageFont.truetype('fonts/Neucha.ttf', size = 85)
    windowColor = '#F4F4F4'
    eventColor = '#C1E787'
    eventOutline = '#8BA85E'
    outlineWidht = 5

    #imgName = f'{name}.pdf'
    imgName = 'bg_2.png'

    #make_big_bg(imgNAme, bg)

    imgToMake = Image.open(imgName)
    imgToMake = imgToMake.resize((764, 1024))
    draw = ImageDraw.Draw(imgToMake)
    cube333 = svg2png(url = r'svgs\333.svg', output_height=60, output_width=60,background_color=eventColor)
    #cube333.save('cube333.svg')
    #insert = Image.po

    

    ### structures ###

    #name 
    draw.rectangle([(50, 230),(714,330)], fill = windowColor, outline = 'gray', width = 2)

    #white bottom
    draw.rectangle([(0, 1024), (764, 894)], fill = windowColor)

    #white top
    draw.rectangle([(0,0),(764, 130)], fill = 'white')

    #outline
    draw.rectangle([(0,0), (764, 1024)], outline = 'black', width = 3)

    #event boxes
    draw.rectangle([(140,345), (200, 405)], fill = eventColor, outline = eventOutline)
    imgToMake.paste(cube333.resize(60,60),(140,345, 200, 405))

    ### text ###

    #comp name
    draw.text((382,65), text = compN, anchor = 'mm', font = nameFont, fill = 'black')

    #competitor name
    draw.text((382,280), text = name, font = textFont, anchor = 'mm', fill = 'black')

    imgToMake.save('test_.png')

make_card('KOSTELEC OPEN 2023', 'Arsenij Kuprin', 'statN1', 'stat1', 'date', 'bg')