from PIL import ImageGrab
import pytesseract
import pyautogui
import numpy
import time
import mss

pyautogui.FAILSAFE = False
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

mon1 = {'top': 90, 'left': 1530, 'width': 85, 'height': 25}
# mon2 = {'top': 592, 'left': 862, 'width': 200, 'height': 100}
# mon3 = {'top': 590, 'left': 860, 'width': 200, 'height': 100}
# mon4 = {'top': 587, 'left': 857, 'width': 200, 'height': 100}
# mon5 = {'top': 585, 'left': 855, 'width': 200, 'height': 100}
# mon6 = {'top': 582, 'left': 852, 'width': 200, 'height': 100}

with mss.mss() as sct:
   time.sleep(2)
   im1 = numpy.asarray(sct.grab(mon1))
   text1 = pytesseract.image_to_string(im1)
   
   screenshot = ImageGrab.grab(bbox=(1530, 90, 1620, 115))
   text = pytesseract.image_to_string(screenshot)

   print(text)
    
#    im2 = numpy.asarray(sct.grab(mon2))
#    text2 = pytesseract.image_to_string(im2)

#    im3 = numpy.asarray(sct.grab(mon3))
#    text3 = pytesseract.image_to_string(im3)
    
#    im4 = numpy.asarray(sct.grab(mon4))
#    text4 = pytesseract.image_to_string(im4)
    
#    im5 = numpy.asarray(sct.grab(mon5))
#    text5 = pytesseract.image_to_string(im5)

#    im6 = numpy.asarray(sct.grab(mon6))
#    text6 = pytesseract.image_to_string(im6)
    
#    #im7 = numpy.asarray(sct.grab(mon7))
#    #text7 = pytesseract.image_to_string(im7)
    
#    #im8 = numpy.asarray(sct.grab(mon8))
#    #text8 = pytesseract.image_to_string(im8)
#    print(text1)
