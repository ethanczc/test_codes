# Demo code, import class from DataFilter.py
from DataFilter import *

sample = [0.9,1.0,1.1,0.9,1.0,1.1,1.1,1.1,0.1,1.8,0.5,0.8,0.1,1.3]
mean = DataFilter.GetMean(sample)
print(mean)