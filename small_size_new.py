from tools import backGround, pdfMaker
from PIL import Image, ImageDraw, ImageFont
import os

textFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 80)
nameFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 90)
statFont = ImageFont.truetype('fonts/Inconsolata_Condensed-Regular.ttf', size = 60)
signsFont = ImageFont.truetype('fonts/Neucha.ttf', size = 50)
copmNameFont = ImageFont.truetype('fonts/Neucha.ttf', size = 85)
windowColor = '#F4F4F4'
outlineWidht = 5



def main(names_arrey, compN, color):
    print('started process, names:', names_arrey)
    tags_arrey = []
    for name in names_arrey:
        tag_name = f'{name}.png'
        nametag = backGround.make_small_bg(tag_name, color)
        nametak_to_edit = Image.open(tag_name)
        draw = ImageDraw.Draw(nametak_to_edit)
        #name rectangle
        draw.rounded_rectangle([(50, 250),(994, 400)], radius = 40, fill = windowColor, outline='black', width = outlineWidht)
        #competition name
        draw.text((522, 100), text = compN, font = copmNameFont, fill = 'black', anchor = 'mm')
        #person name
        draw.text((522, 325), text = name, font = nameFont, fill = 'black', anchor = 'mm' )

        
        nametak_to_edit.save(tag_name)
        tags_arrey.append(tag_name)
    path = pdfMaker.generate_pdfs(tags_arrey)
    for tag in tags_arrey:
        print('cleaning...')
        os.remove(tag)
    return(path)



