# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas
import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test").getOrCreate()

# Read CSV file into table
df = (spark.read.option("header", True).csv("C:/Users/gaura/Downloads/Book1.csv"))
df.printSchema()
df.show()

# Read CSV file into table
spark.read.option("header",True) \
          .csv("C:/Users/gaura/Downloads/Book1.csv") \
          .createOrReplaceTempView("sample1")


# SQL Select query
spark.sql("SELECT A, B, C, D FROM sample1") \
     .show(2)

spark.sql("SELECT A, B, D FROM sample1 where B in ('Gaurav','abs','jdjdee')") \
     .show()




