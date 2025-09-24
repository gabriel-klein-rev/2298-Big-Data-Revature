
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- understand the purpose of indexes in SQL


</details>
<details><summary>Description</summary>
<br>

In SQL (Structured Query Language), an index is a database object that provides a fast and efficient way to look up and retrieve data from a table. It works similarly to an index or bookmark in a book, helping you quickly find information without having to scan the entire content. The primary purpose of an index is to improve the performance of `SELECT` queries by reducing the amount of data that needs to be scanned.

Here are some key points about indexes in SQL:

1. **Structure**: An index is typically a data structure that stores a sorted or hashed subset of the data in a table. It consists of key columns and corresponding pointers to the actual data rows in the table.
2. **Types of Indexes**:
    * **Clustered Index**: The rows of the table are stored in the order of the index key. Each table can have only one clustered index.
    * **Non-Clustered Index**: The index key contains a sorted order of the data, but the actual data rows are stored separately from the index.
3. **Advantages**:
    * **Improved Query Performance**: Indexes significantly speed up the retrieval of data for SELECT queries, especially when searching or sorting based on indexed columns.
    * **Faster Joins**: Indexes can enhance the performance of join operations between tables.
    * **Unique Constraints**: Unique indexes enforce the uniqueness of values in one or more columns.
4. **Disadvantages**:
    * **Overhead on Write Operations**: While SELECT queries benefit from indexes, write operations (INSERT, UPDATE, DELETE) can be slower because indexes need to be updated along with the data.
    * **Storage Overhead**: Indexes consume additional storage space.
5. **Creating and Managing Indexes**:
    * Indexes are created using the `CREATE INDEX` statement.
    * They can be dropped using the `DROP INDEX` statement.
    * Some databases automatically create indexes for primary keys and unique constraints.
</details>
<details><summary>Real World Application</summary>
<br>

Developers use indexes for several reasons to improve the performance and efficiency of database operations. 

1. **Faster Data Retrieval**: Indexes allow for faster retrieval of data from a database. When a query filters or sorts data based on indexed columns, the database engine can quickly locate the relevant rows without scanning the entire table.
2. **Optimized Query Performance**: Queries that involve conditions, sorting, or joining on indexed columns generally perform better. Indexes help reduce the number of rows that need to be examined, resulting in quicker query execution times.
3. **Enhanced JOIN Operations**: Indexes improve the performance of JOIN operations, especially when joining tables on columns that are indexed. This is crucial for scenarios where data from multiple tables needs to be combined.
4. **Unique Constraints**: Indexes can enforce the uniqueness of values in one or more columns, ensuring that no duplicate values exist. This is beneficial for maintaining data integrity, especially in columns representing primary keys or unique constraints.
5. **Accelerated Aggregations**: Queries that involve aggregate functions (e.g., SUM, AVG, COUNT) on indexed columns can be processed more efficiently, leading to faster results.
6. **Increased Concurrency**: Indexes can enhance the concurrency of database operations by reducing the time it takes to read and write data. This is particularly important in applications with a high level of simultaneous database access.
7. **Optimized ORDER BY and GROUP BY**: Indexes can significantly improve the performance of queries involving sorting (`ORDER BY`) and grouping (`GROUP BY`). The database engine can leverage the sorted order provided by indexes.
8. **Efficient WHERE Clauses**: Queries with filtering conditions (`WHERE` clauses) on indexed columns benefit from quicker data retrieval. The database engine can quickly identify the relevant rows that satisfy the conditions.
9. **Improved Performance for Joins**: When joining multiple tables, indexes on the join columns can significantly reduce the time it takes to match and retrieve the related rows.
10. **Minimized Disk I/O**: Indexes reduce the amount of disk I/O by allowing the database engine to locate data more efficiently. This is crucial for applications where minimizing disk reads and writes is essential for performance.

It's important to note that while indexes provide performance benefits, they also come with some trade-offs, such as increased storage requirements and potential overhead on write operations. 
Therefore, developers should carefully consider the specific requirements of their applications and choose indexes judiciously based on the types of queries are commonly executed.

</details>
<details><summary>Implementation</summary> 
<br>

In this example we have a `Users` table and an `Accounts` table.

**Table 1**: Users

|userid|username     |email                  |
|------|-------------|-----------------------|
|     1|LolipopMagee |Sarah.Magee@example.com|
|     2|ToBeOrNotToBe|harry.smith@example.com|
|     3|JingleTrees  |bob.johnson@example.com|



**Table 2**: Accounts

|accountid|userid|accountnumber|balance|
|---------|------|-------------|-------|
|      101|     1|A123456      |1000.00|
|     102|     2|B789012      |2500.50|
|      103|     3|C345678      | 500.25|



Let's create a clustered index on the `Accounts` table based on the `accountid` column, and a non-clustered index on the `Users` table based on the `userid` column:

```sql
-- Create a Non-Clustered Index on Users table
CREATE INDEX idx_UserID ON Users (userid);

-- Create a Non-Clustered Index on Accounts table
CREATE INDEX idx_AccountID ON Accounts (accountid);

-- Cluster the Accounts table based on the idx_AccountID index
CLUSTER Accounts USING idx_AccountID;
```

* The first statement will create a non-clustered index named `idx_UserID` on the `Users` table.
* The second statement will create a non-clustered index named `idx_AccountID` on the `Accounts` table.
* The third statement will use the `CLUSTER` command to physically reorder the `Accounts` table based on the `idx_AccountID` index.

Please note that you run these statements in order due to the index having to exist before you can cluster, and the index `idx_AccountID` is created successfully before attempting to cluster the table. In PostgreSQL, the `CLUSTER` command requires an existing index to be specified, and the index must be created before attempting to cluster the table. 
The order of execution is crucial. Always refer to the specific documentation of the database system being used, as the syntax and behavior of commands like `CLUSTER` can vary between database management systems.

If you clustered a table using the `CLUSTER` command, you can verify the clustering effect by checking the physical order of the table. This can be done using a simple `SELECT` statement without any ordering.

Example:
```sql
SELECT * FROM Accounts;
```

If the `Accounts` table was clustered based on the specified index, you may notice that the rows are physically ordered according to the clustered index.

Always ensure to review the actual execution plans, results, and any related metrics to validate that your queries are performing as expected. It's a good practice to test queries with different data scenarios to ensure robustness.

Things to take into consideration when creating indexes include:

1. **Consideration of Query Patterns**:
    * When creating indexes, it's essential to consider the specific columns that will be used in SQL queries. Indexes should be designed to optimize the performance of frequently executed queries.
    * Identify columns used in WHERE clauses, JOIN conditions, and ORDER BY clauses, as these are common candidates for indexing.
2. **Importance of Indexes on Large Tables**:
    * Indexes play a crucial role in optimizing query performance, especially on large tables. They help reduce the amount of data that needs to be scanned, improving the speed of data retrieval.
    * For large tables, well-designed indexes can significantly enhance the efficiency of queries by allowing the database engine to quickly locate and retrieve relevant rows.
3. **Consideration for Small Tables**:
    * On small tables, the overhead of maintaining indexes may outweigh the performance benefits. In some cases, a full table scan (reading sequentially) might be faster than using an index, especially when most or all rows are accessed.
    * Developers should carefully assess the size and usage patterns of tables before deciding to create indexes.
4. **Sequential Reading vs. Index Access**:
    * When a query needs to access a large portion of the rows in a table, a sequential read might be faster than working through an index. In such cases, the database engine may choose to perform a full table scan instead of using an index.
5. **Balancing Write Performance and Read Performance**:
    * It's crucial to strike a balance between read and write performance. While indexes improve read performance, they may introduce overhead during write operations (`INSERT`, `UPDATE`, `DELETE`). This is an important trade-off to consider.
6. **Regular Monitoring and Optimization**:
    * Database performance should be regularly monitored, and index strategies should be optimized based on changing usage patterns. Periodic review and adjustment of indexes can help maintain optimal performance.

Creating indexes requires thoughtful consideration of the specific queries your application executes and the characteristics of your data. Regular performance monitoring and adjustments to index strategies are essential for ensuring efficient database operations over time.


</details>
<details><summary>Summary</summary> 
<br>

* **Query Optimization**: Indexes are crucial for optimizing query performance, particularly for queries that involve filtering, sorting, or joining on specific columns.
* **Column Selection**: Choose columns for indexing based on their usage in `WHERE` clauses, JOIN conditions, and `ORDER BY` clauses in frequent queries.
* **Large Table Performance**: Indexes play a critical role in enhancing the performance of queries on large tables by reducing the amount of data that needs to be scanned.
* **Trade-Offs on Small Tables**: On small tables, the overhead of maintaining indexes may outweigh performance benefits. Carefully evaluate the size and usage patterns of tables before creating indexes.
* **Balancing Read and Write Performance**: Striking a balance between read and write performance is essential. Indexes improve read performance but may introduce overhead during write operations.
* **Regular Monitoring and Optimization**: Periodically monitor and optimize index strategies based on changing usage patterns. Regular reviews help maintain optimal database performance.
* **Sequential Reading vs. Index Access**: Consider the trade-off between sequential reading and index access, especially when a query needs to access a large portion of rows in a table.
* **Consideration for WHERE, JOIN, ORDER BY**: Index columns commonly used in `WHERE` clauses, JOIN conditions, and `ORDER BY` clauses for effective optimization.
* **Unique Constraints**: Indexes are useful for enforcing unique constraints on columns, ensuring data integrity.
* **Use with Caution on Write-Intensive Tables**: Be cautious with indexes on tables with heavy write operations, as they may introduce additional overhead.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
