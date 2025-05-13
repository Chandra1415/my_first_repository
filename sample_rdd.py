from pyspark import *
from pyspark.sql import *
svar=SparkSession.builder.appName("app1").getOrCreate()
var1= [1,2,3,4,5]
svar2=svar.sparkContext.parallelize(var1).collect()

print(svar2)