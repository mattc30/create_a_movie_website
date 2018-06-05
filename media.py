import webbrowser


class Movie():
    def __init__(self, movie_title, movie_director, release_date,
                 movie_poster, movie_trailer):
        """this class provide a way to store movie information
           initialize instance of class movie

        attributes: str
           movie_title: name of the movie
           director: movie director
           release_date: movie release date
           poster_image_url: movie poster
           railer_youtube_id: movie trailer from youtube
        """
        self.title = movie_title
        self.director = movie_director
        self.release_date = release_date
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        """play movie trailer in web browser"""
        webbrowser.open(self.trailer_youtube_url)
