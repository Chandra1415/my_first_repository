from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType
from pyspark.sql.functions import *
import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\sheka\PycharmProjects\PythonProject\.venv\Scripts\python.exe"

schema = StructType([
    StructField("Id", IntegerType(), nullable=True),
    StructField("FIRSTNAME", StringType(), nullable=True),
    StructField("LASTNAME", StringType(), nullable=True),
    StructField("URL", StringType(), nullable=True),
    StructField("CAMPAIGNS", ArrayType(StringType()), nullable=True)
])
data = [
    [1, "nikhil", "rock", "https://tinyurl.8687", ["facebook", "instagram"]],
    [2, "pavan", "kalyan", "https://tinyurl.8681", ["twitter", "fling"]],
    [3, "sai", "arjun", "https://tinyurl.8682", ["whatsapp", "snapchat"]]
]
if __name__ == "__main__":
    spark = SparkSession.builder.appName("sam").getOrCreate()
    df = spark.createDataFrame(data, schema=schema)
    df.show()
    df.printSchema()
    df.select("LASTNAME").show()
    df1 = df.withColumn("Id", df.Id + 12).show()
    df2 = df.withColumn("full_name", concat(col("FIRSTNAME"), lit("_"), col("LASTNAME")))
    df2.show()
    df.show()
