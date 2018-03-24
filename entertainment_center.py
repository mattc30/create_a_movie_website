import media
import fresh_tomatoes

"""
use constructor function to create 6 instances

input: str
    arg1: name of the movie
    arg2: name of director
    arg3: release date
    arg4: poster url
    arg5: trailer youtube url
"""

la_la_land = media.Movie ("LA LA LAND",
                          "Damien ChazelleDamien Chazelle",
                          "December 16, 2016",
                          "https://openaircinemas.com.au/app/uploads/2017/11/lalaland-4.jpg",
                          "https://www.youtube.com/watch?v=0pdqf4P9MB8")

hunger_games = media.Movie ("THE HUNGER GAMES",
                            "Gary Ross",
                            "March 23, 2012",
                            "http://i.ebayimg.com/00/s/NTAwWDMzNw==/z/~IkAAOxy7nNTVkmT/$_3.JPG?set_id=2",
                            "https://www.youtube.com/watch?v=mfmrPu43DF8")

the_theory_of_everything = media.Movie("THE THEORY OF EVERYTHING",
                                       "James Marsh",
                                       "November 7, 2014",
                                       "http://photo.elcinema.com.s3.amazonaws.com/uploads/_315x420_bff3eb91446795e00225bb2c55c54d205c5cc033b9333e6340fceda198eefdc3.jpg",
                                       "https://www.youtube.com/watch?v=Salz7uGp72c")                       

midnight_in_paris = media.Movie("MIDNIGHT IN PARIS",
                                "Woody Allen",
                                "May 20, 2011",
                                "http://is5.mzstatic.com/image/thumb/Video/v4/80/5c/8f/805c8f2a-5d93-0621-2f3d-2f23ba60f775/source/1200x630bb.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

avatar = media.Movie("AVATAR",
                    "James Cameron",
                    "December 18, 2009",
                    "data:image/jpeg;base64,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",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_shape_of_water = media.Movie ("THE SHAPE OF WATER",
                      "Guillermo del Toro",
                      "December 1, 2017",
                      "https://images-na.ssl-images-amazon.com/images/I/61AOfZOzLCL._SY606_.jpg",
                      "https://www.youtube.com/watch?v=XFYWazblaUA")

# make a list for six movies
movies = [la_la_land, hunger_games, the_theory_of_everything, midnight_in_paris, avatar, the_shape_of_water]

# call movie trailer, take movies as argument
fresh_tomatoes.open_movies_page(movies)
