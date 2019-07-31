
import pandas as pd
from itertools import chain
from collections import Counter
import matplotlib.pyplot as plt

movies = pd.read_csv('movies.csv')

#danh sách các genres xếp theo thứ tự từ phổ biến nhất
frequency = pd.Series(Counter(chain.from_iterable(x.split('|') for x in movies.genres)))\
    .sort_values(ascending=False)

print(frequency)
frequency.plot(kind='bar')
plt.show()
