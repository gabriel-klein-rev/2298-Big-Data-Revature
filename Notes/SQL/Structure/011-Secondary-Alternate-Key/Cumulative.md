
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- To define and implement Secondary Key


</details>
<details><summary>Description</summary>
<br>

- A candidate key is a column or a combination of columns that uniquely identifies each row in a table.
- Any table can have only one primary key so all the candidate keys other than the primary key are secondary keys or alternate keys.
- A secondary key and the foreign key are NOT related or the same.
</details>
<details><summary>Real World Application</summary>
<br>

Understanding secondary keys is important for several reasons:

- __Data Integrity__: Secondary keys enforce data integrity by ensuring the uniqueness of values in specific columns. This helps prevent duplicate entries and maintains the consistency and accuracy of the database.

- __Indexing__: Secondary keys are often used to create indexes, which improve the performance of data retrieval operations. By creating indexes on secondary keys, you can speed up queries that involve filtering, sorting, or joining data based on those columns.

- __Query Flexibility__: Secondary keys provide flexibility in querying the database by allowing users to retrieve data based on different criteria. They enable users to perform complex searches and analysis, leading to better insights and decision-making.

In summary, knowing about secondary keys  helps database administrators, developers, and users leverage the full potential of the database system and ensure its reliability and efficiency.

</details>
<details><summary>Implementation</summary> 
<br>

The following table has a secondary key.

``` sql
CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    Barcode VARCHAR(20) UNIQUE,
    Name VARCHAR(100),
    Description TEXT,
    Price DECIMAL(10, 2)
);

```

In this example:

- ProductID is the primary key of the table.
- Barcode is a candidate key since the column is marked as UNIQUE, ensuring each value in that column is unique.

</details>
<details><summary>Summary</summary> 
<br>

- all the candidate keys other than the primary key and foreign key are called secondary keys.

- even if the secondary key is not a primary key, a secondary key or group of secondary keys is used to uniquely identify a record.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
