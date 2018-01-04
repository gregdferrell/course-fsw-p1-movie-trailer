import configparser
import json
import os

import requests

from media import Movie

# Load OMDB API Key from external config
config = configparser.ConfigParser()
config.read(os.path.join(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini')))
omdb_api_key = config['DEFAULT']['omdb.api.key']


class EntertainmentCenter:
    """ EntertainmentCenter contains properties representing media in an
    entertainment center. Movie data is accessed via omdb api.

    Attributes:
        movies (list): The list of movies.
    """

    def __init__(self):
        # Create Movie instances from hard coded data
        m1 = Movie(imdb_id='tt0097958',
                   trailer_youtube_url='https://www.youtube.com/watch?v=tLVd4ipC5Lc')  # noqa
        m2 = Movie(imdb_id='tt0071853',
                   trailer_youtube_url='https://www.youtube.com/watch?v=LG1PlkURjxE')  # noqa
        m3 = Movie(imdb_id='tt0072431',
                   trailer_youtube_url='https://www.youtube.com/watch?v=mOPTriLG5cU')  # noqa
        self.movies = [m1, m2, m3]

        # Load movie data from external source: omdb api
        self.__load_movie_data_from_omdb()

    def __load_movie_data_from_omdb(self):
        """
        Populates data in the movies attribute by calling OMDB API and
        passing in the imdb_id if present.
        :return: nothing; instead populates the movies attribute
        """
        get_movie_url = 'http://www.omdbapi.com'

        for movie in self.movies:
            if movie.imdb_id:
                params = {'apikey': omdb_api_key, 'i': movie.imdb_id}
                response = requests.get(get_movie_url, params=params)
                data = json.loads(response.text)
                if response.status_code == 200 and 'Error' not in data:
                    movie.title = data.get('Title', '')
                    movie.year = data.get('Year', '')
                    movie.rated = data.get('Rated', '')
                    movie.poster_image_url = data.get('Poster', '')
                else:
                    print(
                        "Fetching movie info for imdb id ({}) resulted in an"
                        " error {}. {}".format(
                            movie.imdb_id, response.status_code,
                            data.get('Error', 'Unspecified error')))
