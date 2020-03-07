import sys
from model.ocr import ocr
from model.extract import get_date, get_total_amount, get_time

def run(imgpath):
    text, lines = ocr(imgpath)
    dates = get_date(lines)
    print(dates)
    total_amount = get_total_amount(lines)
    print(total_amount)
    time = get_time(lines)
    print(time)




if __name__=='__main__':
    imgpath = sys.argv[1]
    run(imgpath)