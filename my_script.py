from statistics import median

import pandas as pd
"""
df = pd.DataFrame({ 'Yes': [50,20], 'No' : [131,21] })
print(df)

df2= pd.DataFrame({'chandra': ['distinction','first class'], 'Meghana': ['distinction', 'first class'] })
print(df2)

df3 = pd.DataFrame({'Name': ['Meghana','chandra'], 'Score': ['distinction', 'first class'] },
index= [456,451])
print(df3)


v= pd.Series([121,233,345,464,523], index = [2010,2011,2012,2013,2014], name= 'Sales')
print(v)
print(pd.__version__)

a= ['chaitanya', "Hemakanth"]
donga= pd.Series(a, index=['who is theif','nor'])
print(donga)

sict={"day1": "monday","day2":'tuesday','day1':"wed"}
vae= pd.Series(sict, index= ['day1',"day2"])
print(vae)

"""
v = pd.read_csv(r"C:\Users\sheka\Downloads\inputEmp_tq.txt")
print(v)


