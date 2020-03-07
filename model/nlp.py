import pandas as pd
import numpy as np
import re
import spacy
import gensim
from gensim import corpora

import operator
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

import nltk
from nltk.stem import WordNetLemmatizer
from string import punctuation
from nltk.tokenize import word_tokenize
from collections import Counter
import operator

# libraries for visualization
import pyLDAvis
import pyLDAvis.gensim
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns

data = pd.read_csv('1.txt', sep=" ", header=None)
print(data)

