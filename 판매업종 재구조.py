import numpy as np
import pandas as pd

data_df = pd.read_csv('YogiyoTip.csv',encoding = 'cp949', header=0, engine='python')

data_df = data_df.replace({'판매업종':5,},22)
data_df = data_df.replace({'판매업종':6},23)
data_df = data_df.replace({'판매업종':7},24)
data_df = data_df.replace({'판매업종':8},25)
data_df = data_df.replace({'판매업종':9},27)
data_df = data_df.replace({'판매업종':10},28)
data_df = data_df.replace({'판매업종':11},26)
data_df = data_df.replace({'판매업종':12},21)
data_df = data_df.replace({'판매업종':13},20)

data_df = data_df.replace({'판매업종':22},2)
data_df = data_df.replace({'판매업종':23},3)
data_df = data_df.replace({'판매업종':24},4)
data_df = data_df.replace({'판매업종':25},5)
data_df = data_df.replace({'판매업종':27},7)
data_df = data_df.replace({'판매업종':28},8)
data_df = data_df.replace({'판매업종':26},6)
data_df = data_df.replace({'판매업종':21},1)
data_df = data_df.replace({'판매업종':20},0)

data_df.to_csv("YogiyoTip.csv",encoding = 'cp949', index = False)