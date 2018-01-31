# Udacity Full Stack Web Developer Project 1: Movie Trailer Website
The movie trailer website is the first project in the Udacity Full Stack Web Developer nano-degree.

A list of IMDB ids are hard coded in the application. When run, the app will call out to the OMDB API to retrieve additional movie information, then create an HTML page to display this information and open this page in a web browser.

# Getting Started
### Dependencies
* Python 3.6.2
* requests==2.18.4

### Setup
* Create a free OMDB API key (from omdbapi.com).
* Copy `config-template.ini` to `config.ini` and fill in the property with your new API key.

### Running the App
* Execute `python app.py` to run the app.
* This will create `fresh_tomatoes.html` in the same directory and open that file using your web browser.
