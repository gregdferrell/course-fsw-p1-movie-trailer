"""
app.py is the entry point to the movie trailer website program.
"""

import fresh_tomatoes
from entertainment_center import movies

if __name__ == '__main__':
    # Open the movies page with the movies from our entertainment center
    fresh_tomatoes.open_movies_page(movies=movies)
