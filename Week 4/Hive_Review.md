# Hive Review

### What is Hive?
- Hive gives an SQL-like interface to query data that interfaces with Hadoop

### Where is the default location of Hive's data in HDFS?
- /user/hive/warehouse

### What is an External table?
- A table whose data is stored outside of Hive’s structure. The data is not lost when drop is used on an external table

### What is a managed table?
- A table whose data is stored in hive. If dropped, the data is removed.

### What is a Hive partition?
- A way of dividing a table into related parts based on the values of particular columns

### Provide an example of a good column or set of columns to partition on.
- A good column to partition on is one where there might be many duplicate elements so as not to create too many directories  for small partitions

### What's the benefit of partitioning?
- Queries on smaller pieces of data become much faster if you only have to search through one or few partitions

### What does a partitioned table look like in HDFS?
- Each partition is stored in its own directory in HDFS with each row as a file within

### What is a Hive bucket?
- Bucketing in Hive groups the data by ranges of values of a column or combination of columns.

### What does it mean to have data skew and why does this matter when bucketing?
- Skew data is data that is very far off from the rest of the data in a table. For example, a field having a very large number when all the other values in the column are quite small. If skew data is not handled, the ranges for the buckets might not be optimized. 

### What does a bucketed table look like in HDFS?
- The buckets are stored as separate files with the rows that fall into each bucket contained within.

### Hive syntax: Create a table?
- Example:
    - ```CREATE TABLE <table_name> (column_names DATATYPE,…) row format deliminated fields terminated by ‘<deliminator>’ stored as textfile;```

### Hive syntax: Load data into a table?
- Example:
    - ```LOAD DATA INPATH ‘<path>’ INTO TABLE <table_name>;```