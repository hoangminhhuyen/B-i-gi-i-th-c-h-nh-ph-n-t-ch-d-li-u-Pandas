import pandas as pd
from itertools import chain
from collections import Counter
import matplotlib.pyplot as plt

movies = pd.read_csv('movies.csv')

#tách genres thành 1 list
movies['genre'] = movies['genres'].apply(lambda x: x.split('|'))

#tách year ra khỏi title
movies["year"] = movies["title"].apply(lambda x: x[-5:-1])
#lọc ra những year NaN
movies.year=pd.to_numeric(movies['year'],errors='coerce',downcast='integer')
#print(movies)

#danh sách các genres xếp theo thứ tự từ phổ biến nhất
frequency = pd.Series(Counter(chain.from_iterable(x.split('|') for x in movies.genres)))\
    .sort_values(ascending=False)
#print(frequency)

#3 genres phổ biến nhất
a = frequency.head(3).index.tolist()
print('3 genres pho bien nhat la:', a)

#Tạo dataframe chỉ chứa 3 genres phổ biến nhất
movies1=movies[movies['genres'].str.contains("Drama")]
movies2=movies[movies['genres'].str.contains("Comedy")]
movies3=movies[movies['genres'].str.contains("Thriller")]

#Tạo chart with 3 lines
movies1.groupby('year').size().plot(kind='line')
movies2.groupby('year').size().plot(kind='line')
movies3.groupby('year').size().plot(kind='line')

plt.show()
