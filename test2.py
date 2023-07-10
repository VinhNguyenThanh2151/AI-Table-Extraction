# Import the Pillow library
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import numpy as np
import warnings
import xml.etree.ElementTree as ET
import random
warnings.filterwarnings("ignore")
tree = ET.parse('header.xml')
root = tree.getroot()
df = pd.read_excel(r"C:\Users\Administrator\Downloads\Test (1) (1).xlsx")
col = [205,280,422,650,852,972,1072,1225,1293,1828]
col2 = [205,280,422,650,852,972,1072,1225,1293,1410,1516,1646,1828]
row = 0
number_row = 6
cell_of_row = [4]
final_word = [1,2,3]
number_table = 4
content = ["Tôi","Bách", "Khoa", "toán", "lý", "hóa", "văn", "anh","sinh","thể", "địa","Chào","hoạt", "chạy","nhảy", "đá","sút", "ném", "ngã", "vấp","qua","trượt", "AI","thầy", "cô","trò", "bắt", "đánh","yêu", "ghét", "A", 0,1,2,3,4,5,6,7,8,9,10,11,12, "ông", "bà","họp", "chính", "phụ"]
content2 = ["Cái/túi", "01 cái/túi", "túi 50 cái", "50 cái/hộp","Hộp 50 cái"]
cell_CCHN = ["N03.", "N07.", "N08."]
tien1 = ["3450.00","2900.00","8400.00","575.00","1571.00","1,841,510.86","2,447,000.00","900,000.00","250,000.00"]
local_in_xml =[6,7,8,9,10,11,13,14,15,16,17,19,20]
# content =["1", " ", "1", "Theo dõi huyết áp liên tục không xâm nhập tại giường ≤ 8 giờ trong một ngày bất kỳ trong tuần", "X", "X","X"," "]
# content2 =["2", " ", "1", "Theo dõi huyết áp liên tục không xâm nhập tại giường ≤ 8 giờ trong một ngày", "X", "X","X"," "]
fnt = ImageFont.truetype("timesbd.ttf",24)
# Create a new image with the given size and color
name_for_cell = ["bơm", "sử", "dụng", "để", "bơm", "thức", "ăn", "cho", "người", "và", "các"]
img = Image.new("RGB", (2339, 1654), "white")
d = ImageDraw.Draw(img)
draw = ImageDraw.Draw(img)
def Draw_table(img, row, color = 'black', width = 3 ):
# Create a draw object to draw on the image
    
# Draw a horizontal line 
    for i in range(row +1):
        draw.line((205,345+ (i+4)*47, 1830,345+ (i+4)*47), fill= color, width=width)
# Draw a vertical line 
    for j in col:
        draw.line((j,345,j, 345+(row+4)*47), fill = color, width =width)
    draw.line((205,345, 1830,345), fill= color, width=width)
    draw.line((1293,345+1*47, 1828,345+1*47), fill= color, width=width)
    draw.line((1516,345+1*47, 1516,345+4*47), fill= color, width=width)
    draw.line((1646,345+1*47, 1646,345+4*47), fill= color, width=width)
    draw.line((1293,438, 1516,438), fill= color, width=width)
    draw.line((1410,438, 1410,345+4*47), fill= color, width=width)

    #draw.line((175+col[1],100+3*47,175+col[3],100+3*47), fill = color, width = width)
    #draw.line((175+col[4],100+3*47,175+col[5],100+3*47), fill = color, width = width)
#Draw column 4/5
    #col4 = (col[5]-col[4])/4
    #for k in range(4):
        #draw.line((205+col[4]+k*col4, 345 +3*47,205+col[4]+k*col4, 345+(row+4)*47 ), fill = color, width = width)
    return img

def Set_Text_Header(img, fnt, fill = "black"):
    draw.text(((col[0]+col[1])/2,345+2*47), "STT", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[1]+col[2])/2,345+47/2), "Mã số theo", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[1]+col[2])/2,345+1*47+47/2), "rawanh mục", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[1]+col[2])/2,345+2*47+47/2), "BHYT ban", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[1]+col[2])/2,345+3*47+47/2), "hành", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[2]+col[3])/2,345+1*47+47/2), "Tên VTYT theo danh", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[2]+col[3])/2,345+2*47+47/2), "mục BYT ban hành", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[3]+col[4])/2,345+2*47), "Tên thương mại", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[4]+col[5])/2,345+2*47), "Quy cách", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[5]+col[6])/2,345+1*47+47/2), "Đơn vị", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[5]+col[6])/2,345+2*47+47/2), "tính", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[6]+col[7])/2,345+1*47+47/2), "Giá mua vào", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[6]+col[7])/2,345+2*47+47/2), "(đồng)", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[7]+col[8])/2,345+1*47), "Mã", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[7]+col[8])/2,345+2*47), "gói", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[7]+col[8])/2,345+3*47), "thầu", font= fnt, fill=fill, anchor="mm")
    draw.text(((col[8]+col[9])/2,345+47/2), "Đề nghị", font= fnt, fill=fill, anchor="mm")
    draw.text(((col2[11]+col2[12])/2,345+2*47+47/2), "Thành tiền (đồng)", font= fnt, fill=fill, anchor="mm")
    draw.text(((col2[10]+col2[11])/2,345+1*47+47/2), "Giá thanh", font= fnt, fill=fill, anchor="mm")
    draw.text(((col2[10]+col2[11])/2,345+2*47+47/2), "toán BHYT", font= fnt, fill=fill, anchor="mm")
    draw.text(((col2[10]+col2[11])/2,345+3*47+47/2), "(đồng)", font= fnt, fill=fill, anchor="mm")
    draw.text(((col2[9]+col2[10])/2,345+3*47), "Nội trú", font= fnt, fill=fill, anchor="mm")
    draw.text(((col2[8]+col2[9])/2,345+3*47), "Ngoại trú", font= fnt, fill=fill, anchor="mm")
    draw.text(((col2[8]+col2[10])/2,345+1*47+47/2), "Số lượng", font= fnt, fill=fill, anchor="mm")
    return img
def Set_content(img, fnt, fill = "black",width = 3):
    L = 0
    LT = 0
    P = 345 + 4*47
    for a in range(9):
        row1 = df.iloc[a]
        r = np.asarray(row1)
        for i in range(len(r)):
            if pd.isna(r[i]):
                r[i]=" "
            content = r.tolist()
        for i in range(len(content)):
            c_width, c_height = draw.textsize(str(content[i]), fnt)
            line = int(c_width/(col2[i+1]-col2[i]-16))+1 
            if line > L:
                L = line
        LT += L  
        S = L
        L=0     
        draw.line((205,P + 47*LT, 1828,P + 47*LT), fill= fill, width=width)
        for j in col2:
            draw.line((j,345+4*47,j, 345+(LT+4)*47), fill = fill, width =width)
        P = 345+(L+4)*47


        for j in range(len(content)):
        # d.text((175+col[1]/2,100+3*47/2), header[0], font= fnt, fill=fill, anchor="mm")
        # d.text((175+(col[2]+col[1])/2,100+3*47/2), header[1], font= fnt, fill=fill, anchor="mm")
            
            if j == 3:
                print(content[j])
                dd = str(content[j]).split()
                h_width, h_height = draw.textsize(str(content[j]), fnt)
                s =[]
                g =[]
                if h_width < (col2[j+1]-col2[j] - 16):
                    d.text((col2[j]+16,345+(4+LT-(S-1)-1/2)*47), content[j], font= fnt, fill=fill,anchor = "lm")
                else:
                    for i in dd:
                        s.append(i)
                        ss = " ".join(s)   
                        text_width, text_height = draw.textsize(ss, fnt)
                        line = int(h_width/(col2[j+1]-col2[j]-16))+1 #số dòng của dữ liệu   
                        print(line)            
                        if text_width > col2[j+1]-col2[j]-16: 
                            vs = s.pop()
                            L_1 =" ".join(s)
                            d.text((col2[j]+16,345+(4+LT-(S-1)-1/2)*47), L_1, font= fnt, fill=fill,anchor = "lm")
                            ff = set(s)^set(dd)  

                    for k in ff:
                        H1 = " ".join(ff)
                        h1_width, h1_height = draw.textsize(H1, fnt)
                        g.append(k)
                        gg = " ".join(g)   
                        text_width, text_height = draw.textsize(gg, fnt)
                        line = int(h_width/(col2[j+1]-col2[j]-16))+1 #số dòng của dữ liệu 
                        if h1_width < col2[j+1]-col2[j]:
                            draw.text((col2[j]+16,345+(4+LT-(S-2)-1/2)*47),H1 , font= fnt, fill=fill,anchor = "ls")       
                        else:
                            vs = g.pop()
                            L_2 =" ".join(g)
                            draw.text((col2[j]+16,345+(4+LT-(S-2)-1/2)*47), L_2, font= fnt, fill=fill,anchor = "ls")
                continue
            
            draw.text(((col2[j+1] +col2[j])/2 , 345+(4+LT-S+(S/2))*47), str(content[j]), font= fnt, fill=fill,anchor = "mm")
            
    return img
def Set_content_2(img, fnt,fill = "black",width = 3 ):    
    L = 0
    ymax_0 = 535
    for i in range(number_row):
        Line = 1
        content_cell_last =[]
        content_cell_last1 =[]
        tien = []
        random_cell = random.choice(cell_of_row)
        L += random_cell
        P = 345 + (L+4)*47
        draw.line((205,P, 1830,P), fill= fill, width=width)
        for j in col2:
            draw.line((0+j,345+4*47,0+j, 345+(L+4)*47), fill = fill, width =width)
            draw.text(((col[0]+col[1])/2,345+(2+L)*47), str(i+1), font= fnt, fill=fill, anchor="mm")
        # print(random_cell)
        # tiền
        tien.append(str(random.choice(tien1)))
        tien_write = " ".join(tien)
        draw.text((col2[7]-8,345+(2+L)*47), tien_write, font= fnt, fill=fill,anchor = "rm")
        #  mã số
        CCHN1 = random.choice(cell_CCHN)
        CCHN2 = Set_number_CCHN()
        CCHN3 = Set_number_CCHN1()
        #Tên VTYT theo danh mục
        Line4 = 0
        while Line4 < random_cell-1:
            content_cell4 = []   
            text_width = 0
            while text_width < col[3]-col[2]-10:
                content_cell4.append(str(random.choice(name_for_cell)))
                content_write4 = " ".join(content_cell4)   
                text_width, text_height = draw.textsize(content_write4, fnt)
            content_cell4.pop()
            content_write4 = " ".join(content_cell4)
            draw.text(((col[2]+col[3])/2,345+47+(L+3 - random_cell )*47 + 47/2 + 47*Line4),content_write4 , font= fnt, fill=fill, anchor="mm")
            Line4 +=1
        content_last_line = []
        for m in range(random.randint(1,5)):
            content_last_line.append(str(random.choice(name_for_cell)))
        content_write_last = " ".join(content_last_line)
        draw.text(((col[2]+col[3])/2,345+47+(L+3)*47 - 47/2),content_write_last , font= fnt, fill=fill, anchor="mm")
        # print(type(random.choice(cell_CCHN)))
        draw.text((155+(col[0]+col[1])/2,345+(2+L)*47),CCHN1 + CCHN3 +"."+ CCHN2 , font= fnt, fill=fill, anchor="rm")
        draw.text((205+(col[0]+col[1])/2,345+(L+4-1/2)*47), "", font= fnt, fill=fill, anchor="rm")
        while Line < random_cell :           
            
            content_cell = Set_content_for_a_cell(fnt)
            # print(content_cell)
            content_cell.pop()
            content_write = " ".join(content_cell)   
            draw.text((0+col2[3]+16,345+(4+L-(random_cell-Line)-1/2)*47), content_write, font= fnt, fill=fill,anchor = "lm")
            # content_cell = content_next_line
            # print(content_cell)
            Line +=1
        for i in range(random.choice(final_word)):
            content_cell_last.append(str(random.choice(content)))
        content_write_last = " ".join(content_cell_last)
        draw.text((0+col2[3]+16,345+(4+L-1/2)*47), content_write_last, font= fnt, fill=fill,anchor = "lm")
        draw.text((0+(col2[5]+col2[6])/2,345+(L+2)*47), "cái", font= fnt, fill=fill,anchor = "mm")
        draw.text((0+(col2[8]+col2[9])/2,345+(L+2)*47), "0", font= fnt, fill=fill,anchor = "lm")
        
        content_cell_last1.append(str(random.choice(content2)))
        content_write_last1 = " ".join(content_cell_last1)
        draw.text((col2[4]+8,345+(2+L)*47), content_write_last1, font= fnt, fill=fill,anchor = "lm")
    #label
         # label table row 
        object = ET.SubElement(root, "object")

        name = ET.SubElement(object, "name")
        name.text = "Table row"

        pose = ET.SubElement(object, "pose")
        pose.text = "Unspecified"

        truncated = ET.SubElement(object, "truncated")
        truncated.text = "0"

        difficult = ET.SubElement(object, "difficult")
        difficult.text = "0"

        bndbox = ET.SubElement(object, "bndbox")

        xmin = ET.SubElement(bndbox, "xmin")
        xmin.text = str(207)

        ymin = ET.SubElement(bndbox, "ymin")
        ymin.text = str(ymax_0)

        xmax = ET.SubElement(bndbox, "xmax")
        xmax.text = str(1829)

        ymax = ET.SubElement(bndbox, "ymax")
        ymax.text = str(ymax_0 + random_cell*47)

        ymax_0 = ymax_0 + random_cell*47
    # Kéo dài các table column và table
    for n in local_in_xml:
        root[n][4][3].text = str(int(root[n][4][3].text) + L*47)
    tree.write("filename.xml")
    
    return img
def Set_content_for_a_cell(fnt):
    content_cell = []
    
    text_width = 0
    while text_width < (col2[4]-col2[3] - 16):
        content_cell.append(str(random.choice(content)))
        content_write = " ".join(content_cell)   
        text_width, text_height = draw.textsize(content_write, fnt)
    
    return(content_cell)

def Set_number_CCHN():
    number_CCHN = []
    for i in range(3):
        number_CCHN.append(str(random.randint(0,9)))
    CCHN = "".join(number_CCHN)
    return CCHN
def Set_number_CCHN1():
    number_CCHN1 = []
    for i in range(2):
        number_CCHN1.append(str(random.randint(0,9)))
    CCHN = "".join(number_CCHN1)
    return CCHN
#Run 
###img = Set_content(img, fnt)

#img = Set_content(img, fnt)


#img.show()
# Save the image to a file
for i in range(number_table):
    img = Image.new("RGB", (2339, 1654), "white")
    draw = ImageDraw.Draw(img)
    img = Draw_table(img, row)
    img = Set_Text_Header(img, fnt)
    # img = Set_content(img, fnt)
    img = Set_content_2(img,fnt)
    tree = ET.parse('filename.xml')
    # tree = ET.ElementTree(root)
    tree.write(f'Table_{i}.xml')
    img.save(f'Table_{i}.png')
    img.show()   