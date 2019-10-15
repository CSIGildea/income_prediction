from math import pow, sqrt
import pandas as pd
import numpy as np

test = pd.read_csv('tcd ml 2019-20 income prediction submission file.csv')
sample = pd.read_csv('previous_best.csv')


mean_square = 0
for i in range(len(test)):
    mean_square += pow((test['Income'][i] - sample['Income'][i]),2)
    if i!= 0:
        mean_square = mean_square/2

print('Root mean square to previous best')
print(sqrt(mean_square))
