import sys
from model.ocr import ocr
from model.extract import get_date

def run(imgpath):
    text, lines = ocr(imgpath)
    #print(text,lines)
    dates = get_date(lines)
    print(dates)





if __name__=='__main__':
    imgpath = sys.argv[1]
    run(imgpath)