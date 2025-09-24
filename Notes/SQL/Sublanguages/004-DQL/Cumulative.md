
<details><summary>Learning Objectives</summary>

<br>

After completing this module, associates should be able to:

- Describe the DQL sublanguage
- Identify the command set of DQL
- Execute DQL statements on a RDBMS

</details>
<details><summary>Description</summary>
<br>

The Data Query Language is the SQL sublanguage used for querying data from the database. It is the major sublanguage used by applications to search, project, filter, join, aggregate and group data for displaying application state.

## Commands

Unlike the other sublanguages, DQL is only associated with a single command

- SELECT

The `select` command is used to build data queries.

</details>
<details><summary>Real World Application</summary>
<br>

The DQL sublanguage is the most widely used sublanguage in enterprise applications. Application developers use DQL `select` statements in combination with platform specific database libraries to query for data. Let's highlight a few enterprise application use cases of DQL.

E-Tail applications like Amazon, Walmart, and Best Buy may use DQL to

- Query a database for the items in a user's shopping cart.
- Query the database for the quantity of items left in inventory.
- Query for a list of specials, sales, or targeted items based on user history.
- Query a database for item information to craft UI elements.

Content driven applications like Youtube, Twitch, Twitter, and Facebook use DQL to

- Query a database for user authentication information.
- Query a database for content based on user feeds.
- Query a database to highlight trending or viral content.
- Query a database to deliver usage information for 3rd party applications.

Search engines like Google, Bing, and Yahoo use DQL to

- Query for url data based on user queries.
- Query for common questions to provide search suggestions.
- Query for ads based on user queries.
- Query for user search history.

The use cases go on and on. The main purpose of DQL is to provide access to the data stored in a database and structure queries in a way to deliver intelligent and useful information to apply to specific application problems.

</details>
<details><summary>Implementation</summary> 
<br>

The DQL sublanguage has a simple one dimensional purpose: query data. However, this can be done in very complex ways depending on:

- Desired projection
- Relationships
- Filtered records
- Grouping
- Aggregation details

## Phrasing

A basic SQL query can be divided into clauses that describe different parts of the query.

```SQL
SELECT <projection> FROM <table_name> <filter> <grouping> <ordering> <offset>
```

According to official documentation, this is how a query can be structured.

```SQL
SELECT [ALL | DISTINCT]
    select_expr [, select_expr] ...
    [into_option]
    [FROM table_ref]
    [WHERE where_condition]
    [GROUP BY {col_name | expr | position}]
    [HAVING having_condition]
    [ORDER BY {col_name | expr | position}]
        [ASC | DESC]
    [LIMIT {[offset,] row_count | row_count OFFSET offset}];
```

That is a lot of information, but as an important note, most of those clauses are optional. Let's query the following simple table:

```SQL
CREATE TABLE my_table (
	id INT PRIMARY KEY,
    my VARCHAR(10) NOT NULL,
    my_other_value FLOAT DEFAULT 10.0
);
```

After creating the table, we can run the following query:

```SQL
SELECT * FROM my_table;
```



| id | my_value  | my_other_value |
|----|-----------|----------------|
|  1 | where val |              1 |
|  2 | new value |              2 |



As you can see the `SELECT` statement can be very simple.

Let's go over some more advanced usages of a `SELECT` statement.

### Projection

The `projection` clause of a `SELECT` statement is the set of columns(or aliases) that are returned from the statement. The `projection` is declared in the `select_expr` clause which comes after the `SELECT` command. In the previous example, the wildcard `*` projection was used. It is best practice to NOT use the wildcard projection, but to enumerate each column(or alias) you would like to use in the query. Let's update the previous `SELECT` statement.

```SQL
SELECT my_value, my_other_value FROM my_table;
```



| my_value  | my_other_value |
|-----------|----------------|
| where val |              1 |
| new value |              2 |



Observe that the new `SELECT` statement returns only the enumerated columns and excludes the `id` column.

Columns in the `projection` can also have aliases assigned to them. Let's use an alias for out columns in the `projection`.

```SQL
SELECT my_value as value, my_other_value as other FROM my_table;
```



| value     | other |
|-----------|-------|
| where val |     1 |
| new value |     2 |



Observe that the column names in the `projection` have been replaced by their aliases. Aliases are often used for simple reusability in complex `SELECT` statements especially when related tables used in joins have columns with the same names.

### Filtering

The `filtering` clause of a `SELECT` statement is a `WHERE` clause that defines how selected rows are filtered from the table. `WHERE` clause use logical operators to select records that meet specific conditions.

#### Where Logical operators

| Operator | Meaning                                                  |
| -------- | -------------------------------------------------------- |
| AND      | true if both boolean expressions evaluate to true        |
| IN       | true if the operand is included in a list of expressions |
| NOT      | Reverses the value of any boolean expression             |
| OR       | true if either or both boolean expressions is true       |
| LIKE    | true if the operand matches a pattern                    |
| BETWEEN  | true if the operand falls within a range                 |

To demonstrate some the use of these `filter` operators, let's use the following code:

```SQL
CREATE schema fruits_and_veggies;
USE fruits_and_veggies;
CREATE TABLE IF NOT EXISTS produce ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20) NOT NULL UNIQUE, price DECIMAL(3,2), type VARCHAR(10) NOT NULL);
INSERT INTO produce (name, price, type) VALUES ('navel orange', 1.99, 'citrus'), 
('mandarin orange', 0.75, 'citrus'), 
('tangerine', 0.50, 'citrus'), 
('red delicious', 2.00, 'apple'),
 ('jona gold', 2.50, 'apple'), 
 ('granny smith', 1.00, 'apple'), 
 ('blueberry', 0.40, 'berry'), 
 ('raspberry', 0.35, 'berry'), 
 ('kiwi', 0.75, 'berry'), 
 ('watermelon', 3.99, 'melon'), 
 ('cantaloupe', 2.99, 'melon'), 
 ('honeydew', 2.00, 'melon'), 
 ('lettuce', 2.99, 'leafy'), 
 ('spinach', 1.99, 'leafy'),
  ('pumpkin', 4.99, 'marrow'), 
  ('cucumber', 0.99, 'marrow'), 
  ('potato', 0.45, 'root'), 
  ('yam', 0.25, 'root'),
   ('sweet potato', 0.50, 'root'), 
   ('onion', 0.33, 'allium'),
    ('garlic', 0.25, 'allium'), 
    ('shallot', 0.60, 'allium');
```
 Before we start let's look at all of the records in the `produce` table.

```sql
SELECT id, name, price, type FROM produce;
```


| id | name            | price | type   |
|----|-----------------|-------|--------|
|  1 | navel orange    |  1.99 | citrus |
|  2 | mandarin orange |  0.75 | citrus |
|  3 | tangerine       |  0.50 | citrus |
|  4 | red delicious   |  2.00 | apple  |
|  5 | jona gold       |  2.50 | apple  |
|  6 | granny smith    |  1.00 | apple  |
|  7 | blueberry       |  0.40 | berry  |
|  8 | raspberry       |  0.35 | berry  |
|  9 | kiwi            |  0.75 | berry  |
| 10 | watermelon      |  3.99 | melon  |
| 11 | cantaloupe      |  2.99 | melon  |
| 12 | honeydew        |  2.00 | melon  |
| 13 | lettuce         |  2.99 | leafy  |
| 14 | spinach         |  1.99 | leafy  |
| 15 | pumpkin         |  4.99 | marrow |
| 16 | cucumber        |  0.99 | marrow |
| 17 | potato          |  0.45 | root   |
| 18 | yam             |  0.25 | root   |
| 19 | sweet potato    |  0.50 | root   |
| 20 | onion           |  0.33 | allium |
| 21 | garlic          |  0.25 | allium |
| 22 | shallot         |  0.60 | allium |


### And

The `AND` operator compares 2 boolean expressions. Both sets of expressions must eval to true for the whole statement to be true.

| Expression                            | Value |
| ------------------------------------- | ----- |
| TRUE AND TRUE                         | TRUE  |
| TRUE AND FALSE                        | FALSE |
| FALSE AND TRUE                        | FALSE |
| FALSE AND FALSE                       | FALSE |
| (TRUE AND TRUE) AND (TRUE AND TRUE)   | TRUE  |
| (TRUE AND TRUE) AND (FALSE AND FALSE) | FALSE |

Select all records that have a type equal to 'apple' and price greater than 1.00;

```sql
SELECT name, price, type FROM produce WHERE type='apple' AND price>1.00;
```


| name          | price | type  |
|---------------|-------|-------|
| red delicious |  2.00 | apple |
| jona gold     |  2.50 | apple |


### In

The `IN` operator compares an operand to a list and evaluates to true if the operand is in the list.

| Expression                      | Value |
| ------------------------------- | ----- |
| 'cat' IN ('cat', 'dog', 'goat') | TRUE  |
| 1 IN (100, 25, 17, 10000)       | FALSE |

Select all produce that have the type 'apple', 'root', 'berry', or 'allium';

```sql
SELECT name, price, type FROM produce WHERE type IN ('apple', 'root', 'berry', 'allium');

```


| name          | price | type   |
|---------------|-------|--------|
| red delicious |  2.00 | apple  |
| jona gold     |  2.50 | apple  |
| granny smith  |  1.00 | apple  |
| blueberry     |  0.40 | berry  |
| raspberry     |  0.35 | berry  |
| kiwi          |  0.75 | berry  |
| potato        |  0.45 | root   |
| yam           |  0.25 | root   |
| sweet potato  |  0.50 | root   |
| onion         |  0.33 | allium |
| garlic        |  0.25 | allium |
| shallot       |  0.60 | allium |


### Not

The `NOT` operator reverses the boolean value.

| Expression | Value |
| ---------- | ----- |
| NOT FALSE  | TRUE  |
| NOT TRUE   | FALSE |

Select all produce that are not an 'apple' and not an 'allium'

```sql
SELECT name, price, type FROM produce WHERE NOT (type='apple') AND NOT (type='allium');
```


| name            | price | type   |
|-----------------|-------|--------|
| navel orange    |  1.99 | citrus |
| mandarin orange |  0.75 | citrus |
| tangerine       |  0.50 | citrus |
| blueberry       |  0.40 | berry  |
| raspberry       |  0.35 | berry  |
| kiwi            |  0.75 | berry  |
| watermelon      |  3.99 | melon  |
| cantaloupe      |  2.99 | melon  |
| honeydew        |  2.00 | melon  |
| lettuce         |  2.99 | leafy  |
| spinach         |  1.99 | leafy  |
| pumpkin         |  4.99 | marrow |
| cucumber        |  0.99 | marrow |
| potato          |  0.45 | root   |
| yam             |  0.25 | root   |
| sweet potato    |  0.50 | root   |


### Or

The `OR` operator compares 2 boolean expressions. Either one or both of the expressions must evaluate to true for the whole statement to be true.

| Expression     | Value |
| -------------- | ----- |
| TRUE OR TRUE   | TRUE  |
| TRUE OR FALSE  | TRUE  |
| FALSE OR TRUE  | TRUE  |
| FALSE OR FALSE | FALSE |

Select all produce with a type of 'citrus' or 'berry'.

```sql
SELECT name, price, type FROM produce WHERE type='citrus' OR type='berry';

```


| name            | price | type   |
|-----------------|-------|--------|
| navel orange    |  1.99 | citrus |
| mandarin orange |  0.75 | citrus |
| tangerine       |  0.50 | citrus |
| blueberry       |  0.40 | berry  |
| raspberry       |  0.35 | berry  |
| kiwi            |  0.75 | berry  |


### Like

The `LIKE` operator is used to match patterns. LIKE can be used for fuzzy logic where a given value either fully or partially matches a pattern. Patterns in SQL can be 0 or more characters and include 0 or more valid wildcard characters.

| Wildcard        | Use                                         |
| --------------- | ------------------------------------------- |
| % (percent)     | match any string of zero or more characters |
| \_ (underscore) | match any single character                  |

Select all produce with a type that starts with 'a'.

```sql
SELECT name, price, type FROM produce WHERE type LIKE 'a%';
```

| name          | price | type   |
|---------------|-------|--------|
| red delicious |  2.00 | apple  |
| jona gold     |  2.50 | apple  |
| granny smith  |  1.00 | apple  |
| onion         |  0.33 | allium |
| garlic        |  0.25 | allium |
| shallot       |  0.60 | allium |


Select all produce that have a type that is exactly 5 characters long.

```sql
SELECT name, price, type FROM produce WHERE type LIKE '_____';
```


| name          | price | type  |
|---------------|-------|-------|
| red delicious |  2.00 | apple |
| jona gold     |  2.50 | apple |
| granny smith  |  1.00 | apple |
| blueberry     |  0.40 | berry |
| raspberry     |  0.35 | berry |
| kiwi          |  0.75 | berry |
| watermelon    |  3.99 | melon |
| cantaloupe    |  2.99 | melon |
| honeydew      |  2.00 | melon |
| lettuce       |  2.99 | leafy |
| spinach       |  1.99 | leafy |


### Between

The `BETWEEN` operator match expression that fall in a range.

Select all produce with a price between 0.50 and 1.00.

```sql
SELECT name, price, type FROM produce WHERE price BETWEEN 0.50 and 1.00;
```


| name            | price | type   |
|-----------------|-------|--------|
| mandarin orange |  0.75 | citrus |
| tangerine       |  0.50 | citrus |
| granny smith    |  1.00 | apple  |
| kiwi            |  0.75 | berry  |
| cucumber        |  0.99 | marrow |
| sweet potato    |  0.50 | root   |
| shallot         |  0.60 | allium |


Select all produce that have name between 'o' and 'y'.

```sql
SELECT name, price, type FROM produce WHERE name BETWEEN 'o' AND 'y';
```


| name          | price | type   |
|---------------|-------|--------|
| onion         |  0.33 | allium |
| potato        |  0.45 | root   |
| pumpkin       |  4.99 | marrow |
| raspberry     |  0.35 | berry  |
| red delicious |  2.00 | apple  |
| shallot       |  0.60 | allium |
| spinach       |  1.99 | leafy  |
| sweet potato  |  0.50 | root   |
| tangerine     |  0.50 | citrus |
| watermelon    |  3.99 | melon  |


### Grouping Pt 1

The `group by` clause of the `SELECT` statement groups rows that have the same values into summary rows. `Group by` is often used with aggregate functions like `count`, `max`, `min`. **Note: Most databases require that the group by clause contain all projected columns. This may affect the results of the query**

Select the types and avg price of each type of produce.

```sql
SELECT type, AVG(price) FROM produce GROUP BY type;
```

| type   | AVG(price) |
|--------|------------|
| citrus |   1.080000 |
| apple  |   1.833333 |
| berry  |   0.500000 |
| melon  |   2.993333 |
| leafy  |   2.490000 |
| marrow |   2.990000 |
| root   |   0.400000 |
| allium |   0.393333 |


### Grouping Pt. 2

The `HAVING` clause is used to filter out groups that meet a condition.

Select the types of produce that have an avg cost higher than the average all all produce.

```sql
SELECT type, AVG(price) AS group_avg, (SELECT AVG(price) FROM produce) AS gross_avg FROM produce GROUP BY type HAVING AVG(price) > gross_avg;
```


| type   | group_avg | gross_avg |
|--------|-----------|-----------|
| apple  |  1.833333 |  1.480000 |
| melon  |  2.993333 |  1.480000 |
| leafy  |  2.490000 |  1.480000 |
| marrow |  2.990000 |  1.480000 |


### Ordering

The `ORDER BY` clause is used to sort the returned records by a specified column. The records can be ordered either `ASC` (ascending) or `DESC` (descending). Ascending order is default if not specified.

Select all produce ordered alphabetically ascending.

```sql
SELECT name, price, type FROM produce ORDER BY name ASC;

```


| name            | price | type   |
|-----------------|-------|--------|
| blueberry       |  0.40 | berry  |
| cantaloupe      |  2.99 | melon  |
| cucumber        |  0.99 | marrow |
| garlic          |  0.25 | allium |
| granny smith    |  1.00 | apple  |
| honeydew        |  2.00 | melon  |
| jona gold       |  2.50 | apple  |
| kiwi            |  0.75 | berry  |
| lettuce         |  2.99 | leafy  |
| mandarin orange |  0.75 | citrus |
| navel orange    |  1.99 | citrus |
| onion           |  0.33 | allium |
| potato          |  0.45 | root   |
| pumpkin         |  4.99 | marrow |
| raspberry       |  0.35 | berry  |
| red delicious   |  2.00 | apple  |
| shallot         |  0.60 | allium |
| spinach         |  1.99 | leafy  |
| sweet potato    |  0.50 | root   |
| tangerine       |  0.50 | citrus |
| watermelon      |  3.99 | melon  |
| yam             |  0.25 | root   |


Do the same, but in reverse.

```sql
SELECT name, price, type FROM produce ORDER BY name DESC;
```


| name            | price | type   |
|-----------------|-------|--------|
| yam             |  0.25 | root   |
| watermelon      |  3.99 | melon  |
| tangerine       |  0.50 | citrus |
| sweet potato    |  0.50 | root   |
| spinach         |  1.99 | leafy  |
| shallot         |  0.60 | allium |
| red delicious   |  2.00 | apple  |
| raspberry       |  0.35 | berry  |
| pumpkin         |  4.99 | marrow |
| potato          |  0.45 | root   |
| onion           |  0.33 | allium |
| navel orange    |  1.99 | citrus |
| mandarin orange |  0.75 | citrus |
| lettuce         |  2.99 | leafy  |
| kiwi            |  0.75 | berry  |
| jona gold       |  2.50 | apple  |
| honeydew        |  2.00 | melon  |
| granny smith    |  1.00 | apple  |
| garlic          |  0.25 | allium |
| cucumber        |  0.99 | marrow |
| cantaloupe      |  2.99 | melon  |
| blueberry       |  0.40 | berry  |


### Offset Pt. 1

The `LIMIT` clause restricts number of records returned from the `SELECT` statement.

Select the first 5 produce records after ordering alphabetically.

```sql
SELECT name, price, type FROM produce ORDER BY name ASC LIMIT 5;
```


| name         | price | type   |
|--------------|-------|--------|
| blueberry    |  0.40 | berry  |
| cantaloupe   |  2.99 | melon  |
| cucumber     |  0.99 | marrow |
| garlic       |  0.25 | allium |
| granny smith |  1.00 | apple  |


### Offset Pt. 2

The `OFFSET` clause specifies from which record position to start counting from. This is often used in conjunction with the `LIMIT` clause. **NOTE: Some SQL implementations use the `SKIP` keyword instead of `OFFSET`**

Given the array [1,2,3,4,5,6,7,8,9,10], the following are facts in context of `LIMIT` and `OFFSET`

| Clause           | Fact                   |
| ---------------- | ---------------------- |
|                  | [1,2,3,4,5,6,7,8,9,10] |
| OFFSET 0         | [1,2,3,4,5,6,7,8,9,10] |
| LIMIT 5 OFFSET 0 | [1,2,3,4,5]            |
| OFFSET 2         | [3,4,5,6,7,8,9,10]     |
| LIMIT 5 OFFSET 2 | [3,4,5,6,7]            |

Select the second 5 produce records after ordering alphabetically.

```sql
SELECT name, price, type FROM produce ORDER BY name ASC LIMIT 5 OFFSET 5;
```


| name            | price | type   |
|-----------------|-------|--------|
| honeydew        |  2.00 | melon  |
| jona gold       |  2.50 | apple  |
| kiwi            |  0.75 | berry  |
| lettuce         |  2.99 | leafy  |
| mandarin orange |  0.75 | citrus |



</details>
<details><summary>Summary</summary> 

The SQL DQL sublanguage is the backbone for querying a database for data. The command set is simple consisting of the single `SELECT` command. However, The sublangage is built on a grammar structure that is used to...

- Search data
- Project record views
- Filter records
- Group values
- Offset resultsets

The `SELECT` statement, at the core of the Data Query Language (DQL) sublanguage, consists of clauses that dictate the selection of records from the database.

| Phrase  | Clause 1                   | Clause 2                |
| ------- | -------------------------- | ----------------------- |
| Search  | ... FROM table_ref         |                         |
| Project | SELECT col_1 [, col_2] ... |                         |
| Filter  | WHERE where_condition      |                         |
| Group   | Group By group_list        | Having having_condition |
| Offset  | Limit count                | Offset count            |
</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
