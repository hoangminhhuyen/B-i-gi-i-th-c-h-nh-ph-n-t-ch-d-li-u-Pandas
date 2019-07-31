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
print('No.1:',a[0])
print('No.2:',a[1])
print('No.3:',a[2])

#Tạo dataframe chỉ chứa 3 genres phổ biến nhất
movies1=movies[movies['genres'].str.contains(a[0])]
movies2=movies[movies['genres'].str.contains(a[1])]
movies3=movies[movies['genres'].str.contains(a[2])]

#Tạo chart with 3 lines
movies1.groupby('year').size().plot(kind='line', label = a[0])
movies2.groupby('year').size().plot(kind='line', label = a[1])
movies3.groupby('year').size().plot(kind='line', label = a[2])

plt.ylabel('Số phim')
plt.legend()
plt.show()
