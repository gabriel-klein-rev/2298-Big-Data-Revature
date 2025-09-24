
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- Understand the purpose of a view in SQL
- Create a view in SQL

</details>
<details><summary>Description</summary>
<br>

In SQL (Structured Query Language), a view is a virtual table based on the result of a `SELECT` query. Unlike a physical table, a view does not store the data itself but rather provides a way to represent the result of a query as if it were a table. Views are created for various reasons, such as simplifying complex queries, encapsulating business logic, and providing a layer of security by restricting access to certain columns or rows.

Here are key points about views in SQL:

1. **Definition**: A view is defined by a SELECT statement that specifies the columns and rows to include in the view.
2. **Virtual Table**: A view is not a physical table; it's a virtual table that is dynamically generated when queried.
3. **Simplified Queries**: Views can simplify complex queries by encapsulating the logic in a named structure. This can make it easier to understand and maintain code.
4. **Security**: Views can be used to restrict access to specific columns or rows of a table. Users can be granted permission to access a view without granting direct access to the underlying table.
5. **Abstraction**: Views provide a level of abstraction, allowing users to interact with the data in a way that is more meaningful or convenient for their needs.
6. **Joining Tables**: Views can be used to join multiple tables, making it easier to work with complex data relationships.
7. **Updateable Views**: In some databases, views can be made updateable, allowing users to perform `INSERT`, `UPDATE`, and `DELETE` operations through the view.
 However, this depends on the complexity of the view and the underlying tables.
</details>
<details><summary>Real World Application</summary>
<br>

The decision to use views is often driven by factors such as simplifying complex queries, enhancing security, providing a layer of abstraction, and improving overall system performance. Here are some common reasons why developers use views:

1. **Simplifying Complex Queries**: Views can encapsulate complex SQL logic, making it easier for developers to write and maintain queries. This is particularly useful when dealing with multiple tables, joins, and filtering conditions.
2. **Abstraction and Modularity**: Views provide a level of abstraction, allowing developers to work with a simplified representation of the data. This abstraction promotes modularity and code organization, making it easier to understand and maintain the database schema.
3. **Security and Access Control**: Views can be used to control access to sensitive data. By granting users access to specific views rather than direct access to underlying tables, developers can restrict which columns or rows users are allowed to see. This enhances security and ensures that users only have access to the information they need.
4. **Performance Optimization**: Views can be used to precompute and store the results of complex queries. This can improve query performance by avoiding redundant calculations and aggregations. Additionally, views can be indexed, further enhancing query performance.
5. **Data Aggregation and Transformation**: Views are valuable for aggregating and transforming data. Developers can create views that present data in a format that is more suitable for reporting or analysis. This eliminates the need to repeat complex transformations in multiple queries.
6. **Code Reusability**: Views promote code reusability by allowing developers to define a set of common queries that can be used across different parts of an application. This reduces redundancy and ensures consistency in query logic.
7. **Hiding Complexity**: Views can hide the underlying complexity of the database schema from application developers. This is particularly useful when changes are made to the database structure but the views remain unchanged, preventing the need for extensive modifications in application code.
8. **Joining Tables**: Views simplify the process of joining multiple tables. Instead of writing complex join operations in every query, developers can create a view that encapsulates the necessary joins, making subsequent queries more straightforward.
9. **Versioning and Migration**: Views can be used as an abstraction layer during database versioning and migration. Developers can update the underlying tables without affecting the queries that rely on views, minimizing the impact on the application code.

</details>
<details><summary>Implementation</summary> 
<br>

In this example we will work with two tables. The `players` table will focus on the player information and the `games_played` table, which stores data about each game played and has a foreign key (`player_id`) referencing the players table to establish a relationship between players and the games they've played.

Table 1: players

|player_id|player_name|player_email             |
|---------|-----------|-------------------------|
|        1|Tanisi     |cantstopmenow@example.com|
|        2|Zelda      |mamamia@example.com      |
|        3|ImmaWinner |zeldafan@example.com     |





Table 2: games_played

|game_id|player_id|game_title                             |game_score|
|-------|---------|--------------------------------------|----------|
|    101|        1|The Legend of Zelda: Ocarina of Time   |        95|
|    102|        1|The Legend of Zelda: Breath of the Wild|        98|
|    103|        2|The Legend of Zelda: Twilight Princess |        92|
|    104|        2|The Legend of Zelda: Skyward Sword     |        88|
|    105|        3|The Legend of Zelda: Wind Waker        |        90|
|    106|        3|The Legend of Zelda: A Link to the Past|        94|



Let's consider a scenario where you were tasked with retrieving detailed information about each player along with the games they have played. Assuming we want a view that includes detailed information about each player and the games they have played, we can create a view named `player_games_view`:

**Syntax for Creating a View**:
```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

**Creating a view named player_games_view**:
```sql
-- Create a view to show detailed information about each player and the games they played
CREATE VIEW player_games_view
AS
SELECT p.player_id, p.player_name, p.player_email, g.game_id,g.game_title, g.game_score
FROM players p
JOIN games_played g 
ON p.player_id = g.player_id;
```


This view encapsulates the logic of joining the `players` and `games_played` tables, providing a simplified way to retrieve detailed information about each player and the games they have played.

To see the view we can do a basic SELECT all statement
```sql
SELECT * FROM player_games_view;
```
OUTPUT:

|player_id|player_name|player_email             |game_id|game_title                             |game_score|
|---------|-----------|-------------------------|-------|---------------------------------------|----------|
|        1|Tanisi     |cantstopmenow@example.com|    101|The Legend of Zelda: Ocarina of Time   |        95|
|        1|Tanisi     |cantstopmenow@example.com|    102|The Legend of Zelda: Breath of the Wild|        98|
|        2|Zelda      |mamamia@example.com      |    103|The Legend of Zelda: Twilight Princess |        92|
|        2|Zelda      |mamamia@example.com      |    104|The Legend of Zelda: Skyward Sword     |        88|
|        3|ImmaWinner |zeldafan@example.com     |    105|The Legend of Zelda: Wind Waker        |        90|
|        3|ImmaWinner |zeldafan@example.com     |    106|The Legend of Zelda: A Link to the Past|        94|


</details>
<details><summary>Summary</summary> 
<br>

* A `VIEW`  does not store data itself but provides a way to represent the result of a query as if it were a table.
* `VIEW` promotes code reusability by allowing developers to define common queries that can be used across different parts of an application.
* Views can restrict access to specific columns or rows, enhancing security. Users can be granted permission to access a view without direct access to underlying tables.
* Views simplify complex queries by encapsulating logic, promoting modularity, and providing a level of abstraction. They help developers work with a more manageable representation of the data.


</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
