
import operator 
import sys
import re
import nltk
# from nltk.corpus import stopwords
# from bs4 import BeautifulSoup
# from xlrd import open_workbook
# from xlutils.copy import copy
import xlrd
import os
# import xlwt
# from tkinter import *
# from tkinter import ttk
# import pandas as pd 
# import subprocess, sys

def get_date(items):
	#format d/m/y & d-m-y is support
    dates=set()
    for data in items:
        f1 = re.findall(r'\d{1,2}\/\d{1,2}\/\d{4}',data)
        f2 = re.findall(r'\d{4}\/\d{1,2}\/\d{1,2}',data)
        f3 = re.findall(r'\d{2}\/\d{1,2}\/\d{1,2}',data)
        f4 = re.findall(r'\d{1,2}\/\d{1,2}\/\d{2}',data)
        
        for i in f1:
            dates.add(i)
        for i in f2:
            dates.add(i)
        for i in f3:
            dates.add(i)
        for i in f4:
            dates.add(i)
    return dates
