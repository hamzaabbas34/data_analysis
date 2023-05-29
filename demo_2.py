import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import requests
final = pd.DataFrame()
for j in range(1,10):
    response = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key=36c90eb8c7864d9adf816100134bbc24&language=en.US&page={j}').json()
    popularity = []
    vote_average = []
    vote_count= [ ]
    original_language = []
    title = []
    overview = []
    release_date = []
    
    for i in response['results']:
        popularity.append(i['popularity'])
        vote_count.append(i['vote_count'])
        original_language.append(i['original_language'])
        title.append(i['title'])
        overview.append(i['overview'])
        try:
            release_date.append(i['release_date'])
        except:
            release_date.append(np.nan)
        vote_average.append(i['vote_average'])

    d = {'title':title, 'overview':overview ,'original_language':original_language, 'ralease_date':release_date , 'popularity':popularity ,'vote_count' :vote_count , 'vote_average' : vote_average }
    
    df = pd.DataFrame(d)
    # Convert dictionary 'd' to DataFrame
    d_df = pd.DataFrame.from_dict(d)
    # Use pandas.concat to concatenate the DataFrames
    final = pd.concat([final, d_df], ignore_index=True)

print(final)