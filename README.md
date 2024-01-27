## Movie Recommendation System

This repository contains a movie recommendation system created using the TMDB dataset from Kaggle. The system uses collaborative filtering to recommend movies to users based on their past movie ratings.

## Installation

To use the movie recommendation system, follow these steps:

### First run  the jupyter notebook and generate `similarity.pkl` file

1. Clone the repository to your local machine:
```
git clone https://github.com/antonysamuel/movie_recommendation_system.git
```

2. Navigate to the cloned repository:
```
cd movie_recommendation_system
```

3. Install the required packages:
```
pip install -r requirements.txt
```

## Usage

The movie recommendation system has streamlit ui. To use the system, follow these steps:

1. Run the `app.py` file:
```
streamlit run app.py
```

2. Enter your movie ratings when prompted. The system will recommend movies based on your ratings.

## Dataset

The movie recommendation system uses the TMDB dataset from Kaggle. The dataset contains information about movies, such as their titles, genres, and ratings. The dataset can be found at <https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata>.

## Credits

The movie recommendation system was created by Antony Samuel. The system was inspired by the book "Programming Collective Intelligence" by Toby Segaran.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Kaggle for providing the TMDB dataset