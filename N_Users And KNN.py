#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix

class Get_Recommendations():
    def get_n_similar_books(self, ISBN, n):
        rating_count = pd.DataFrame(ratings.groupby('ISBN')['Book-Rating'].count())
        rating_count.sort_values('Book-Rating', ascending=False)
        average_rating = pd.DataFrame(ratings.groupby('ISBN')['Book-Rating'].mean())
        average_rating['ratingCount'] = pd.DataFrame(ratings.groupby('ISBN')['Book-Rating'].count())
        average_rating.sort_values('ratingCount', ascending=False)
        counts1 = ratings['User-ID'].value_counts()
        Ratings = ratings[ratings['User-ID'].isin(counts1[counts1 >= 200].index)]
        counts = ratings['Book-Rating'].value_counts()
        Ratings = ratings[ratings['Book-Rating'].isin(counts[counts >= 100].index)]
        ratings_pivot = Ratings.pivot(index='User-ID', columns='ISBN').Book-Rating
        userID = Ratings_pivot.index
        ISBN3 = Ratings_pivot.columns
        Ratings_pivot.shape
        book_ratings = Ratings_pivot[ISBN]
        similar_to_book = Ratings_pivot.corrwith(book_ratings)
        corr_book = pd.DataFrame(similar_to_book, columns=['pearsonR'])
        corr_book.dropna(inplace=True)
        corr_summary = corr_book.join(average_rating['ratingCount'])
        return corr_summary[corr_summary['ratingCount']>=300].sort_values('pearsonR', ascending=False).head(n)
        
        
    def get_n_similar_users(self, userID, n):
        user_ratings = Ratings_pivot[userID]
        similar_to_user = Ratings_pivot.corrwith(user_ratings)
        corr_user = pd.DataFrame(similar_to_user, columns=['pearsonR'])
        corr_user.dropna(inplace=True)
        corr_summary = corr_user.join(average_rating['ratingCount'])
        return corr_summary[corr_summary['ratingCount']>=300].sort_values('pearsonR', ascending=False).head(n)
    
    
    def RecommendBooksKNN(self, ISBN, n):
    number_rating = merged_df.groupby('Book-title')['Book-Rating'].count().reset_index()
    number_rating.rename(columns= {'Book-Rating':'number_of_ratings'}, inplace=True)
    final_rating = merged_df.merge(number_rating, on='Book-title')
    final_rating.shape
    final_rating = final_rating[final_rating['number_of_ratings'] >= 50]
    final_rating.drop_duplicates(['User_ID','Book-title'], inplace=True)
    book_pivot = final_rating.pivot_table(columns='User_ID', index='Book-title', values="Book-Rating")
    book_pivot.fillna(0, inplace=True)
    book_sparse = csr_matrix(book_pivot)
    model = NearestNeighbors(algorithm='brute')
    model.fit(book_sparse)
    distances, suggestions = model.kneighbors(book_pivot[ISBN].values.reshape(1, -1))
    for i in range(len(suggestions)):
        print(book_pivot.index[suggestions[i]])


# In[ ]:




