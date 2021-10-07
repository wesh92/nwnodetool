from PIL import ImageGrab
import pytesseract
import psutil
from playsound import playsound
from time import sleep
import pathlib

# for 3440*1440 : (3182,19,3416,39)
localpath = str(pathlib.Path(__file__).parent.resolve())
pytesseract.pytesseract.tesseract_cmd = rf"{localpath}\Tesseract-OCR\tesseract.exe"
node = ['7831', '1673', '165']  
def screen_loc_check(items: list, screen_img):
    text = pytesseract.image_to_string(screen_img, config="--psm 7")
    text = str(text).replace('\n', '').replace('\x0c', '').replace('(', '').replace(']', '').replace('[', '')
    confirms = []
    for element in items:
        if element in text:
            confirms.append(True)
            print(True)
        else:
            confirms.append(False)

    print(text+'\n')
    print(confirms)
    if all(confirms):
        print("All Match\n")
        return True
    else:
        print("Miss\n")
        return False
    
while "NewWorld.exe" in (p.name() for p in psutil.process_iter()):
    # Grab some screen
    screenx =  ImageGrab.grab(bbox=(3182,19,3416,39))
    # Make greyscale
    w = screenx.convert('L')
    # Save so we can see what we grabbed
    w.save('grabbed.png')
    
    if screen_loc_check(node, w) is True:
        playsound(rf'{localpath}\bell.wav')
    sleep(5)
    