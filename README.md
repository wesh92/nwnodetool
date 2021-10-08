# nwnodetool
## A simple OCR Nearby Node Tool for NW
 -------------------------------------
 ! This has only been tested on Windows 10, any other OS or version of Windows will not see direct support from me both because I don't have access to it AND because I simply don't care to make it work with other OSes. 
 
 _FEEL FREE TO FORK AND DO YOUR OWN THING THOUGH. SEE LICENSE FILE FOR MORE LICENSE INFORMATION (APACHE LICENSE)_
 
 -------------------------------------
 Special thanks to the team over at **https://www.newworld-map.com** whose marker JSON file I used to create the lists of coordinates for this program!
 
 -------------------------------------
 
 Goals:
 - Given a list of node coordinates, let the player know they are near it.
 - That's about it.

 -------------------------------------
 
 ### Using this program
 
 DISCLAIMER: I simply don't have the time to troubleshoot **general** issues you may face. Issues related to installing Python, Packages, or anything _easily_ google-able will be closed with prejudice.
 
 This is ***NOT*** an executable so you will need to set up Python and have all the packages in the requirements.txt. 
 
 If you want to PR an executable version for release or fork for yourself that is fine but I won't be doing it for myself!
 
After you've ensured you have all the necessary packages mentioned in requirements.txt, make sure you _have the game running_ as it will look for it in the process list, and then start the program by clicking on nwocrsounds.py. 

Having **specific issues?** File an Issue in Github.

-------------------------------------

### TODO:
- All node lists for the different gatherables.
- Ability to select which group or which specific gatherable you'd like to be notified of.
- Accessibility options related to the sound produced by the program, namely the length and frequency.
- Cropping and bbox mappings for **common** resolutions such as 1080p, 2k, 4k.
- Ability to change the detection box range.

**See a task you're interested in? Make a branch and PR!**
