def main():
    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Nishant Kumar Khatri",
        "student_ID": 10321358,
        "pizza_toppings": ["ONION", "CHICKEN", "HAM"],
        "movies": [
            {"title": "avatar", "genre": "epic science fiction"},
            {"title": "kgf", "genre": "action"}
        ],
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {"title": "kabaddi", "genre": "romance"}
    about_me["movies"].append(new_movie)
    add_pizza_toppings(about_me, ["BACON", "CHEESE"])
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me["movies"])


# TODO: Step 4 - Function that prints student name and ID
def print_student_name_and_id(about_me):
    full_name = about_me['full_name']
    first_name = (full_name.split())[0]
    student_id = about_me["student_ID"]
    print(f"My name is {full_name}, but you can call me Mr.{first_name}.")
    print(f"My student ID is {student_id}")
    return

# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me["pizza_toppings"].extend(toppings)
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    pizza_toppings= about_me["pizza_toppings"]
    print(f"My favourite pizza toppings are :{pizza_toppings}\n")
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie["genre"] for movie in about_me["movies"]]
    print(f"I like to watch {', '.join(genres)}\n movies.\n")
    return

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie.get('title') for movie in movie_list]
    print(f"Some of my favorite movies are {', '.join(titles)}!\n")
    return

if __name__ == '__main__':
    main()