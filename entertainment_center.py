"""
Exposes a list of Movies.
"""

from media import Movie

# Create Movie instances from hard coded data
__m1 = Movie(title='National Lampoon''s Christmas Vacation',
             poster_image_url='http://www.movieposter.com/posters/archive/main/77/MPW-38615',
             trailer_youtube_url='https://www.youtube.com/watch?v=tLVd4ipC5Lc')
__m2 = Movie(title='Monty Python and the Holy Grail',
             poster_image_url='http://img.moviepostershop.com/monty-python-and-the-holy-grail-movie-poster-1975-1010465239.jpg',
             trailer_youtube_url='https://www.youtube.com/watch?v=LG1PlkURjxE')
__m3 = Movie(title='Young Frankenstein',
             poster_image_url='http://m.b5z.net/i/u/6127364/i/young_frankestein_ezr2.jpg',
             trailer_youtube_url='https://www.youtube.com/watch?v=mOPTriLG5cU')

# Add movies to list
movies = [__m1, __m2, __m3]
