import pandas as pd

# drive.mount('/content/drive')

# df=pd.read_csv('drive/MyDrive/CSE587-DIC/data.csv')

def func():
  df=pd.read_csv('../python/data_phase2.csv')

  to_drop = ['Unnamed: 0']

  df.drop(to_drop, inplace=True, axis=1)

  df= df.dropna()
  print(df)

func()