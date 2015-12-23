
import numpy as np
import matplotlib.pyplot as plt
import statsmodels as sms
import random
import pandas as pd
from numpy.random import *
seed(100)

n = 10

x = randint(100, size = n)
z =randn(n,8) #10サンプル　9変数モデル
eps = randn(n)
x= x.reshape(-1,1)

X = np.hstack((x,z))
df = pd.DataFrame(X)
print(df)