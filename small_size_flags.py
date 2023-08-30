from tools import backGround, pdfMaker, filter
from PIL import Image, ImageDraw, ImageFont
import os
import pandas as pd

textFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 80)
nameFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 90)
statFont = ImageFont.truetype('fonts/Inconsolata_Condensed-Regular.ttf', size = 60)
signsFont = ImageFont.truetype('fonts/Neucha.ttf', size = 60)
copmNameFont = ImageFont.truetype('fonts/Neucha.ttf', size = 85)
windowColor = '#F4F4F4'
outlineWidht = 5



def main(csv, compN, color):
    print('creating small nametags...', color)
    data = pd.read_csv(csv)

    tags_array = [] #storing image names to delete after creating pdf

    data = data.to_dict('records')
    print(data)

    for row in data:
        name = filter.empty_to_placeholder(row["Name"])
        WCA_ID = filter.empty_to_placeholder(row["WCA ID"])
        country = row["Country"]
        print(name, WCA_ID, country)

        refactored_country = country.replace(" ", "-")#changes country name to png naming format
        country_flag = Image.open(f'flags/{refactored_country}.png').resize((200,200))
        tag_name = f'{name}-{WCA_ID}.png'

        nametag = backGround.make_small_bg(tag_name, color)
        nametag_to_edit = Image.open(tag_name)

        draw = ImageDraw.Draw(nametag_to_edit)
        #name rectangle
        draw.rounded_rectangle([(50, 250),(994, 400)], radius = 40, fill = windowColor, outline='black', width = outlineWidht)
        #competition name
        draw.text((522, 100), text = compN, font = copmNameFont, fill = 'black', anchor = 'mm')
        #person name
        draw.text((522, 325), text = name, font = nameFont, fill = 'black', anchor = 'mm' )
        #WCA Id
        draw.text((40, 615), text = WCA_ID,font = signsFont, fill ='black', anchor = 'lb')
        #add flag
        nametag_to_edit.paste(country_flag,(804,465),country_flag)

        
        nametag_to_edit.save(tag_name)
        tags_array.append(tag_name)

    path = pdfMaker.generate_pdfs(tags_array)
    for tag in tags_array:
        print('cleaning...')
        os.remove(tag)
    return(path)


if __name__=='__main__':
    a = main('new.csv', 'Prague Open 2023', '#C3A9EE')
    #82B36A
