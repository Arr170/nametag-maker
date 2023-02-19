from fpdf import FPDF

def generate_pdfs(data):
    pdf = FPDF()
    image_count = 0
    i = 0
    #print(len(data))
    for image in data:
        if(i == 0): 
            pdf.add_page()
            pdf.image(image, x = 10, y = 10, w = 80, h = 50 )
            image_count += 1
            #print(i, image)
            i += 1
        elif(i == 1): 
            pdf.image(image, x = 100, y = 10, w = 80, h = 50)
            image_count += 1
            #print(i, image)
            i += 1
        elif(i == 2):
            pdf.image(image, x = 10, y = 70, w = 80, h = 50)
            image_count += 1
            #print(i, image)
            i += 1
        elif(i == 3): 
            pdf.image(image, x = 100, y = 70, w = 80, h = 50)
            image_count += 1
            #print(i, image)
            i += 1
        elif(i == 4):
            pdf.image(image, x = 10, y = 130, w = 80, h = 50)
            image_count += 1
            #print(i, image)
            i += 1
        elif(i == 5):
            pdf.image(image, x = 100, y = 130, w = 80, h = 50)
            image_count += 1
            #print(i, image)
            i += 1
        elif(i == 6):
            pdf.image(image, x = 10, y = 190, w = 80, h = 50)
            image_count += 1
            #print(i, image)
            i += 1
        elif(i == 7):
            pdf.image(image, x = 100, y = 190, w = 80, h = 50)
            image_count += 1
            #print(i, image)
            i = 0
        
    pdf.output("namecards.pdf")

def generate_big_pdf(data):
    ### demo pdf, should be finished ###
    print('creating pdf file...')
    pdf = FPDF()
    image_count = 0
    i = 0
    for image in data:
        if(i == 0):
            pdf.add_page()
            pdf.image(image, x = 3, y = 3, w = 100, h = 145)
            print('inserting', image)
            i += 1
        elif(i == 1):
            pdf.image(image, x = 106, y = 3, w = 100, h = 145)
            print('inserting', image)
            i += 1
        elif(i == 2):
            pdf.image(image, x = 3, y = 150, w = 100, h = 145)
            print('inserting', image)
            i += 1
        elif(i == 3):
            pdf.image(image, x = 106, y = 150, w = 100, h = 145)
            print('inserting', image)
            i = 0

    pdf.output("big_namecadrs.pdf")