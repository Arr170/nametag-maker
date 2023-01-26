from PIL import Image, ImageDraw, ImageFont
from backGround import make_bg

def make_card(compN, name, statN1, statN2, stat1, stat2, bg):

    ###filter###
    if(stat1 == '\t' or stat1 != stat1): stat1 = 'Coming soon...'
    if(stat2 == '\t' or stat2 != stat2): stat2 = 'Coming soon...'
    if(type(stat1) == float): stat1 = int(stat1)
    if(type(stat2) == float): stat2 = int(stat2)


    textFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 80)
    nameFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 90)
    statFont = ImageFont.truetype('fonts/Inconsolata_Condensed-Regular.ttf', size = 70)
    signsFont = ImageFont.truetype('fonts/Neucha.ttf', size = 55)
    copmNameFont = ImageFont.truetype('fonts/Neucha.ttf', size = 85)
    backgoundColor = '#B3C87B'
    windowColor = '#F4F4F4'
    outlineWidht = 5

    imgName = f'{name}.png'

    #creating background
    make_bg(imgName, bg)


    imgToMake = Image.open(imgName)
    draw = ImageDraw.Draw(imgToMake)

    ###structures###

    #name
    draw.rounded_rectangle([(250, 180),(994, 280)], radius = 40, fill = windowColor, outline='black', width = outlineWidht)
    #stat1
    draw.rounded_rectangle([(522, 340),(994, 440)], radius = 40, fill = windowColor, outline = 'black', width = outlineWidht)
    #stat2
    draw.rounded_rectangle([(522, 500),(994, 600)], radius = 40, fill = windowColor, outline = 'black', width = outlineWidht)
    
    ###text###

    #competition name
    draw.text((522, 80), text = compN, font = copmNameFont, fill = 'black', anchor = 'mm')
    #person name
    draw.text((50, 230), text = 'Name:', font = signsFont, fill = 'black', anchor = 'lm')
    draw.text((622, 230), text = name, font = textFont, fill = 'black', anchor = 'mm' )
    #stat1
    draw.text((50, 390), text = statN1 + ':', fill = 'black', anchor = 'lm', font = signsFont)
    draw.text((759, 390), text = str(stat1), font = statFont, fill = 'black', anchor = 'mm')
    #stat2
    draw.text((50, 555), text = statN2 + ':', fill = 'black', anchor = 'lm', font = signsFont)
    draw.text((759, 550), text = str(stat2), font = statFont, fill = 'black', anchor = 'mm')
    
    
    imgToMake.save(imgName)
    return(imgName)

