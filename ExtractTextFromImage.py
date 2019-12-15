from PIL import Image
import pytesseract
import cv2
import re
import os
import webbrowser
imgloc= "C:\\Users\\Khushboo prasad\\Desktop\\img.png "    
img=cv2.imread(imgloc)
print(img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
file="{}.png".format(os.getpid())
cv2.imwrite(file,gray)
text=pytesseract.image_to_string(Image.open(file))
os.remove(file)
print(text)
