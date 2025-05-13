from pyspark import *
from pyspark.sql import *
from pyspark.sql.types import *
#import my_script as pd
import pandas as pd
#import pyodbc
import os

3

schema = StructType([
    StructField("name", StringType(), nullable=False),
    StructField("age", IntegerType(), nullable=False),
    StructField("DOB", StringType(), nullable=True)
])

list = [("Ram", 24, "20-11-2000"), ("Sham", 22, "20-11-2002")]

svar = SparkSession.builder.appName("app234").getOrCreate()
sdfvar = svar.createDataFrame(list, schema)

schema2 = StructType([
    StructField("name",StringType(), nullable=False),
    StructField("Qualification",StringType(),False),
    StructField("collage",StringType(),False),
    StructField("currentorg",StringType(),False)

])
list2=[("Ram","B-Tech","CBIT","Capgemini"),("James","Bse","NNRG","Astra")]
sdfvar2 = svar.createDataFrame(list2,schema2)

#var1 = sdfvar[['name']].show()#to get column data
#ar2 =sdfvar[sdfvar["name"]=="Ram"].show()

pdvar=sdfvar.toPandas()
pdvar2=sdfvar2.toPandas()

var3 = pd.merge(pdvar,pdvar2, on="name",how="inner")
print(var3)