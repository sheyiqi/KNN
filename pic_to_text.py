from PIL import Image
#图片处理
#先将所有图片转为固定宽高，比如32*32，然后再转为文本
#pillow
im=Image.open("C:/Users/me/Pictures/weixin3.jpg")
fh=open("C:/Users/me/Pictures/weixin3.txt","a")
#im.save("C:/Users/me/Pictures/weixin.bmp")
width=im.size[0]
height=im.size[1]
#k=im.getpixel((1,9))
#print(k)
for i in range(0,width):
    for j in range(0,height):
        cl=im.getpixel((i,j))
        clall=cl[0]+cl[1]+cl[2]
        if(clall==0):
            #黑色
            fh.write("1")
        else:
            fh.write("0")
    fh.write("\n")
fh.close()
