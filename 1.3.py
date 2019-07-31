import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('movies.csv')

#tách year ra khỏi title
movies["year"] = movies.title.apply(lambda x: x[-5:-1])

#loại bỏ những year NaN
movies.year=pd.to_numeric(movies.year,errors='coerce',downcast='integer')
#print(movies.year)

#tách genres thành 1 list
movies['genre'] = movies.genres.apply(lambda x: x.split('|'))
#print(movies.genre)

#tạo dataframe chỉ chứa genre Drama
movies1=movies[movies.genres.str.contains("Drama")]

#vẽ line Drama qua các năm
movies1.groupby('year').size().plot(kind='line')
plt.show()