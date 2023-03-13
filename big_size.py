from PIL import  Image, ImageDraw, ImageFont, ImageOps
from backGround import make_bg
import pandas as pd
import csv
import pdfMaker
import os
import inquirer



########################################### PLACE FOR GLOBAL VARIABLES ############################################################
textFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 80)
nameFont = ImageFont.truetype('fonts/Inconsolata_Condensed-SemiBold.ttf', size = 90)
statFont = ImageFont.truetype('fonts/Inconsolata_Condensed-Regular.ttf', size = 60)
signsFont = ImageFont.truetype('fonts/Inconsolata_Condensed-Regular.ttf', size = 40)
eventNameFont = ImageFont.truetype('fonts/Inconsolata_Condensed-Regular.ttf', size = 38)
copmNameFont = ImageFont.truetype('fonts/Neucha.ttf', size = 85)
windowColor = '#F4F4F4'
eventColor = '#DDD9D8'
eventOutline = '#C6C2C1'
outlineWidht = 3
####################################################################################################################################

def event_writer(img_to_write, data, column_names):
    
    for n in range(len(data)):
        pos = 0
        for name in (column_names):
            if(name == 'Name'): img_to_write.text((382,275), text = events.loc[n, name], font = textFont, anchor = 'mm', fill = 'black')
            if(name != 'Name'):
                position = box_position_switch(pos)
                img_to_write.rectangle(position[0], fill = eventColor, outline = eventOutline, width = outlineWidht)
                img_to_write.rectangle(position[1], fill = eventColor, outline = eventOutline, width = outlineWidht)
                pos += 1
                

        break

def event_switch(event):
    #print('in switch:', event)
    if(event == '222'): return(r'png_events\222.PNG')
    if(event == '333'): return(r'png_events\333.png')
    if(event == '333bf'): return(r'png_events\333bf.png')
    if(event == '333fm'): return(r'png_events\333fm.png')
    if(event == '333mbf'): return(r'png_events\333mbf.png')
    if(event == '333oh'): return(r'png_events\333oh.png')
    if(event == '444'): return(r'png_events\444.png')
    if(event == '444bf'): return(r'png_events\444bf.png')
    if(event == '555'): return(r'png_events\555.png')
    if(event == '555bf'): return(r'png_events\555bf.png')
    if(event == '666'): return(r'png_events\666.png')
    if(event == '777'): return(r'png_events\777.png')
    if(event == 'clock'): return(r'png_events\clock.png')
    if(event == 'minx'): return(r'png_events\minx.png')
    if(event == 'pyram'): return(r'png_events\pyram.png')
    if(event == 'skewb'): return(r'png_events\skewb.png')
    if(event == 'sq1'): return(r'png_events\sq1.png')
    return(event)

def role_filter(role):
    if(type(role)  is not str): return('---')
    else: return(role)

def box_position_switch(pos):
    if(pos == 0): return([[(90,345), (150, 405)],[(170,345),(300,405)], (90,345,150, 405), (235,375)])
    if(pos == 1): return([[(464,345), (524, 405)],[(544,345),(674,405)], (464,345,524, 405), (609, 375)])
    if(pos == 2): return([[(90,415), (150, 475)],[(170,415),(300,475)], (90,415,150, 475), (235, 445)])
    if(pos == 3): return([[(464,415), (524, 475)],[(544,415),(674,475)], (464,415,524, 475), (609, 445)])
    if(pos == 4): return([[(90,485), (150, 545)],[(170,485),(300,545)], (90,485,150, 545), (235, 515)])
    if(pos == 5): return([[(464,485), (524, 545)],[(544,485),(674,545)], (464,485,524, 545), (609, 515)])
    if(pos == 6): return([[(90,555), (150, 615)],[(170,555),(300,615)], (90,555,150, 615), (235, 585)])
    if(pos == 7): return([[(464,555), (524, 615)],[(544,555),(674,615)], (464,555,524, 615), (609, 585)])
    if(pos == 8): return([[(90,625), (150, 685)],[(170,625),(300,685)], (90,625,150, 685), (235, 655)])
    if(pos == 9): return([[(464,625), (524, 685)],[(544,625),(674,685)], (464,625,524, 685), (609, 655)])
    if(pos == 10): return([[(90,695), (150, 755)],[(170,695),(300,755)], (90,695,150, 755), (235, 725)])
    if(pos == 11): return([[(464,695), (524, 755)],[(544,695),(674,755)], (464,695,524, 755), (609, 725)])
    if(pos == 12): return([[(90,765), (150, 825)],[(170,765),(300,825)], (90,765,150, 825), (235, 795)])
    if(pos == 13): return([[(464,765), (524, 825)],[(544,765),(674,825)], (464,765,524, 825), (609, 795)])

def image_to_paste(img):
    return(img.resize((60,60)).convert("L"))

def image_to_mask(img):
    img = img.resize((60,60)).convert("L")
    img = ImageOps.colorize(img, black = 'white', white = 'black').convert("L")
    return(img)

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

def make_card(compN, csv, template):
    print('creating namecards...')
    events = pd.read_csv(csv)
    img_arr = []# arrey for storing images
    column_names = []#storing names of columns
    for column in events:
        column_names.append(column)

    for n in range(len(events)):
        imgToMake = make_bg_img(template, compN)
        draw = ImageDraw.Draw(imgToMake)
        pos = 0
        for name in (column_names):
            if(name == 'Name'): 
                draw.text((382,226), text = events.loc[n, name], font = textFont, anchor = 'mm', fill = 'black')
                img_name = f'{events.loc[n, name]}.png'
            if(name != 'Name'):
                position = box_position_switch(pos)#taking coordinates for boxes and text
                event = event_switch(name)#event image png file name
                img_to_insert = Image.open(event)#opening event image
                role = role_filter(events.loc[n,name])#filtening roles (no role = '---')  
                draw.rounded_rectangle(position[0], radius = 5, fill = eventColor, outline = eventOutline, width = outlineWidht)#making box foe event icon
                draw.rounded_rectangle(position[1], radius = 5, fill = eventColor, outline = eventOutline, width = outlineWidht)#making box for roles text
                imgToMake.paste(image_to_paste(img_to_insert),position[2],image_to_mask(img_to_insert))#event icon
                draw.text(position[3], text = role, fill = 'black', font = signsFont, anchor = 'mm')#event role
                pos += 1#counting for placing event boxes
        
        imgToMake.save(img_name)
        img_arr.append(img_name)            
                
    path = pdfMaker.generate_big_pdf(img_arr)

    print('cleaning...')
    for image in img_arr:
        os.remove(image)
    
    return(path)
    #imgToMake.save('test_.png', format="png")




def main(source_csv, competition_name, template):
    path = make_card(competition_name, source_csv, template)
    return(path)








