import streamlit as st
import pickle
import pandas as pd
import requests






#Function to fetch poster
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=d22502286f7ce075df26122b0ceec98b')
    data = response.json()
    
    poster = data['poster_path']
    
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


#Function to get recommendations
def recommend(movie,df,similarity):
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key= lambda x: x[1])[1:6]
    movies_idx = [m[0] for m in movies_list]
    recommended_movies = df.iloc[movies_idx].title.values 


    #fetch posters of recommended movies
    recommended_movies_poster = [fetch_poster(m) for m in df.movie_id.loc[movies_idx].values]
    return recommended_movies, recommended_movies_poster
#Loding movies pkl file -> dict and -> df
movies_dict = pickle.load(open('./movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
st.title("Movie Recommendation System")

#Loading similarity file
similarity = pickle.load(open('./similarity.pkl','rb'))



selected_movie_name = st.selectbox(label='Movies',options=movies['title'].values)

if st.button('Recommend'):
    st.write(selected_movie_name)
    recommendations, posters = recommend(selected_movie_name, movies, similarity)
    cols = st.columns(len(posters))
    for idx,col in enumerate(cols):
        with col:
            st.text(recommendations[idx])
            st.image(posters[idx])
  


