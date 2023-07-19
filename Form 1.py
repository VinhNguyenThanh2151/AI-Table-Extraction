# Import the Pillow library
from PIL import Image, ImageDraw, ImageFont
#import pandas as pd
#import numpy as np
import random
import xml.etree.ElementTree as ET
tree = ET.parse('header.xml')
root = tree.getroot()
col = [0,65,189,316,498,840,992,1139,1325,1481,1600,1918,2058,2162,2322,2711,2880,3200]
row = 0
header = ["STT", "STT\ntrong\nHSMT", "Mã thuốc", "Tên thuốc","Tên hoạt chất", "Nồng độ,\n hàm lượng", "Nhóm\nthuốc", "SĐK\n hoặc số \n GPNK" , "Dạng bào\n chế/Đường\n dùng", "Quy cách\n đóng gói", "Hãng sản xuất", "Nước sản\n xuất", "Đơn vị\n tính", "Số lượng", "Cơ sở y tế", "Tỉnh/thành \nphố", "Công ty trúng thầu"]
fnt = ImageFont.truetype("timesbd.ttf",25)
number_row = 10
number_table = 1
name_tinh = ["Hà Giang", "Tuyên Quang", "Cao Bằng", "Lạng Sơn", "Lào Cai", "Hà Tĩnh", "Bắc Kạn", "Phú Thọ", "Hoà Bình", "Sơn La", "Yên Bái"]
name_mathuoc = ["A06.N5"]
name_tenthuoc = ["JIMENEZ"]
name_hoatchat = ["Tenofovir disoproxil fumarat"]
Name_nongdo=["300mg"]
Name_SDK = ["VD-30341-18"]
name_nhomthuoc =["Nhóm 5"]
Name_nuocsanxuat = ["Việt Nam"]
Name_Donvitinh = ["Viên"]
name_cosoyte = ["BVDK A", "TTYT B", "BVDK C", "TTKSBT D", "BVDK D", "BVDK E"]
So_luong = ["450", "4.740", "1.350", "12.270", "5.430"]
local_in_xml =[6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
# Create a new image with the given size and color

img = Image.new("RGB", (3500, 2700), "white")

draw = ImageDraw.Draw(img)
def Draw_table(img, row, color = 'black', width = 3 ):
# Create a draw object to draw on the image
    draw.line((175,100, 3375,100), fill= color, width=width)
    
# Draw a horizontal line 
    for i in range(row+1):
        draw.line((175,100+ (i+4)*50, 3375,100+ (i+4)*50), fill= color, width=width)
# Draw a vertical line 
    for j in col:
        draw.line((175+j,100,175+j, 100+(row+4)*50), fill = color, width =width)
    return img

def Set_Text_Header(img, fnt, fill = "black"):
    for j in range(len(header)):
        draw.text((175+(col[j+1]+col[j])/2,100+(row+4)*50/2), header[j], font= fnt, fill=fill, anchor="mm")
    
    return img

def Set_content(img, fnt, fill = "black",width = 3):
    L = 0
    ymax_0 = 300
    tree = ET.parse('header.xml')
    root = tree.getroot()
    for i in range(number_row):
        random_cell = random.randint(4,5)
        name_cell =[]
        L += random_cell
        P = 100 + (L + 4)*50
        draw.line((175,P, 3375,P), fill= fill, width=width)
        for j in col:
            draw.line((175+j,100+3*50,175+j, 100+(L+4)*50), fill = fill, width =width)
        # STT
        draw.text((175+(col[0]+col[1])/2,100+(L+4)*50-(random_cell/2)*50), str(i+1), font= fnt, fill=fill, anchor="mm")
        #STT trong HSMT
        draw.text((175+(col[1]+col[2])/2,100+(L+4)*50-(random_cell/2)*50), str(2), font= fnt, fill=fill, anchor="mm")
        #Ma thuoc
        draw.text((175+(col[2]+col[3])/2,100+(L+4)*50-(random_cell/2)*50), name_mathuoc[0], font= fnt, fill=fill, anchor="mm")
        #ten thuoc
        draw.text((175+(col[3]+col[4])/2,100+(L+4)*50-(random_cell/2)*50), name_tenthuoc[0], font= fnt, fill=fill, anchor="mm")
        #hoat chat
        draw.text((175+(col[4]+col[5])/2,100+(L+4)*50-(random_cell/2)*50), name_hoatchat[0], font= fnt, fill=fill, anchor="mm")
        #nong do
        draw.text((175+(col[5]+col[6])/2,100+(L+4)*50-(random_cell/2)*50), Name_nongdo[0], font= fnt, fill=fill, anchor="mm")
        #nhom thuoc
        draw.text((175+(col[6]+col[7])/2,100+(L+4)*50-(random_cell/2)*50), name_nhomthuoc[0], font= fnt, fill=fill, anchor="mm")
        #sdk
        draw.text((175+(col[7]+col[8])/2,100+(L+4)*50-(random_cell/2)*50), Name_SDK[0], font= fnt, fill=fill, anchor="mm")
        #dang bao che
        draw.text((175+(col[8]+col[9])/2,100+(L+4)*50-(random_cell/2)*50), str('viên nén \n bao phim'), font= fnt, fill=fill, anchor="mm")
        #quy cach
        draw.text((175+(col[9]+col[10])/2,100+(L+4)*50-(random_cell/2)*50), str('Hộp 3 vỉ \n x 10 viên'), font= fnt, fill=fill, anchor="mm")
        #hang san xuat
        draw.text((175+(col[10]+col[11])/2,100+(L+4)*50-(random_cell/2)*50), str('Công ty cổ phần dược phẩm \n Đạt vi phú'), font= fnt, fill=fill, anchor="mm")
        #nuoc san xuat
        draw.text((175+(col[11]+col[12])/2,100+(L+4)*50-(random_cell/2)*50), Name_nuocsanxuat[0], font= fnt, fill=fill, anchor="mm")
        #don vi tinh
        draw.text((175+(col[12]+col[13])/2,100+(L+4)*50-(random_cell/2)*50), Name_Donvitinh[0], font= fnt, fill=fill, anchor="mm")
        #  Số lượng
        TongSo = random.choice(So_luong)
        draw.text((175+(col[13]+col[14])/2,100+(L+4)*50-(random_cell/2)*50 ),TongSo , font= fnt, fill=fill, anchor="mm")
        # tên tỉnh
        for k in range(random.choice([1])):
            name_cell.append(random.choice(name_tinh))
        name_put_cell = " ".join(name_cell)
        text_width, text_height = draw.textsize(name_put_cell, fnt)
        if text_width < (col[16]-col[15]-10):
            draw.text((175+col[15]+10,100+(L+4)*50-(random_cell/2)*50 ),name_put_cell , font= fnt, fill=fill, anchor="lm")
        else:
            pop_name = name_cell.pop()
            name_put_cell = " ".join(name_cell)
            draw.text((175+col[15]+10,100+(L+4)*50-(random_cell/2)*50 - 50/2 ),name_put_cell , font= fnt, fill=fill, anchor="lm")
            draw.text((175+col[15]+10,100+(L+4)*50-(random_cell/2)*50 + 50/2),pop_name , font= fnt, fill=fill, anchor="lm")
        #Co so y te
        CoSo = random.choice(name_cosoyte)
        draw.text((175+(col[14]+col[15])/2,100+(L+4)*50-(random_cell/2)*50 ),CoSo , font= fnt, fill=fill, anchor="mm")
        #cty trung thau
        draw.text((175+(col[16]+col[17])/2,100+(L+4)*50-(random_cell/2)*50), str('Công ty cổ phần dược phẩm \n Đạt vi phú'), font= fnt, fill=fill, anchor="mm")
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
        xmin.text = str(175)

        ymin = ET.SubElement(bndbox, "ymin")
        ymin.text = str(ymax_0)

        xmax = ET.SubElement(bndbox, "xmax")
        xmax.text = str(3375)

        ymax = ET.SubElement(bndbox, "ymax")
        ymax.text = str(ymax_0 + random_cell*50)

        ymax_0 = ymax_0 + random_cell*50
    
    for n in local_in_xml:
        root[n][4][3].text = str(int(root[n][4][3].text) + L*50)
    tree.write("filename.xml")
    
    return img

    



#Run 
for o in range(number_table):
    img = Image.new("RGB", (3500, 2700), "white")
    draw = ImageDraw.Draw(img)
    img = Draw_table(img, row)
    img = Set_Text_Header(img, fnt)
    img = Set_content(img,fnt)
    tree = ET.parse('filename.xml')
    #tree = ET.ElementTree(root)
    tree.write(f'Table_{o}.xml')
    img.save(f'Table_{o}.png')
    img.show()   
    #img.save("header.png")