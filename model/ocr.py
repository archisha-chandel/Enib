import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import sys
import matplotlib.pyplot as plt
from PIL import Image as im
from scipy.ndimage import interpolation as inter

def ocr(imgpath):
    '''
    input : path to the img file
    output: text
    '''
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread(imgpath,0)
    edge = cv2.Canny(img, 50, 200)
    d = pytesseract.image_to_data(edge, output_type=Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])    
        edge = cv2.rectangle(edge, (x, y), (x + w, y + h), (130, 20, 243), 2)
    extracted_text = pytesseract.image_to_string(img, lang = 'eng')
    text = extracted_text.splitlines()
    return extracted_text, text


