import operator 
import sys
import re
import nltk
# from nltk.corpus import stopwords
import os
# import pandas as pd 


def get_date(items):
	#format d/m/y & d-m-y is support
    dates=set()
    # print(items)
    for data in items:
        f1 = re.findall(r'\d{1,2}\d[- /.]\d{1,2}\d[- /.]\d{4}',data)
        f2 = re.findall(r'\d{4}\d[- /.]\d{1,2}\d[- /.]\d{1,2}',data)
        f3 = re.findall(r'\d{2}\d[- /.]\d{1,2}\d[- /.]\d{1,2}',data)
        f4 = re.findall(r'\d{1,2}\d[- /.]\d{1,2}\d[- /.]\d{2}',data)
        f5 = re.findall(r'(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2},\s+\d{4}',data)
        f6 = re.findall(r'\d{1,2}[,/-](Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)[,/-]\d{4}',data)
        f7 = re.findall(r'\d{1,2}[,/-](Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)[,/-]\d{2}',data)
         
        for i in f1:
            dates.add(i)
        for i in f2:
            dates.add(i)
        for i in f3:
            dates.add(i)
        for i in f4:
            dates.add(i)
        for i in f5:
            dates.add(i)
        for i in f6:
            dates.add(i)
        for i in f7:
            dates.add(i)
        
    return dates

def get_store_name(data):
    store_name = set()
    existing_stores = os.listdir(r'Training Data Set')
    print(data)
    print(existing_stores)
    print([x for x in data if re.search('PHOENIX MALL', x)])
    # sequence = 'PHOENIX MALL'
    # rgx = re.compile('.*'.join(re.escape(x) for x in sequence))

def get_invoice_no(data):
    print(data)
    invoice_no = set()
    for i in data:
        if 'invoice' in i.lower().strip().split():
            print(i)
        if 'bill' in i.lower().strip().split():
            print(i)
            for words in i.lower().strip().split():
                try:
                    x = int(words) + 0
                    invoice_no.add(x)
                except:
                    continue
    return invoice_no