import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

#df = pd.read_csv("배달앱_이용현황.csv", encoding='utf-8-sig')
df = pd.read_csv("배달앱_이용현황.csv", encoding='cp949')

years = [2018,2019,2020,2021]

for idx, year in enumerate(years):
    plt.subplot(2,2,idx + 1)
    plt.title(f"{year}년도 배달앱 이용 현황")
    plt.pie([df[f'{year}'][22],df[f'{year}'+'.1'][22]],
            labels = ['예','아니오'],colors=['c','orange'], autopct='%.1f%%')

plt.show()