# Hive Activity 3

Complete the following activity to practice partitioning and bucketing in Hive. Completion of Hive_Activity_2 will be helpful to complete this activity.

### Steps

1. Using the supplied [players.csv](./players.csv) file, create a Hive table called 'players' and load it with the csv data.
    - Note that the csv file has a header.

2. Create a partitioned and bucketed table called 'players_partitioned' which contains the players data partitioned by the Team column and clustered by the Height column. 
    - Use your discretion to determine the number of buckets to use.

3. Query the partitioned table to answer the follwing:
    - The average age of players on each team.
    - The maximum and minimum height of players in the "Catcher" position.
    - The number of players at each position whose age is younger than 25.
    - All teams that contain at least 35 players, in alphabetical order.

4. Query the table to find the 5 "youngest" teams (lowest average age) and save that to a table. Find
the result on HDFS and save to your local machine.
