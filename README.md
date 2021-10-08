# nwnodetool
## A simple OCR Nearby Node Tool for New World
 -------------------------------------
 ! This has only been tested on Windows 10, any other OS or version of Windows will not see direct support from me both because I don't have access to it AND because I simply don't care to make it work with other OSes. 
 
 _FEEL FREE TO FORK AND DO YOUR OWN THING THOUGH. SEE LICENSE FILE FOR MORE LICENSE INFORMATION (APACHE LICENSE)_
 
 -------------------------------------
 Special thanks to the team over at **https://www.newworld-map.com** whose marker JSON file I used to create the lists of coordinates for this program!
 
 This script uses OCR to take a screenshot of the top right of your game window (where the FPS Counter/Ping Counter/Coordinates are), crops them down to X and Y coordinates and compares those coordinates against a list of known coordinates for nodes.
 
 When it does find a match, it will make a beep to call your attention to it. It makes a screen grab every 3 seconds.
 
 As with _ALL_ OCR-based scripts, the detection _WILL BE_ hit or miss especially if you have a bright, mixed color, or similarly light-yellow colored backgroud behind the coordinates. Lowering your brightness or gamma may help you! YMMV.
 
 ***I want to be very clear that this script in no way interacts directly with the game, your RAM, hard drive (other than temp saving the screen shots for processing), network interface, or any other software or hardware. It simply takes a screenshot and compares it against a list of coordinates. Anyone could get these coordinates, it's the same as having the new world interactive map above up on another screen.***
 
 ###### The maintainer, this project and all contained files are in no way associated with the game New World, Amazon Game Studios(AGS), Amazon Games, Amazon, or any of it's affiliates. New World is a registered trademark of Amazon Games.
 
 ##### The maintainer and this project are in no way associated with Google or any Alphabet owned company. PyTesseract, Tesseract are all used under the Apache 2.0 License and maintainer affirms no changes have been made to the distribution. This project is also distributed with an Apache 2.0 License for convenience in terms.
 -------------------------------------
 
 Goals:
 - Given a list of node coordinates, let the player know they are near it.
 - That's about it.

 -------------------------------------
 
 ### Using this program
 
 DISCLAIMER: I simply don't have the time to troubleshoot **general** issues you may face. Issues related to installing Python, Packages, or anything _easily_ google-able will be closed with prejudice.
 
 This is ***NOT*** an executable so you will need to set up Python and have all the packages in the requirements.txt. 
 
 If you want to PR an executable version for release or fork for yourself that is fine but I won't be doing it for myself!
 
After you've ensured you have all the necessary packages mentioned in requirements.txt, make sure you _have the game running_ as it will look for it in the process list, you have your coordinates at the top right (Turn on the FPS Counter in settings), and then start the program by clicking on nwocrsounds.py. 

Having **specific issues?** File an Issue in Github.

-------------------------------------

### TODO:
- All node lists for the different gatherables.
- Ability to select which group or which specific gatherable you'd like to be notified of.
- Accessibility options related to the sound produced by the program, namely the length and frequency.
- Cropping and bbox mappings for **common** resolutions such as 1080p, 2k, 4k.
- Ability to change the detection box range.

**See a task you're interested in? Make a branch and PR!**
