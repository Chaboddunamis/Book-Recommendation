


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import csv




# A python class to load datasets and output a dataframe

    class load_data:
        def Ratings(self, filename): # A function to read the ratings file into a dataframe. Takes the filename as arguments
            ratings = pd.read_csv(filepath + filename, delimiter=';',encoding= 'unicode_escape') # file is read from the filepath into a variable as a dataframe. The delimiter argument ensures that commas are recognized as separators in the csv file
            return ratings
    
        def Books(self, filename): # A function to read the books file to a dataframe
            books = pd.read_csv(filepath + filename, delimiter=';',encoding= 'unicode_escape', usecols = ['ISBN','Book-Title','Book-Author','Year-Of-Publication']) # File is read and only specified columns from the csv file are recognized and used. Thee usecols argument does this.
            return books
    
    
    def get_preferences(datasets): # A function to turn datasets and obtain a unified dataframe.
         if __name__ == '__main__':
                getPref = load_data() # Instance of the load_data class.
                ratings_df = getPref.Ratings(datasets[0]) # Variable holding the ratings dataframe
                books_df = getPref.Books(datasets[1]) # Variable holding the books dataframe
                merged_df = pd.merge(ratings_df, books_df, on='ISBN') # Merge both dataframes into one dataframe using their ISBN columns 
                user_preferences = merged_df.groupby('User-ID')[['ISBN','Book-Title','Book-Author', 'Year-Of-Publication','Book-Rating']].apply(lambda x: x.set_index('ISBN').to_dict(orient='index')).to_dict() # Group the data by setting the base index as User-ID and secondary index as ISBN
                return user_preferences
 





datasets = ['Book-Ratings.csv', 'Books.csv']



user_preferences = get_preferences(datasets)

user_preferences





