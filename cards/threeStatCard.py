from PIL import Image, ImageDraw, ImageFont
from backGround import make_bg


def make_card(compN, name, statN1, statN2, statN3, stat1, stat2, stat3, date, bg):

    ###filtration###
    if(stat1 == '\t' or stat1 != stat1): stat1 = 'Coming soon...'
    if(stat2 == '\t' or stat2 != stat2): stat2 = 'Coming soon...'
    if(stat3 == '\t' or stat3 != stat3): stat3 = 'Coming soon...'
    if(type(stat1) == float): stat1 = int(stat1)
    if(type(stat2) == float): stat2 = int(stat2)
    if(type(stat3) == float): stat2 = int(stat3)
    

    textFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 70)
    statFont = ImageFont.truetype('fonts/Inconsolata_Condensed-Regular.ttf', size = 60)
    signsFont = ImageFont.truetype('fonts/Neucha.ttf', size = 50)
    copmNameFont = ImageFont.truetype('fonts/Neucha.ttf', size = 70)
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
    draw.rounded_rectangle([(50, 150),(994, 250)], radius = 40, fill = windowColor, outline='black', width = outlineWidht)
    #stat1
    draw.rounded_rectangle([(50, 310),(514, 410)], radius = 40, fill = windowColor, outline = 'black', width = outlineWidht)
    #stat2
    draw.rounded_rectangle([(534, 310),(994, 410)], radius = 40, fill = windowColor, outline = 'black', width = outlineWidht)
    #stat3
    draw.rounded_rectangle([(50, 470),(614, 570)], radius = 40, fill = windowColor, outline = 'black', width = outlineWidht)
    #date
    draw.rounded_rectangle([(704, 470),(994, 570)], radius = 40, fill = windowColor, outline = 'black', width = outlineWidht)

    ###text###

    #competition name
    draw.text((522, 50), text = compN, font = copmNameFont, fill = 'black', anchor = 'mm')
    #person name
    draw.text((90, 140), text = 'Name:', font = signsFont, fill = 'black', anchor = 'lb')
    draw.text((522, 200), text = name, font = textFont, fill = 'black', anchor = 'mm' )
    #stat1
    draw.text((90, 300), text = statN1, fill = 'black', anchor = 'lb', font = signsFont)
    draw.text((282, 360), text = str(stat1), font = textFont, fill = 'black', anchor = 'mm')
    #stat2
    draw.text((550, 300), text = statN2, fill = 'black', anchor = 'lb', font = signsFont)
    draw.text((762, 360), text = str(stat2), font = textFont, fill = 'black', anchor = 'mm')
    #stat3
    draw.text((90, 460), text = statN3, fill = 'black', anchor = 'lb', font = signsFont)
    draw.text((332, 520), text = str(stat3), font = textFont, fill = 'black', anchor = 'mm')
    #date
    draw.text((850, 520), text = date, font = textFont, fill = 'black', anchor = 'mm')

    imgToMake.save(imgName)
    return(imgName)