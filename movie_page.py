import media
import fresh_tomatoes

# create array of movies
movie_array = [
    ["Austin Powers",
        "The international man of mystery fights the ultimate Dr. Evil",
        "http://static.rogerebert.com/uploads/movie/movie_poster/austin-powers-international-man-of-mystery-1997/large_mLVymsqdkwNNKjw2ZXn8fkor3om.jpg",
        "http://www.youtube.com/watch?v=_tQMdNoc8T8"],
    ["Convoy",
         "Rubby Ducky gets mad and fights back.",
         "http://www.impawards.com/1978/posters/convoy_ver2.jpg",
         "https://www.youtube.com/watch?v=sA0OP_x_zLc&feature=youtu.be"],
    ["Freddy Got Fingered",
        "Gordy, and animator, leaves home to fulfill his dreams.",
        "http://images.moviepostershop.com//freddy-got-fingered-movie-poster-1020476187.jpg",
        "http://www.youtube.com/watch?v=OwoVgMEXusM"],
    ["Gleaming the Cube",
         "Brian hunts for the killer of his adopted brother",
         "http://www.movieposter.com/posters/archive/main/27/MPW-13518",
         "http://www.youtube.com/watch?v=yviIgIDxlwc"],
    ["Quest for the Hold Grail",
        "King Arthur searches for the Holy Grail.",
        "http://www.movie-list.com/img/posters/big/zoom/montypythonandtheholygrail.jpg",
        "https://www.youtube.com/watch?v=LG1PlkURjxE"],
    ["War Party",
         "Battle of Milk River re-enactment goes wrong.",
         "http://images.moviepostershop.com/war-party-movie-poster-1989-1020210795.jpg",
         "http://www.youtube.com/watch?v=sgXlr5_KRBI"]
    ]

# initialize array to store movie objects
movie_list = []

# iterate over movie list array and generate a set of Movie objects
for movie_detail in movie_array:
    movie_list.append(media.Movie(movie_detail[0],movie_detail[1],movie_detail[2],movie_detail[3]))

# call prewritten method to render list of Movie objects
fresh_tomatoes.open_movies_page(movie_list)
