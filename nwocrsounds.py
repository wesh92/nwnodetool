"""
New World OCR Node Detector
Created: 2021-10-07
Dev: Wes H.

Uses OCR to get coordinates from top right of the NW game window
and imposes that against a list of possible nodes.
When you're close to one it will play a bell noise!
"""
import winsound
from PIL import ImageGrab, ImageOps
import pytesseract
import psutil
from time import sleep
import pathlib
import iron_markers as imark

# for 3440*1440 : (3182,19,3416,39)
localpath = str(pathlib.Path(__file__).parent.resolve())
pytesseract.pytesseract.tesseract_cmd = rf"{localpath}\Tesseract-OCR\tesseract.exe"
# node = [['7831', '1673'], ['9341', '2725']] 
node = imark.iron
def screen_loc_check(items, screen_img):

    x = ImageOps.crop(screen_img, (0,0,210,0))
    y = ImageOps.crop(screen_img, (86,0,120,0))
    x = x.resize((150, 100))
    y = y.resize((150, 100))
    xpos = pytesseract.image_to_string(x, config="--psm 13 digits")
    ypos = pytesseract.image_to_string(y, config="--psm 13 digits")

    xpos = str(xpos).replace('\n', '').replace('\x0c', '').replace('(', '').replace(']', '').replace('[', '')
    ypos = str(ypos).replace('\n', '').replace('\x0c', '').replace('(', '').replace(']', '').replace('[', '')

    pos = [xpos, ypos]
    
    confirms = []
    for element in items:
        min_x = str(int(element[0])-5)
        max_x = str(int(element[0])+5)
        min_y = str(int(element[1])-5)
        max_y = str(int(element[1])+5)
        if pos[0] >= min_x and pos[0] <= max_x and pos[1] >= min_y and pos[1] <= max_y:
            confirms.append(True)
        else:
            confirms.append(False)

    if any(confirms):
        print("All Match\n ---------")
        return True
    else:
        print("Miss\n ---------")
        return False
    
while "NewWorld.exe" in (p.name() for p in psutil.process_iter()):
    screen = ImageGrab.grab(bbox=(3191, 19, 3440, 39))
    remote_image = screen.convert('L')
    remote_image.save('grabbed.png')
    
    if screen_loc_check(node, remote_image) is True:
        duration = 333
        freq = 880
        winsound.Beep(freq, duration)
    sleep(3)
    