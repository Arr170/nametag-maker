from PIL import  Image, ImageDraw, ImageFont
from backGround import make_bg

def make_card(compN, name, statN1, stat1, date, bg):

    ###filter###

    if(stat1 == '\t' or stat1 != stat1): stat1 = 'Coming soon...'
    if(type(stat1) == float): stat1 = int(stat1)

    textFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 80)
    nameFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 90)
    statFont = ImageFont.truetype('fonts/Inconsolata_Condensed-Regular.ttf', size = 60)
    signsFont = ImageFont.truetype('fonts/Neucha.ttf', size = 50)
    copmNameFont = ImageFont.truetype('fonts/Neucha.ttf', size = 85)
    windowColor = '#F4F4F4'
    outlineWidht = 5

    imgName = f'{name}.png'


    make_bg(imgName, bg)


    imgToMake = Image.open(imgName)
    draw = ImageDraw.Draw(imgToMake)
    ###structures###

    #name
    draw.rounded_rectangle([(50, 250),(994, 360)], radius = 40, fill = windowColor, outline='black', width = outlineWidht)
    #stat1
    draw.rounded_rectangle([(50, 460),(570, 560)], radius = 40, fill = windowColor, outline = 'black', width = outlineWidht)
    #date
    draw.rounded_rectangle([(650, 460),(994, 560)], radius = 40, fill = windowColor, outline = 'black', width = outlineWidht)

    ###text###

    #competition name
    draw.text((522, 100), text = compN, font = copmNameFont, fill = 'black', anchor = 'mm')
    #person name
    draw.text((90, 240), text = 'Name', font = signsFont, fill = 'black', anchor = 'lb')
    draw.text((522, 300), text = name, font = nameFont, fill = 'black', anchor = 'mm' )
    #stat1
    draw.text((90, 450), text = statN1, fill = 'black', anchor = 'lb', font = signsFont)
    draw.text((310, 510), text = str(stat1), font = textFont, fill = 'black', anchor = 'mm')
    #date
    draw.text((822, 510), text = date, font = textFont, fill = 'black', anchor = 'mm')

    imgToMake.save(imgName)
    return(imgName)

