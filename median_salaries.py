from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col, collect_list

# Define the schema
schema = StructType([
    StructField("ID", IntegerType(), True),
    StructField("Name", StringType(), True),
    StructField("salary", IntegerType(), True),
    StructField("department", StringType(), True)
])

# Sample data
data = [
    [1, "nikhil", 60000, "it"],
    [2, "sds", 60000, "it"],
    [3, "hari", 60000, "it"],
    [4, "pan", 70000, "hr"],
    [5, "venkat", 80000, "hr"]
]

from pyspark import SparkConf, SparkContext

conf = SparkConf().set("spark.ui.port", "4050")
sc = SparkContext(conf=conf)


# Initialize Spark session
spark = SparkSession.builder.appName("MedianSalary").config("spark.ui.enabled", "true").getOrCreate()

# Create DataFrame
var2 = spark.createDataFrame(data, schema)
var2.show()

# Group salaries by department
s_d = var2.groupBy("department").agg(collect_list("salary").alias("salaries"))

# Define the function to calculate the median
def calculate_median(salaries):
    sorted_salaries = sorted(salaries)
    n = len(sorted_salaries)
    if n % 2 == 0:
        return (sorted_salaries[n // 2 - 1] + sorted_salaries[n // 2]) / 2.0
    else:
        return float(sorted_salaries[n // 2])

# Register the UDF
from pyspark.sql.functions import udf
from pyspark.sql.types import FloatType

median_udf = udf(calculate_median, FloatType())

# Calculate median salary for each department
median_salaries = s_d.withColumn("median_salary", median_udf(col("salaries")))

# Show the results
median_salaries.select("department", "median_salary").show()

import time
time.sleep(300) 