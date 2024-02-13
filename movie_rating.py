import random

movie_list = {"The Shawshank Redemption": 5,
              "The Godfather": 5,
              "The Dark Knight": 2,
              "The Godfather, Part II": 4,
              "12 Angry Men": 3,
              "Schindler's List": 5,
              "The Lord of the Rings: The Return of the King": 5,
              "Pulp Fiction": 4,
              "The Lord of the Rings: The Fellowship of the Ring": 5,
              "The Good, the Bad, and the Ugly": 4,
              "Forrest Gump": 5,
              "The Lord of the Rings: The Two Towers": 5,
              "Fight Club": 4,
              "Inception": 3,
              "Star Wars: Episode V - The Empire Strikes Back":4,
              "The Matrix": 2,
              "Goodfellas": 3,
              "One Flew Over the Cuckoo's Nest": 3,
              "Se7en": 2,
              "It's a Wonderful Life": 3}

movie, movie_rating = random.choice(list(movie_list.items()))

print(f"Please rate the movie: {movie},")
user_rating = input("from 1-5 stars: ")

input("> ")
rating_difference = int(user_rating) - movie_rating
print(f"Your rating is: {user_rating}.")
print(f"Our rating is: {movie_rating}.")
print(f"The difference between the ratings is: {rating_difference}")