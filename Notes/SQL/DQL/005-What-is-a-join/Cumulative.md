
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- Define what a join is
- Understand the importance of joins in SQL
</details>
<details><summary>Description</summary>
<br>

In relational databases, data stored in multiple tables is related to one another with a common key value. This relation is established by a foreign key inside of the child table linking to the parent. There is a constant need to extract the records from related tables to obtain the full picture of the information stored in our database. After applying some condition, this joined information is compiled together based on the type of join and using SQL's `JOIN` clause. This `JOIN` clause is a part of the DQL and used in queries to access multiple tables, based on the logical relationships of those two tables and join that information together in the output as a single table. There are several different types of SQL `JOIN` clauses that will be explained in other modules.
</details>
<details><summary>Real World Application</summary>
<br>

In businesses when they are looking to analyze metrics for quarterly business profits, they have queries that pull information from multiple tables across their entire database. This would include joining information from sales & product information to see how much profit is being obtained in sales verse the cost of maintain all of those products. `JOIN` clauses are frequently used to handle such things as the above. Along with this you could also query and join information for customer orders that could track the category of products that are selling most. There is a nearly endless amount of uses for `JOIN` clauses in a business for analytics to help improve the business as a whole.



</details>
<details><summary>Implementation</summary> 
<br>

- Basic SQL `JOIN` Clause syntax, using `INNER JOIN` to show basic syntax.

```sql
SELECT 
TABLE_NAME1.column1, TABLE_NAME1.columnN, TABLE_NAME2.column1, TABLE_NAME2.columnN
FROM TABLE_NAME1
INNER JOIN TABLE_NAME2
ON TABLE_NAME1.matching_column = TABLE_NAME2.matching_column;
```

</details>
<details><summary>Summary</summary> 
<br>

This `JOIN` clause is a part of the DQL and used in queries to access multiple tables, based on the logical relationships of those two tables and join that information together in the output as a single table. 
- There are several different types of SQL `JOIN` clauses.
- This relation is established by a foreign key inside of the child table linking to the parent used at the 'matching_column' for the join. 
- There is a constant need to extract the records from related tables to obtain the full picture of the information stored in the business's database. 
- After applying some condition, this joined information is compiled together based on the type of join and using SQL's `JOIN` clause. 
</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
