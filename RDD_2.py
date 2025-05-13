from pyspark.sql import SparkSession

# Step 1: Create Spark session
spark = SparkSession.builder \
    .appName("Basic RDD Transformations") \
    .master("local[*]") \
    .getOrCreate()

# Step 2: Create raw data (list of tuples)
data = [("Alice", 34), ("Bob", 23), ("Charlie", 29), ("David", 19), ("Eva", 42)]

# Step 3: Convert data to RDD
rdd = spark.sparkContext.parallelize(data)

# Step 4: Apply a filter transformation (only people over 25)
filtered_rdd = rdd.filter(lambda x: x[1] > 25)

# Step 5: Map transformation - convert to dictionary-like format
mapped_rdd = filtered_rdd.map(lambda x: {"name": x[0], "age": x[1]})

# Step 6: Count action - how many people are over 25
count = mapped_rdd.count()
print(f"Number of people over 25: {count}")

# Step 7: Collect and print the final RDD
result = mapped_rdd.collect()
for person in result:
    print(person)

# Optional: Save result to a file (each worker writes a part)
# mapped_rdd.saveAsTextFile("output_folder")

# Step 8: Stop Spark session
spark.stop()
