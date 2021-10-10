from PIL import ImageGrab, ImageOps, Image
import pytesseract
import psutil
from playsound import playsound
from time import sleep
import pathlib
import numpy as np

# for 3440*1440 : (3182,19,3416,39)
localpath = str(pathlib.Path(__file__).parent.resolve())
pytesseract.pytesseract.tesseract_cmd = rf"{localpath}\nwnodedetector\Tesseract-OCR\tesseract.exe"
# screenx =  ImageGrab.grab(bbox=(3191, 19, 3230, 39))
# screeny =  ImageGrab.grab(bbox=(3277, 19, 3321, 39))
screen = ImageGrab.grab(bbox=(3191, 19, 3440, 39))
img = screen.convert('RGB')
z = ImageOps.crop(img, (173,0,50,0))
zpos = pytesseract.image_to_string(z, config="--psm 13 outputbase digits")
zpos = str(zpos).replace('\n', '').replace('\x0c', '').replace('(', '').replace(']', '').replace('[', '')
if zpos.isdigit() and int(float(zpos)) >= 100:
    xcrop = (0,0,220,0)
    ycrop = (82,0,128,0)
    print('ge100')
else:
    xcrop = (0,0,210,0)
    ycrop = (88,0,120,0)
    print('l100')
x = ImageOps.crop(img, xcrop)
y = ImageOps.crop(img, ycrop)
x = x.resize((150, 100))
y = y.resize((150, 100))
z = z.resize((150, 100))
print(zpos)
datax = np.array(x)
datay = np.array(y)
r1, g1, b1 = 235, 235, 165
r1x, g1x, b1x = 110, 105, 70
r2, g2, b2 = 0, 0, 0
redx, greenx, bluex = datax[:,:,0], datax[:,:,1], datax[:,:,2]
redy, greeny, bluey = datay[:,:,0], datay[:,:,1], datay[:,:,2]
mask1x = (redx <= r1x) & (greenx <= g1x) & (bluex <= b1x)
mask2x = (redx >= r1) & (greenx >= g1) & (bluex >= b1)
mask1y = (redy <= r1x) & (greeny <= g1x) & (bluey <= b1x)
mask2y = (redy >= r1) & (greeny >= g1) & (bluey >= b1)
datax[:,:,:3][mask1x] = [r2, g2, b2]
datax[:,:,:3][mask2x] = [r2, g2, b2]
datay[:,:,:3][mask1y] = [r2, g2, b2]
datay[:,:,:3][mask2y] = [r2, g2, b2]
x = Image.fromarray(datax)
y = Image.fromarray(datay)
x.convert("L")
y.convert("L")
x.show()
y.show()
z.show()
xpos = pytesseract.image_to_string(x, config="--psm 13 outputbase digits")
ypos = pytesseract.image_to_string(y, config="--psm 13 outputbase digits")

xpos = str(xpos).replace('\n', '').replace('\x0c', '').replace('(', '').replace(']', '').replace('[', '')
ypos = str(ypos).replace('\n', '').replace('\x0c', '').replace('(', '').replace(']', '').replace('[', '')

pos = [xpos, ypos]
print(pos)