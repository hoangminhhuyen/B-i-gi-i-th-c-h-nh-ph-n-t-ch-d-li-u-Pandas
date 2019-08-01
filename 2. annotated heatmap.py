import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

movies = pd.read_csv('movies.csv')

#tách year ra khỏi title
movies["year"] = movies["title"].apply(lambda x: x[-5:-1])
#lọc ra những year NaN
movies.year=pd.to_numeric(movies['year'],errors='coerce',downcast='integer')
#print(movies)

# Tao dummies
movies = movies.join(movies.genres.str.get_dummies())

# Tao bang correlation
a = movies.loc[:, "(no genres listed)":"Western"].corr().round(1)
print(a)

plt.yticks(np.arange(0.5, len(a.index), 1), a.index)
plt.ylabel("genres")
plt.xticks(np.arange(0.5, len(a.index), 1), a.index) 
plt.xlabel("genres")
plt.pcolor(a)

for i in range(len(a.columns)):
    for j in range(len(a.index)):
        plt.text(0.5 + i, 0.5 + j, a.iat[j, i],
ha="center", va="center", color="r")

plt.show()
