
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- Describe the use of set operators in a database
- Different types of set operators 

</details>
<details><summary>Description</summary>
<br>

- SET Operators are specific type of operators which are used to combine the result of two queries.

- Operators covered under SET operators are:
    - `UNION`
    - `UNION ALL`
    - `INTERSECT`
    - `MINUS` / `EXCEPT`

- Two important rules to perform SET operations are:
    - The order and number of columns must be same.
    - Data types must be compatible.

</details>
<details><summary>Real World Application</summary>
<br>

Set operators are commonly used by developers to perform operations on sets of data. In the context of databases and SQL (Structured Query Language), set operators are particularly useful. Here are some reasons why developers use set operators:

1. **Data Retrieval and Filtering**:
    * **Union (UNION)**: Developers use the UNION operator to combine the results of two or more SELECT statements, eliminating duplicate rows. This is useful when working with datasets that have similar structures or when aggregating data from multiple sources.
    * **Intersect (INTERSECT)**: The INTERSECT operator is used to retrieve common rows from two SELECT statements. It helps identify the shared elements between two datasets, which can be beneficial for various analysis tasks.
    * **Except (EXCEPT or MINUS)**: The EXCEPT operator (MINUS in some databases) is used to retrieve rows from the first SELECT statement that are not present in the second SELECT statement. This is helpful for finding the difference between two datasets.
2. **Data Cleaning and De-duplication**:
    * Set operators, especially UNION, are valuable for cleaning and deduplicating data. By combining datasets and removing duplicates, developers can ensure data integrity and accuracy.
3. **Complex Query Construction**:
    * Set operators enable developers to construct complex queries by combining multiple sets of data. This is useful for generating reports, analytics, and insights from diverse sources.
4. **Optimizing Queries**:
    * Set operators can be used to optimize queries by breaking down complex problems into simpler, modular components. This can make queries more readable, maintainable, and efficient.
5. **Logical Operations**:
    * Set operators mimic logical operations on sets, making it easier for developers to express complex conditions. For example, UNION corresponds to a logical OR operation, INTERSECT to a logical AND operation, and EXCEPT to a logical NOT operation.
6. **Data Analysis and Reporting**:
    * In scenarios where developers need to analyze data from different perspectives or generate reports that involve merging or comparing datasets, set operators provide a convenient way to accomplish these tasks.
7. **Database Query Optimization**:
    * Set operators can be leveraged to optimize database queries, allowing developers to retrieve the required information with minimal resource usage and improved performance.

Set operators, particularly in databases, help developers manipulate and analyze sets of data efficiently, enabling them to perform tasks such as data retrieval, filtering, cleaning, and complex query construction.
</details>
<details><summary>Implementation</summary> 
<br>

This example will use two tables, `businesses` and `sales`:

**Table 1**: businesses

|business_id|business_name        |
|-----------|---------------------|
|          1|Fashion Excess Cloths|
|          2|High Fashion Shoes   |



**Table 2**: sales 

|sale_id|business_id|product_id|quantity|total_amount|
|-------|-----------|----------|--------|------------|
|      1|          1|       101|       3|      300.00|
|      2|          1|       102|       2|      200.00|
|      3|          2|       101|       5|      500.00|
|      4|          2|       103|       4|      400.00|



## UNION 

The SQL `UNION` operator merges the result sets of multiple SELECT statements into a single result set, removing duplicates. Ensure that the number and data types of columns in the SELECT statements match to avoid errors; for instance, a SELECT with 2 columns cannot be combined with another having 3 columns.


```sql
-- UNION: Get a combined list of all unique products sold across businesses
SELECT product_id
FROM (
    SELECT product_id FROM sales
    WHERE business_id IN (SELECT business_id FROM businesses)
    UNION
    SELECT product_id FROM sales
) AS union_result;
```
A list of unique `product_id` values that have been sold across all businesses. Duplicates are automatically removed by UNION .

The subquery before `UNION` selects the products with the product_id of 101, 102, and 103. The result of `UNION` will remove duplicates, so the output will be: 101, 102, 103.

**OUTPUT**:

|product_id|
|----------|
|       102|
|       101|
|       103|


If you wanted to include duplicate values you could use `UNION ALL`. 
```sql
-- UNION ALL: Get a combined list of all products sold across businesses (including duplicates)
SELECT product_id
FROM (
    SELECT product_id FROM sales
    WHERE business_id IN (SELECT business_id FROM businesses)
    UNION ALL
    SELECT product_id FROM sales
) AS union_all_result;
```
`UNION ALL` differs from `UNION` in that it does not remove duplicate rows; it includes all rows from the combined result sets.

The subquery before `UNION ALL` selects products with the product_id of 101, 102, and 103.

**OUTPUT**:

|product_id|
|----------|
|       101|
|       102|
|       101|
|       103|
|       101|
|       102|
|       101|
|       103|




## INTERSECT

The `INTERSECT` operator in SQL is used to retrieve the common rows that appear in the result sets of two SELECT statements. It returns only the distinct rows that exist in both result sets.

NOTE: MySQL **does not** support the `INTERSECT` clause. Achieve similar functionality using `INNER JOIN` or `IN` clauses. Always refer to the database documentation to ensure the correct usage of these clauses.

```sql

-- INTERSECT: Get a list of products sold in common across all businesses
SELECT product_id
FROM (
    SELECT product_id FROM sales
    WHERE business_id = 1
    INTERSECT
    SELECT product_id FROM sales
    WHERE business_id = 2
) AS intersect_result;
```
The subqueries selects the products with the `product_id` of 101. The result of `INTERSECT` will include `product_id` 101, which is common to both businesses.


**OUTPUT**:

|product_id|
|----------|
|       101|



## EXCEPT

The `EXCEPT` operator in SQL is used to retrieve the rows that are present in the result set of the first SELECT statement but not in the result set of the second SELECT statement. It returns the distinct rows from the first result set that do not appear in the second result set. 


```sql
-- EXCEPT: Get a list of products sold in the first business but not in the second business
SELECT product_id
FROM (
    SELECT product_id FROM sales
    WHERE business_id = 1
    EXCEPT
    SELECT product_id FROM sales
    WHERE business_id = 2
) AS except_result;
```

The first subquery selects `product_id` 101 and 102. While the second subquery selects `product_id` 101.The result of `EXCEPT` will exclude product_id 102, which is sold in the first business but not in the second.



**OUTPUT**:

|product_id|
|----------|
|       102|



Note that the `MINUS` clause, found in some databases, is functionally equivalent to the `EXCEPT` clause. For example, in PostgreSQL or Oracle, you can replace `EXCEPT` with `MINUS` in your queries. Always refer to the database documentation to ensure the correct usage of these clauses.

</details>
<details><summary>Summary</summary> 
<br>

* The `UNION` command is used to combine the results of two or more SELECT queries into a single result set that includes all the rows from the individual SELECT queries.
* `UNION ALL`  command will return duplicate values.
* The number of columns and their data types in the SELECT statements must be the same for a `UNION` operation to work. This ensures that corresponding columns in the combined result set align properly.
* The `EXCEPT` operator in SQL is used to retrieve the rows that are present in the result set of the first SELECT statement but not in the result set of the second SELECT statement.
* The `INTERSECT` operator in SQL is used to retrieve the common rows that appear in the result sets of two SELECT statements. It returns only the distinct rows that exist in both result sets.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
