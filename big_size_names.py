from PIL import Image, ImageDraw, ImageFont, ImageOps
from tools import pdfMaker, filter
import os
import pandas as pd
########################################### PLACE FOR 'GLOBAL' VARIABLES ############################################################
textFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 80)
nameFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 85) #actually compName font
dateFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 70)
windowColor = '#F4F4F4'

eventOutline = '#C6C2C1'
outlineWidht = 3
####################################################################################################################################


def main(compN, csv, template, date):
    print('creating nametags...', template)
    if (template == 'bg_1.png'):
        bgColor = '#DDD9D8'
    else:
        bgColor = '#D3E2C1'
    
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
        img_to_make = make_bg_img(template, compN, date, bgColor)
        draw = ImageDraw.Draw(img_to_make)
        img_name = f'{name}.png'
        #writing name into card
        draw.text((382,339), text = name, font = textFont, anchor = 'mm', fill = 'black')
        #writing wca ID
        draw.text((382, 550), text = WCA_ID, font = dateFont, anchor = 'mm', fill  = 'black')
        img_to_make.save(img_name)
        array_to_delete.append(img_name)
        print(array_to_delete)

    path = pdfMaker.generate_big_pdf(array_to_delete)

    print('cleaning...')
    for image in array_to_delete:
        print('removing', image)
        os.remove(image)
    
    return(path)

def make_bg_img(path, compName, date, bgColor):
    bg_image = path

    bgToMake = Image.open(bg_image)
    bgToMake = bgToMake.resize((764, 1024))
    draw = ImageDraw.Draw(bgToMake)  

    ### structures ###
    #name 
    draw.rounded_rectangle([(50, 285),(714,400)], radius = 5, fill = bgColor, outline = 'gray', width = 2)
    #wca ID
    draw.rounded_rectangle([(230, 500),(534,600)], radius = 5, fill = bgColor, outline = 'gray', width = 2)
    #date 
    draw.rounded_rectangle([(230, 700),(534,800)], radius = 5, fill = bgColor, outline = 'gray', width = 2)
    #white bottom
    draw.rectangle([(0, 1024), (764, 894)], fill = bgColor, outline = 'gray')
    #white top
    draw.rectangle([(0,0),(764, 150)], fill = bgColor, outline = 'gray')
    #outline
    draw.rectangle([(0,0), (764, 1024)], outline = 'black', width = 3)

    ### text ###
    #comp name
    draw.text((382,75), text = compName, anchor = 'mm', font = nameFont, fill = 'black')
    draw.text((382, 750), text = date, font = dateFont, anchor = 'mm', fill = 'black')

    return(bgToMake)

#a = main('idk', './uploaded/new.csv', 'bg_1.png', 'nonoe')