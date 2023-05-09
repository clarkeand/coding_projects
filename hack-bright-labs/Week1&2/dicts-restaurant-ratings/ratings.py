"""Restaurant rating lister."""

the_file = open("scores.txt")
restaurant_ratings_dictionary = {}

for row in the_file: 
    line = row.rstrip()
    restaurant_rating_list = line.split(':')
    name = restaurant_rating_list[0]
    rating = restaurant_rating_list[1]
    restaurant_ratings_dictionary[name] = rating

user_restaurant = input("Please enter a restaruant: ")
user_score = input("Please enter a score for the restaruant: ")
restaurant_ratings_dictionary[user_restaurant] = user_score

keys_of_restaurants = list(restaurant_ratings_dictionary.keys())
keys_of_restaurants.sort()
sorted_restaurants = {}
for key in keys_of_restaurants: 
     sorted_restaurants[key] = restaurant_ratings_dictionary[key]

for restaurants, rating in sorted_restaurants.items():
     print(f'{restaurants} is rated at {rating}.')