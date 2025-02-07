# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
] 


#1

def single_movie_5_5(movie):
    return True if movie['imdb'] > 5.5 else False 

movie = {
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
}
print(single_movie_5_5(movie))
print()


#2

def sublist_movies_5_5(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

movies_above_5_5 = sublist_movies_5_5(movies)
for toma in movies_above_5_5:
    print(toma["name"], toma["imdb"], toma["category"])
print()


#3

def sublist_movies_category(movies, mycategory):
    return [movie for movie in movies if movie['category'] == mycategory]

new_categorylist = sublist_movies_category(movies, "Thriller")
for category in new_categorylist:
    print(category["name"], category["imdb"], category["category"])
print()


#4

def avg_imdb(movies):
    if not movies:
        return 0
    
    total_score = 0
    for movie in movies:
        total_score += movie['imdb']

    return total_score/len(movies)

avg = avg_imdb(movies)
print(f"avg = {avg:.2f}")
print()


#5

def avg_category(movies, mycategory):
    new_list = list(([movie['imdb'] for movie in movies if movie['category'] == mycategory]))
    total=0
    for x in new_list:
        total+=x
    
    return total/len(new_list)

avg_ctg = avg_category(movies, "Thriller")
print(f"avg of category = {avg_ctg:.2f}")

