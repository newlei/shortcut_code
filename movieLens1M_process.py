# Import packages
import os
import pandas as pd
import pdb
import numpy as np


# Define file directories
MOVIELENS_DIR = '/home/d1/chenlei/fairness/data/ml1m' 
USER_DATA_FILE = 'users.dat'
MOVIE_DATA_FILE = 'movies.dat'
RATING_DATA_FILE = 'ratings.dat'


# Specify User's Age and Occupation Column
GENDER = {'F':0,'M':1}
AGESNUM = {1: 0, 18: 1, 25: 2, 35: 3, 45: 4, 50: 5, 56: 6}
AGES = { 1: "Under 18", 18: "18-24", 25: "25-34", 35: "35-44", 45: "45-49", 50: "50-55", 56: "56+" }
OCCUPATIONS = { 0: "other or not specified", 1: "academic/educator", 2: "artist", 3: "clerical/admin",
                4: "college/grad student", 5: "customer service", 6: "doctor/health care",
                7: "executive/managerial", 8: "farmer", 9: "homemaker", 10: "K-12 student", 11: "lawyer",
                12: "programmer", 13: "retired", 14: "sales/marketing", 15: "scientist", 16: "self-employed",
                17: "technician/engineer", 18: "tradesman/craftsman", 19: "unemployed", 20: "writer" }

# GENRES = { 0: "Action", 1: "Adventure", 2: "Animation", 3: "Children's",
#                 4: "Comedy", 5: "Crime", 6: "Documentary",
#                 7: "Drama", 8: "Fantasy", 9: "Film-Noir", 10: "Horror", 11: "Musical",
#                 12: "Mystery", 13: "Romance", 14: "Sci-Fi", 15: "Thriller", 16: "War",
#                 17: "Western"}

GENRES = { "Action":0 ,  "Adventure":1, "Animation":2, "Children's":3,
                "Comedy":4,"Crime":5, "Documentary":6,
                "Drama":7,  "Fantasy":8,  "Film-Noir":9,  "Horror":10,"Musical":11,
                "Mystery":12, "Romance":13,"Sci-Fi":14,"Thriller":15, "War":16,
                 "Western":17}

# Read the Ratings File
ratings = pd.read_csv(os.path.join(MOVIELENS_DIR, RATING_DATA_FILE), 
                    sep='::', 
                    engine='python', 
                    encoding='latin-1',
                    names=['user_id', 'movie_id', 'rating', 'timestamp'])

# Set max_userid to the maximum user_id in the ratings
max_userid = ratings['user_id'].drop_duplicates().max()
# Set max_movieid to the maximum movie_id in the ratings
max_movieid = ratings['movie_id'].drop_duplicates().max()

# Process ratings dataframe for Keras Deep Learning model
# Add user_emb_id column whose values == user_id - 1
ratings['user_emb_id'] = ratings['user_id'] - 1
# Add movie_emb_id column whose values == movie_id - 1
ratings['movie_emb_id'] = ratings['movie_id'] - 1

print(len(ratings), 'ratings loaded')

all_ratings = ratings[['user_emb_id', 'movie_emb_id','rating']].values
all_user = ratings['user_emb_id'].values
all_item = ratings['movie_emb_id'].values

# np.save(os.path.join(MOVIELENS_DIR, 'all_ratings.npy'),all_ratings)
np.save('./mldata/all_ratings.npy',all_ratings)

users = pd.read_csv(os.path.join(MOVIELENS_DIR, USER_DATA_FILE), 
                    sep='::',
                    engine='python', 
                    encoding='latin-1',
                    names=['user_id', 'gender', 'age', 'occupation', 'zipcode'])
                
users['age_desc'] = users['age'].apply(lambda x: AGES[x])
users['occ_desc'] = users['occupation'].apply(lambda x: OCCUPATIONS[x])
users['user_emb_id'] = users['user_id'] - 1
users['gender_num'] = users['gender'].apply(lambda x: GENDER[x])
users['age_num'] = users['age'].apply(lambda x: AGESNUM[x])

users_features = users[['user_emb_id', 'gender_num','age_num', 'occupation']].values
# np.save(os.path.join(MOVIELENS_DIR, 'users_features.npy'),users_features)
np.save('./mldata/users_features.npy',users_features)

item = pd.read_csv(os.path.join(MOVIELENS_DIR, MOVIE_DATA_FILE), 
                    sep='::',
                    engine='python', 
                    encoding='latin-1',
                    names=['modvie_id', 'Title', 'genres'])
            
item['item_emb_id'] = item['modvie_id'] - 1
x1= item['genres'].values
items_features = item[['item_emb_id', 'genres']].values
np.save('./mldata/items_features.npy',items_features)

# pdb.set_trace()   
# item['genres_num'] = item['genres'].apply(lambda x: GENRES[x])  
# items_features = item[['item_emb_id', 'genres_num']].values
# np.save('./mldata/items_features.npy',items_features)

pdb.set_trace()
exit()


# Save into ratings.csv
ratings.to_csv(RATINGS_CSV_FILE, 
               sep='\t', 
               header=True, 
               encoding='latin-1', 
               columns=['user_id', 'movie_id', 'rating', 'timestamp', 'user_emb_id', 'movie_emb_id'])
print('Saved to', RATINGS_CSV_FILE)