import pandas as pd
import json

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df=pd.read_csv(r'C:\Users\keash\Desktop\Test.csv')
summary_df=df.iloc[0:6]
summary_df=summary_df.dropna(axis=1,how='any')
summary_df=summary_df.drop(summary_df.columns[-1],axis=1)
summary_df.columns=['Region','Total Cases','New Cases','Total Deaths','New Deaths','Total Recoverd','New Recovered','Active Cases','Serious Critical']
summary_df.to_json('COVID19_Summary.json',orient='records')

country_df=df.iloc[8:]
country_df=country_df.drop(country_df.columns[0:3],axis=1)
error_list=country_df[country_df['7'].isnull()]
error_list2=error_list[error_list['11'].isnull()]
print(error_list2.head(10))