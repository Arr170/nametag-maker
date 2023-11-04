from PIL import Image, ImageDraw, ImageFont, ImageOps
from tools import pdfMaker, filter
import os
import pandas as pd
########################################### PLACE FOR 'GLOBAL' VARIABLES ############################################################
textFont = ImageFont.truetype('fonts/Sumana-Bold.ttf', size = 65)#for max name lengh 20 (including space)
longTextFont = ImageFont.truetype('fonts/Sumana-Bold.ttf', size = 55)#for names 20-22 characters  (including space)
nameFont = ImageFont.truetype('fonts/Sumana-Regular.ttf', size = 85) #actually compName font
idFont = ImageFont.truetype('fonts/Sumana-Bold.ttf', size = 50)
signsFont = ImageFont.truetype('fonts/Sumana-Regular.ttf', size = 50)
dateFont = ImageFont.truetype('fonts/Sumana-Bold.ttf', size = 55)
windowColor = '#E8E8E8'
eventOutline = '#C6C2C1'
outlineWidht = 3
####################################################################################################################################


def main(compN, csv, color, date):
    print('creating nametags...', color)
    names = pd.read_csv(csv)#csv from wca
   
    array_to_delete = [] #storing image names to delete after creating pdf

    names = names.to_dict('records')
    print(names,'\n')
    for row in names:
        name = filter.empty_to_placeholder(row["Name"])
        WCA_ID = filter.empty_to_placeholder(row["WCA ID"])
        country = row["Country"]
        print(name, WCA_ID)
        refactored_country_name = country.replace(" ", "-")#changes country name to png naming format

        img_to_make = make_bg_img(color, compN, date, windowColor, refactored_country_name)
        draw = ImageDraw.Draw(img_to_make)


        img_name = f'{name}-{WCA_ID}.png'
        #writing name into card
        if len(name) < 20:
            draw.text((382,289), text = name, font = textFont, anchor = 'mm', fill = 'black')
        else:
            draw.text((382,289), text = name, font = longTextFont, anchor = 'mm', fill = 'black')
        #writing wca ID
        draw.text((225, 500), text = WCA_ID, font = idFont, anchor = 'mm', fill  = 'black')
        img_to_make.save(img_name)
        array_to_delete.append(img_name)
        print(array_to_delete)

    path = pdfMaker.generate_big_pdf(array_to_delete)

    print('cleaning...')
    for image in array_to_delete:
        try:
            print('removing', image)
            os.remove(image)
        except Exception as e:
            print(e)
    return(path)

def make_bg_img(color, compName, date, bgColor, country_name):
    
    bgToMake = Image.new(mode = 'RGB', size = (764, 894), color = color)
    draw = ImageDraw.Draw(bgToMake)  
    country_flag = Image.open(f'flags/{country_name}.png').resize((120,100))
    logo = Image.open('logochampionship.png').resize((350,350))

    ### structures ###
    #name 
    draw.text((90, 226), text = 'Name:', anchor='lb', fill = 'black', font = signsFont)
    draw.rounded_rectangle([(50, 235),(714,350)], radius = 40, fill = bgColor, outline = 'black', width = 2)
    #wca ID
    draw.text((90, 440), text = 'WCA ID:', anchor='lb', fill = 'black', font = signsFont)
    draw.rounded_rectangle([(50, 450),(400,550)], radius = 40, fill = bgColor, outline = 'black', width = 2)
    #date 
    draw.text((90, 640), text = 'Date:', anchor='lb', fill = 'black', font = signsFont)
    draw.rounded_rectangle([(50, 650),(350,750)], radius = 40, fill = bgColor, outline = 'black', width = 2)
    #outline
    draw.rectangle([(0,0), (764, 894)], outline = 'black', width = 3)
    #add flag
    bgToMake.paste(country_flag,(510,450, 630, 550),country_flag)
    #add logo
    bgToMake.paste(logo,(400,550),logo)

    ### text ###
    #comp name
    draw.text((382,75), text = compName, anchor = 'mm', font = nameFont, fill = 'black')
    #date
    draw.text((200, 700), text = date, font = dateFont, anchor = 'mm', fill = 'black')

    return(bgToMake)

def image_to_mask(img):
    img = img.convert("L")
    img = ImageOps.colorize(img, black = 'white', white = 'black').convert("L")
    return(img)

def image_to_paste(img):
    return(img.convert("L"))

if __name__=='__main__':
    a = main('Prague Open 2023', 'new.csv', '#C3A9EE', '17-18.6.')
    #82B36A