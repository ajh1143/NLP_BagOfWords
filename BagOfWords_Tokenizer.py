#Import Packages
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

#Extracts contents of a file, returns a bag of words(count of each word)
def count_words(document):
    #Load target File as 'document' to 'raw_file' 
    raw_file = pd.read_csv(document)
    #Tokenize all words in 'raw_file' using word_tokenize()
    token_list = word_tokenize(raw_file)
    #Convert each item in token list to lower_case list
    lowercase_tokens = [each.lower() for each in token_list]
    #Create list of each word and associated count
    bag_Of_Words = Counter(lowercase_tokens)
    return bag_Of_Words

#Given a particular bag of words, desired counts, creates a dataframe, resets index, plots counts
def plot_counts(bag_of_words, amount):
    df = pd.DataFrame(bag_of_words.most_common(amount))
    df.set_index(0,drop=True,inplace=True)
    df.plot(kind="bar")
    plt.show()
