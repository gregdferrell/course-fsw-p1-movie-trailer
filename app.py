from entertainment_center import EntertainmentCenter
from fresh_tomatoes import open_movies_page

if __name__ == '__main__':
    # Initialize an entertainment center
    entertainment_center = EntertainmentCenter()

    # Get the list of movies from the entertainment center instance and filter
    # out any that have properties with empty values
    movies = filter(lambda movie: movie.all_properties_non_empty(),
                    entertainment_center.movies)

    # Open the movies web page with the filtered list of movies from our
    # entertainment center
    open_movies_page(movies=movies)
