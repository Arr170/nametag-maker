from PIL import Image, ImageDraw, ImageFont, ImageOps
from tools import pdfMaker, filter
import os
import pandas as pd
########################################### PLACE FOR 'GLOBAL' VARIABLES ############################################################
textFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 80)
nameFont = ImageFont.truetype('fonts/Neucha.ttf', size = 85) #actually compName font
dateFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 70)
signsFont = ImageFont.truetype('fonts/Neucha.ttf', size = 50)
windowColor = '#F4F4F4'

eventOutline = '#C6C2C1'
outlineWidht = 3
####################################################################################################################################


def main(compN, csv, color, date):
    print('creating nametags...', color)
    names = pd.read_csv(csv)
   
    array_to_delete = [] #storing image names to delete after creating pdf

    #storing column names
    column_names = [] 
    for column in names:
        column_names.append(column)
    names = names.to_dict('records')
    print(names,'\n', column_names)
    for row in names:
        name = filter.empty_to_placeholder(row[column_names[0]])
        WCA_ID = filter.empty_to_placeholder(row[column_names[1]])
        print(name, WCA_ID)
        img_to_make = make_bg_img(color, compN, date, windowColor)
        draw = ImageDraw.Draw(img_to_make)
        img_name = f'{name}.png'
        #writing name into card
        draw.text((382,289), text = name, font = textFont, anchor = 'mm', fill = 'black')
        #writing wca ID
        draw.text((200, 500), text = WCA_ID, font = dateFont, anchor = 'mm', fill  = 'black')
        img_to_make.save(img_name)
        array_to_delete.append(img_name)
        print(array_to_delete)

    path = pdfMaker.generate_big_pdf(array_to_delete)

    print('cleaning...')
    for image in array_to_delete:
        print('removing', image)
        os.remove(image)
    
    return(path)

def make_bg_img(color, compName, date, bgColor):
    
    bgToMake = Image.new(mode = 'RGB', size = (764, 894), color = color)
    draw = ImageDraw.Draw(bgToMake)  

    ### structures ###
    #name 
    draw.text((90, 226), text = 'Name:', anchor='lb', fill = 'black', font = signsFont)
    draw.rounded_rectangle([(50, 235),(714,350)], radius = 40, fill = bgColor, outline = 'black', width = 2)
    #wca ID
    draw.text((90, 440), text = 'WCA ID:', anchor='lb', fill = 'black', font = signsFont)
    draw.rounded_rectangle([(50, 450),(350,550)], radius = 40, fill = bgColor, outline = 'black', width = 2)
    #date 
    draw.text((90, 640), text = 'Date:', anchor='lb', fill = 'black', font = signsFont)
    draw.rounded_rectangle([(50, 650),(350,750)], radius = 40, fill = bgColor, outline = 'black', width = 2)
    #outline
    draw.rectangle([(0,0), (764, 894)], outline = 'black', width = 3)

    ### text ###
    #comp name
    draw.text((382,75), text = compName, anchor = 'mm', font = nameFont, fill = 'black')
    #date
    draw.text((200, 700), text = date, font = dateFont, anchor = 'mm', fill = 'black')

    return(bgToMake)


if __name__=='__main__':
    a = main('Prague Open 2023', 'PragueOpen2023-registration.csv', '#B2D866', '17-18.6')
    #82B36A