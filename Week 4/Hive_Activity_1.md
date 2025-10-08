# Hive Introductory Activity

Complete the following steps to interact with the HiveQL and HDFS. 

### Steps
1. Open a Linux Terminal and ssh into your localhost.
2. Start Hive
3. Create a new Hive database called 'test_db'.
4. Inside the 'test_db' database, create a new table called 'FirstTable' with the following fields:
    - ID INT
    - FirstName STRING
    - LastName STRING
    - Gender STRING
    - Age INT
5. Insert 10 records into 'FirstTable' using INSERT.
6. Make the following queries:
    - Query all IDs whose age is greater than 30.
    - Query the first and last names of every male, in alphabetical order.
    - Query the average age per gender.
7. Locate the 'FirstTable' table in the Hive Warehouse. Note the HDFS path to the directory.
8. Once you have found the table, drop it from the 'test_db' database.
9. Drop the 'test_db' database.