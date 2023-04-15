from PIL import Image, ImageDraw, ImageFont, ImageOps
from tools import pdfMaker
import os

########################################### PLACE FOR GLOBAL VARIABLES ############################################################
textFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 80)
botTextFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 70)
nameFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 85) #actually compName font
statFont = ImageFont.truetype('fonts/Inconsolata_Condensed-Regular.ttf', size = 60)
signsFont = ImageFont.truetype('fonts/Inconsolata_Condensed-Regular.ttf', size = 40)
eventNameFont = ImageFont.truetype('fonts/Inconsolata_Condensed-Regular.ttf', size = 38)
windowColor = '#F4F4F4'
eventColor = '#DDD9D8'
eventOutline = '#C6C2C1'
outlineWidht = 3
####################################################################################################################################

def main(compN, names_array, template, date):
    print('creating nametags...')
    for name in names_array:
        img_to_make = make_bg_img(template, compN)
        draw = ImageDraw.Draw(img_to_make)

def make_bg_img(path, compName):
    bg_image = path

    bgToMake = Image.open(bg_image)
    bgToMake = bgToMake.resize((764, 1024))
    draw = ImageDraw.Draw(bgToMake)  

    ### structures ###
    #name 
    draw.rounded_rectangle([(50, 185),(714,285)], radius = 5, fill = eventColor, outline = 'gray', width = 2)
    #white bottom
    draw.rectangle([(0, 1024), (764, 894)], fill = eventColor)
    #white top
    draw.rectangle([(0,0),(764, 130)], fill = eventColor)
    #outline
    draw.rectangle([(0,0), (764, 1024)], outline = 'black', width = 3)

    ### text ###
    #comp name
    draw.text((382,65), text = compName, anchor = 'mm', font = nameFont, fill = 'black')

    return(bgToMake)

