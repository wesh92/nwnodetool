"""
New World OCR Node Detector
Created: 2021-10-07
Dev: Wes H.

Uses OCR to get coordinates from top right of the NW game window
and imposes that against a list of possible nodes.
When you're close to one it will play a bell noise!
"""
import winsound
from PIL import ImageGrab, ImageOps, Image
import pytesseract
import psutil
from time import sleep
import pathlib
import iron_markers as imark
import essence_markers as emark
import chest_essence as ce
import numpy as np

# for 3440*1440 : (3182,19,3416,39)
localpath = str(pathlib.Path(__file__).parent.resolve())
pytesseract.pytesseract.tesseract_cmd = rf"{localpath}\Tesseract-OCR\tesseract.exe"
# node = [['7831', '1673'], ['9341', '2725']] 
node = ce.chest_essence
def screen_loc_check(items, screen_img):

    z = ImageOps.crop(screen_img, (173,0,50,0))
    zpos = pytesseract.image_to_string(z, config="--psm 13 outputbase digits")
    zpos = str(zpos).replace('\n', '').replace('\x0c', '').replace('(', '').replace(']', '').replace('[', '')
    if zpos.isdigit() and int(float(zpos)) >= 100:
        xcrop = (0,0,220,0)
        ycrop = (82,0,128,0)
    else:
        xcrop = (0,0,210,0)
        ycrop = (88,0,120,0)
    x = ImageOps.crop(screen_img, xcrop)
    y = ImageOps.crop(screen_img, ycrop)
    
    x = x.resize((150, 100))
    y = y.resize((150, 100))
    
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
    
    xpos = pytesseract.image_to_string(x, config="--psm 13 outputbase digits")
    ypos = pytesseract.image_to_string(y, config="--psm 13 outputbase digits")

    xpos = str(xpos).replace('\n', '').replace('\x0c', '').replace('(', '').replace(']', '').replace('[', '')
    ypos = str(ypos).replace('\n', '').replace('\x0c', '').replace('(', '').replace(']', '').replace('[', '')

    pos = [xpos, ypos]
    
    confirms = []
    for element in items:
        min_x = int(float(element[0]))-15
        max_x = int(float(element[0]))+15
        min_y = int(float(element[1]))-15
        max_y = int(float(element[1]))+15
        if pos[0].isdigit() and pos[1].isdigit():
            if int(float(pos[0])) >= min_x and int(float(pos[0])) <= max_x and int(float(pos[1])) >= min_y and int(float(pos[1])) <= max_y:
                confirms.append(True)
            else:
                confirms.append(False)
        else:
            pass

    if any(confirms):
        print("All Match\n ---------")
        print(pos[0], pos[1])
        return True
    else:
        print("Miss\n ---------")
        print(pos[0], pos[1])
        return False
    
while "NewWorld.exe" in (p.name() for p in psutil.process_iter()):
    screen = ImageGrab.grab(bbox=(3191, 19, 3440, 39))
    remote_image = screen.convert('RGBA')
    remote_image.save('grabbed.png')
    
    if screen_loc_check(node, remote_image) is True:
        duration = 333
        freq = 880
        winsound.Beep(freq, duration)
    sleep(1)
    