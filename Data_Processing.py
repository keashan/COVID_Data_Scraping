import pandas as pd
import json

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df=pd.read_csv(r'C:\Users\keash\Desktop\Test.csv')
summary_df=df.iloc[0:6]
summary_df=summary_df.dropna(axis=1,how='any')
summary_df=summary_df.drop(summary_df.columns[-1],axis=1)
summary_df.columns=['Region','Total Cases','New Cases','Total Deaths','New Deaths','Total Recoverd','New Recovered','Active Cases','Serious Critical']
dict={}
for index,item in summary_df.iterrows():
    dict[index]=item.to_dict()
summary_json=json.dumps(dict)
print( dict)