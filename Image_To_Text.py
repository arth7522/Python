#import libraries
import cv2
import pytesseract
from PIL import Image
import sys
import os
from pdf2image import convert_from_path as getImgsFromPDF
pytesseract.pytesseract.tesseract_cmd='C:\\Users\\SHIVAM\\Tesseract-OCR\\tesseract.exe'

img_path=input('Please enter the complete path of the image:\n')  #input path of image
img=cv2.imread(img_path)  #read image
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)   #Converting BGR to RGB because pytesseract accepts only RGB but in opencv it's BGR
print(pytesseract.image_to_string(img))
#print(pytesseract.image_to_boxes(img))
cv2.imshow('Text',img)  #display image
cv2.waitKey(0)
