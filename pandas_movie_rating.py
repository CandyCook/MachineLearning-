import pandas as pd
import numpy as np
import string
import matplotlib.pyplot as plt

movie = pd.read_csv('movie.csv')
rating = movie['Rating']
runtime = movie['Runtime (Minutes)']

fig = plt.figure(figsize = (20,12))
ax1 = fig.add_subplot(121)
bins =10
rating_range = np.linspace(rating.min(),rating.max(),bins,round(1))

bin_width = 10
ax1.set_title('电影评分分布')
ax1.set_xticks(rating_range)
ax1.set_xlabel("电影评分")
ax1.set_ylabel('电影数量')
plt.hist(rating,bins)

ax2 = fig.add_subplot(122)
bins =10
runtime_range = np.linspace(runtime.min(),runtime.max(),bins,round(1))
bin_width = 10
ax2.set_title('电影评分分布')
ax2.set_xticks(rating_range)
ax2.set_xlabel("电影评分")
ax2.set_ylabel('电影数量')
plt.hist(runtime,bins)
plt.show()