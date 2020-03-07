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
        if 'W.E.F' in data:
            continue
        f1 = re.findall(r'\d{1,2}\d[\-|\/|\.]\d{1,2}\d[\-|\/|\.]\d{4}',data)
        f2 = re.findall(r'\d{4}\d[\-|\/|\.]\d{1,2}\d[\-|\/|\.]\d{1,2}',data)
        f3 = re.findall(r'\d{2}\d[\-|\/|\.]\d{1,2}\d[\-|\/|\.]\d{1,2}',data)
        f4 = re.findall(r'\d{1,2}\d[\-|\/|\.]\d{1,2}\d[\-|\/|\.]\d{2}',data)
        f5 = re.findall(r'(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2},\s+\d{4}',data)
        f6 = re.findall(r'\d{1,2}[\,|\/|\-](Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)[\,|\/|\-]\d{4}',data)
        f7 = re.findall(r'\d{1,2}[\,|\/|\-](Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)[\,|\/|\-]\d{2}',data)
         
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
    dates = list(dates)
    return_me = dates[0] if dates else None
    return {
        'date' : return_me
    }

def get_store_name(data):
    store_name = set()
    existing_stores = os.listdir(r'Training Data Set')
    # print(data)
    # print(existing_stores)
    # print([x for x in data if re.search('PHOENIX MALL', x)])
    # sequence = 'PHOENIX MALL'
    # rgx = re.compile('.*'.join(re.escape(x) for x in sequence))

def get_total_amount(data):
    total_amount = set()
    for x in data:
        # print(x)
        if 'total' in x.lower().strip().strip('\n').split():
            total_amount.add(x)
        if 'net' in x.lower().strip().strip('\n').split():
            if 'total' in x.lower().strip().strip('\n').split():
                total_amount.add(x)
            if 'amount' in x.lower().strip().strip('\n').split():
                total_amount.add(x)
    for x in total_amount:
        if 'sub' in x.lower().strip().strip('\n').split():
            total_amount.remove(x)
    tlt_amt = ' '.join(list(total_amount))
    # amt_set = set()
    # linesplit=list(total_amount).split("TOTAL")[-1]
    p = re.compile(r'\d+[\.|\,|\s]?\d+')
    elem = p.findall(tlt_amt)
    return_me = max(elem) if elem else None
    return {
        'total amount' : return_me
    }

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