import pandas as pd

movies = pd.read_csv('movies.csv')

#tách year ra khỏi title
movies["year"] = movies["title"].apply(lambda x: x[-5:-1])
#lọc ra những year NaN
movies.year=pd.to_numeric(movies['year'],errors='coerce',downcast='integer')
#print(movies)

# Tao ra dummies
movies = movies.join(movies.genres.str.get_dummies())

# Tao bang tuong quan
a = movies.loc[:, '(no genres listed)':'Western'].corr()
print(a)
