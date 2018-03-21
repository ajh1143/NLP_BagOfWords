#Import Packages
import pandas as pd
from collections import Counter

def count_words(document):
    #Load target File as 'document' to 'raw_file' 
    raw_file = pd.read_csv(document)
    #Tokenize all words in 'raw_file' using word_tokenize()
    token_list = word_tokenize(raw_file)
    #Convert each item in token list to lower_case list
    lowercase_tokens = [each.lower() for each in token_list]
    #Create list of each word and associated count
    bag_Of_Words = Counter(lowercase_tokens)
    print(bag_Of_Words)
