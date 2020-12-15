import pandas as pd
import numpy as np
import matplotlib.pyplot as py
from scipy.stats import pearsonr


def scale1(x):
    return (x - np.mean(x))/np.std(x)
def scale2(x):
    return (x - np.min(x))/(np.max(x)-np.min(x))

x = [1,2,3,4,5]
y = [2,3,5,6,10]
py.scatter(x,y)

r,p=pearsonr(x,y)
print(r)
x = scale1(x)
y = scale1(y)
py.scatter(x,y,color='r')
py.show()
r,p=pearsonr(x,y)
print(r)