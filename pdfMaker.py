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