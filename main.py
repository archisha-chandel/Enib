import sys
from model.ocr import ocr
from model.extract import get_date, get_total_amount

def run(imgpath):
    text, lines = ocr(imgpath)
    dates = get_date(lines)
    print(dates)
    total_amount = get_total_amount(lines)
    print(total_amount)





if __name__=='__main__':
    imgpath = sys.argv[1]
    run(imgpath)