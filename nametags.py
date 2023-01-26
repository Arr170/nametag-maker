#from cardmaker import make_card
from cards import oneStatCard, twoStatCard, threeStatCard
from pdfMaker import generate_pdfs
from backGround import choose_bg
import os

import pandas as pd
import sys

try:
    csvToRead = sys.argv[1]
except IndexError:
    print("[E] Syntax Error; Usage: python testing_main.py csvToRead.csv")
    exit()

#storing names of cards files
imgArrey = []

df = pd.read_csv(csvToRead)

stats = df.to_dict(orient='record')

#asking for data
compName = str(input('[a] name of the competition: '))
namecardMode = int(input('[a] how many stat do u want to place (maximum of 3 stats):'))
#warning if wrong number
if(namecardMode > 3):
    namecardMode = int(input('[!] maximum of 3 stats! '))

if(namecardMode == 1):
    bg_color = choose_bg()
    columnNameStat1 = str(input('[a] column name for stat 1: '))
    statName1 = str(input('[a] name for stat 1: '))
    date = str(input('[a] date of the comp in format dd-dd.mm: '))
    for stat in stats:
        img = oneStatCard.make_card(compName, stat['name'], statName1, stat[columnNameStat1], date, bg_color)
        imgArrey.append(img)


elif(namecardMode == 2):
    bg_color = choose_bg()
    columnNameStat1 = str(input('[a] column name for stat 1: '))
    columnNameStat2 = str(input('[a] column name for stat 2: '))  
    statName1 = str(input('[a] name for stat 1: '))
    statName2 = str(input('[a] name for stat 2: '))
    for stat in stats:
        img = twoStatCard.make_card(compName, stat['name'], statName1, statName2, stat[columnNameStat1], stat[columnNameStat2], bg_color)
        imgArrey.append(img)
elif(namecardMode == 3):
    bg_color = choose_bg()
    columnNameStat1 = str(input('[a] column name for stat 1: '))
    columnNameStat2 = str(input('[a] column name for stat 2: '))   
    columnNameStat3 = str(input('[a] column name for stat 3: '))
    statName1 = str(input('[a] name for stat 1: '))
    statName2 = str(input('[a] name for stat 2: '))
    statName3 = str(input('[a] name for stat 3: '))
    date = str(input('[a] date of the comp in format dd-dd.mm'))
    for stat in stats:
        img = threeStatCard.make_card(compName, stat['name'], statName1, statName2, statName3, stat[columnNameStat1], stat[columnNameStat2], stat[columnNameStat3], date, bg_color)
        imgArrey.append(img)

generate_pdfs(imgArrey)
for img in imgArrey:
    os.remove(img)



