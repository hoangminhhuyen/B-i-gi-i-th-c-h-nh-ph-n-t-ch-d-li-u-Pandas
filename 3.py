import pandas as pd
from itertools import chain
from collections import Counter

movies = pd.read_csv("movies.csv")
b = pd.read_csv("stopwords.txt", header=None)

#tách year ra khỏi title
movies.title = movies.title.str[:-7]
#lowercase title
movies['title'] = movies['title'].str.lower()
#xoá các khoảng trống
movies.title = movies.title.str.strip() 
#print(movies)

#list of words in title by frequency
frequency = pd.Series(Counter(chain.from_iterable(x.split(' ') for x in movies.title)))\
    .sort_values(ascending=False)
print(frequency)

#danh sach stop words
b_list = list(b[0])
print('danh sach stop words', b_list)

#tao ra list những từ có trong tiêu đề phim, không bao gồm stop words
a = [x for x in frequency.index if x not in b_list]
print('a', a)

#in ra 10 từ xuất hien nhieu nhất
d = frequency[frequency.index.isin(a)].head(10)
print('10 tu xuat hien nhieu nhat trong tieu de phim')
print(d)
