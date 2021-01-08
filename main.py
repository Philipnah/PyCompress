from PIL import Image
import os
import glob

saveToPath = "C:\\Users\\phili\\Desktop\\"

filePath = input("File: ")
filePath = filePath[1:-1]

fileName = filePath.split("\\")[len(filePath.split("\\")) - 1]

image = Image.open(filePath)

size = image.size

print("Current image size of " + fileName + " is: " + str(size))

newSize = input("(Default is 300x168) New image size: ")
if newSize == "\r" or newSize == "" or newSize == " ":
     newSize = [300, 168]
else:
     "130 130"
     newSize = newSize.split(" ")
     newSize = [int(newSize[0]), int(newSize[1])]

print("New size is " + "(" + str(newSize[0]) + ", " + str(newSize[1]) + ")")

newImage = image.resize((newSize[0], newSize[1]), Image.ANTIALIAS)

newImage.save(saveToPath + "Downscaled_" + fileName, optimize=True, quality=95)