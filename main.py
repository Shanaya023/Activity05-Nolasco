import cv2 as cv
import numpy as np
from os import system
from time import sleep

system('cls')

filepath = "Eimi.jpg"

img = cv.imread(filepath)

if len(img.shape) < 3:
    print("Image is grayscale")
    sleep(3)
    exit()

# coordinate a pixel then print its value
system('cls')
shp = img.shape
print("Access a pixel")
xs = int(input("Enter 'X' coordinate value (max value "+str(shp[0])+" ) : "))
ys = int(input("Enter 'Y' coordinate value (max value "+str(shp[1])+" ) : "))
chn = int(input("""Select channel:
0 - blue
1 - green
2 - red
>> """))

acs = img.item(xs, ys, chn)

system('cls')
shp = img.shape
print("Modify a pixel")
xs = int(input("Enter 'x' coordinate value (max value "+str(shp[0])+" ) : "))
ys = int(input("Enter 'y' coordinate value (max value "+str(shp[1])+" ) : "))
bl = int(input("Enter blue channel value: "))
grn = int(input("Enter green channel value: "))
red = int(input("Enter red channel value: "))

system('cls')

print("Outputs:")

print("\nAccessed Pixel Value:", acs)

print("Pixel value before modify:", img[xs, ys])  

img.itemset((xs, ys, 0), bl)
img.itemset((xs, ys, 1), grn)
img.itemset((xs, ys, 2), red)

print("Pixel value after modified:", img[xs, ys])  

wd = 640
ht = 427

if wd > shp[1] or ht > shp[0]:
    print("Set Image Dimension: Out of bounderies")
else:
    print("Set Image Dimension: Within the bounderies")

pix = 1683001

if pix > img.size: print("Set Pixel: Higher than the pixel count")
elif pix < img.size: print("Set Pixel: Lower than the pixel count")
else: print("Set pixel: Equal to the pixel count")

print("Image Data Type:", img.dtype)
