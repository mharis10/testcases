# -*- coding: utf-8 -*-
"""testcases1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EGhpHj157Wlib_MlqIqX6td4SrRjg7u4
"""

import pandas as pd 
import numpy as np

data = pd.read_csv('TestData.csv',encoding='latin-1')

data['Test Case Failed']= ''
data = data.replace(np.nan,'',regex=True)
data.insert(0, 'ID', range(0, len(data)))

#testcase1
data_1 = data[(((data['Gender'] == 'Male') & (data['SRGender'] == 'Male')) & 
              (
                  (data['PrimAddText'].str.contains('Ms')) | (data['PrimAddText'].str.contains('Mrs')) | 
                  (data['PrimSalText'].str.contains('Ms')) | (data['PrimSalText'].str.contains('Mrs'))
                  ))]
ids = data_1.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 1'

#testcase2
data_2 = data[(((data['Gender'] == 'Female') & (data['SRGender'] == 'Female')) & 
              (
                  (data['PrimAddText'].str.contains('Ms')) | (data['PrimAddText'].str.contains('Mrs')) | 
                  (data['PrimSalText'].str.contains('Ms')) | (data['PrimSalText'].str.contains('Mrs'))
                  ))]
ids = data_2.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 2'

#testcase 3
data_3 = data[(data['FirstName'] == data['SRFirstName'])]
ids = data_3.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 3'

#testcase 4
def find_value_column(row):
    return row.LastName not in row.PrimSalText

data_4 = data[data.apply(find_value_column, axis=1)][['LastName', 'PrimSalText']]
ids = data_4.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 4'

#testcase 4
def find_value_column(row):
    return row.LastName not in row.PrimAddText

data_4 = data[data.apply(find_value_column, axis=1)][['LastName', 'PrimAddText']]
ids = data_4.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 4'

data["Test Case Failed"].replace({", 4, 4": ", 4"}, inplace=True)
data["Test Case Failed"].replace({", 3, 4, 4": ", 4"}, inplace=True)
data["Test Case Failed"].replace({", 2, 4, 4": ", 4"}, inplace=True)
data["Test Case Failed"].replace({", 1, 4, 4": ", 4"}, inplace=True)

#testcase5
df = data[((data['FirstName']!='') & (data['LastName']!='')) & 
              ((data['SRFirstName']!='') & (data['SRLastName']!='') &
              (data['SRDeceased'].str.contains('Yes')==False) & (data['Deceased'].str.contains('Yes')==False) 
              )]
df1 = df[df['PrimAddText'].str.contains("AND|&")==False] 
data_5 = df1[df1['PrimSalText'].str.contains("AND|&")==False] 
ids = data_5.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 5'

#testcase 6
data['BDay']= pd.to_datetime(data['BDay'])
data_6 = data.loc[data['BDay'] >= '01/01/2004']
ids = data_6.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 6'

#testcase 7 
df = data[data['SRDeceased'] == 'Yes']
df = df[df['PrimAddText'].str.contains("AND|&")]
data_7 = df[df['PrimSalText'].str.contains("AND|&")]  
ids = data_7.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 7'

#testcase 8 
df = data[(data['SRLastName'] == '') | (data['SRFirstName']=='')]
df = df[df['PrimAddText'].str.contains("AND|&", na=False)]
data_8 = df[df['PrimSalText'].str.contains("AND|&", na=False)]  
ids = data_8.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 8'

#testcase 9
data_9 = data[((data['SRDeceasedDate'] != '') & (data['MrtlStat'] != 'Widowed'))]
ids = data_9.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 9'

#testcase 10
data_10 = data[(data['SRDeceasedDate']!='') & (df['SRInactive']!='Yes')]
ids = data_10.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 10'

#testcase 11
data_11 = data[(data['DeceasedDate']!='') & (data['Inactive']!='Yes')]
ids = data_11.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 11'

#testcase 12
df = data[(data['SRDeceasedDate']!='')]
df = df[df['PrimAddText'].str.contains("AND|&", na=False)]
data_12 = df[df['PrimSalText'].str.contains("AND|&", na=False)]  
ids = data_12.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 12'

#testcase13
df = data[((data['SRLastName'] != '') | (data['SRFirstName'] != ''))]
data_13 = df[df['MrtlStat'] == 'single']
ids = data_13.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 13'

#testcase 14
df = data[data['MrtlStat'] == '']
df = df[df['PrimAddText'].str.contains("AND|&", na=False)]
data_14 = df[df['PrimSalText'].str.contains("AND|&", na=False)]
ids = data_14.index.tolist()
for i in ids:
  data.at[i,'Test Case Failed']+=', 14'

#data.iloc[70:90]
#data.head()

#data['Test Case Failed'].unique()

#(data['Test Case Failed'].values == '').sum()

final = data[(data['Test Case Failed'] != '')]
#final.head(50)

passed = data[(data['Test Case Failed'] == '')]

#final['Test Case Failed'].unique()
#passed.head()

final['Test Case Failed'] =final['Test Case Failed'].str[1:]

final = final[(final['Test Case Failed'] != '')]

del final["ID"]

del passed["ID"]

final['Test Case Failed'].value_counts()

print("There were a total of",data.shape[0], "rows.", final.shape[0], "rows failed atleast one test case")

final.to_csv('result.csv', index = False)

passed.to_csv('passed.csv', index = False)