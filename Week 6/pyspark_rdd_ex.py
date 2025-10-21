from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("pyspark Example").getOrCreate()
sc = spark.sparkContext

sc.setLogLevel("WARN")

rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = rdd1.map(lambda x: x * 10)

print(rdd2.collect())

spark.stop()