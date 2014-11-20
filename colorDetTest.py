
from myro import *
#from Tkinter import *
#from PIL import ImageTk
#import ImageTk
#import Image
#initialize("/dev/tty.IPRE6-196107-DevB")

def findIfRGB():#returns r,g,b,or 0
    wait(0.5)
    sMinRange = 0
    sMaxRange = 130
    mMinRange = 75
    mMaxRange = 255
    print("starting again")
    redResult = filterImage(mMinRange,mMaxRange,sMinRange,sMaxRange,sMinRange,sMaxRange)# was (100,200,-1,-1,-1,-1) #Filter image100,255,0,75,0,75
    greenResult = filterImage(sMinRange,sMaxRange,mMinRange,mMaxRange,sMinRange,sMaxRange-25)# was (-1,-1,100,200,-1,-1)
    blueResult = filterImage(sMinRange,sMaxRange,sMinRange,sMaxRange-25,mMinRange,mMaxRange)

    print(redResult['pxlCount'],greenResult['pxlCount'],blueResult['pxlCount'])

    array = [redResult['pxlCount'],greenResult['pxlCount'],blueResult['pxlCount']]

    if redResult['pxlCount'] == max(array): 
        return "red"
    elif greenResult['pxlCount'] == max(array): 
        return "green"
    elif blueResult['pxlCount'] == max(array): 
        return "blue"

    #else:
        
        #return findIfRGB()
    
def filterImage(minR, maxR, minG, maxG, minB, maxB): # Enter -1 into min value to remove color from filter
    pic = takePicture("color")
    x = 0
    y = 1
    avgX = 0
    avgY = 0
    pxlCount = 0
    for pixel in getPixels(pic): #For every pixel in image
        x = x + 1
        if x == 257:
            x = 1
            y = y + 1
        r, g, b = getRGB(pixel)
        rCheck = True
        gCheck = True
        bCheck = True
        if minR > 0: #Ignore red filter if minR<0
            if not(minR<=r and maxR>=r): #Is red in range
                rCheck = False
        if minG > 0: #Ignore green filter if minR<0
            if not(minG<=g and maxG>=g): #Is green in range
                gCheck = False
        if minB > 0: #Ignore blue filter if minR<0
            if not(minB<=b and maxB>=b): #Is blue in range
                bCheck = False
        if rCheck and bCheck and gCheck: #Check if pixel matches color range
            setRGB(pixel, (255,255,255)) #Set pixel white
            pxlCount += 1
            avgX += x
            avgY += y
        else:
            setRGB(pixel, (0,0,0))       #Set pixel black
    if pxlCount != 0:
        avgX = avgX / pxlCount
        avgY = avgY / pxlCount
    elif pxlCount == 0:
        avgX = 0
        avgY = 0
    #Return dictionary(black-white blob image, pixel count, average x value and y value of pixel locations
    return {'shape':pic, 'pxlCount':pxlCount, 'avgX':avgX, 'avgY':avgY}
"""
def main():
    for i in range(0,18):
        
        wait(1)
        result = findIfRGB()
        if result == "R":
            print("red")
        elif result == "G":
            print("green")
        elif result == "B":
            print("blue")

        #show(result['shape']) #Display Image 


main()
"""               
