
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:


- To define and implement `DEFAULT`

</details>
<details><summary>Description</summary>
<br>

- The `DEFAULT` constraint is made use of to set a default value for a column.
- The `DEFAULT` value will be added to all new records, if no other value is specified.
- The `DEFAULT` values are typically literal constants, there's an important exception for timestamp and datetime columns. Many database systems allow the use of functions like now(), CURRENT_TIMESTAMP, or similar to set the default value to the current time for these specific column types. This is a commonly used feature and an exception to the general 'literal constant' rule.
- Use `ALTER TABLE table_name  ALTER COLUMN col_name SET DEFAULT` to create a `DEFAULT` constraint to an existing column of a table.
- Use `ALTER TABLE table_name ALTER COLUMN col_name DROP DEFAULT` to delete a `DEFAULT` constraint from an existing column of a table.

</details>
<details><summary>Real World Application</summary>
<br>

`DEFAULT` keyword in SQL can include scenarios where you want to ensure that a certain column always has a value, even if it's not explicitly provided during data insertion. This can be useful for maintaining data consistency and handling cases where certain information may be missing but can be assumed or assigned a default value.
For example, you might use `DEFAULT` for timestamp columns to automatically record when a record was created if no specific timestamp is provided.

Some examples of when you may want to use `DEFAULT` include:

* **Timestamps for Record Creation**: prefill data with current data and time that the record was created. 
* **Boolean Values**: Is the user subscribed to receive notifications.
* **Numeric Defaults**: prefill values with a 0 until otherwise modified. This could be useful in a database that stores user orders. All orders start at 0 until items are added to the cart and purchased.
* **Categorization or Status**: All orders set to pending until being processed.
* **Default Text Values**: Notes column in a database may be set to not have ‘no notes’ as a default value until modified. 

These examples demonstrate how `DEFAULT` can be used to handle cases where certain values are expected to be common or assumed if not explicitly provided. It helps maintain data integrity and simplifies data insertion by providing reasonable default values.
</details>
<details><summary>Implementation</summary> 
<br>

It's important to refer to the documentation of the specific database system you are using, as the syntax and supported data types for DEFAULT can vary between database management systems
```sql
CREATE TABLE UserOnline (
    ID INT PRIMARY KEY,
    UserName VARCHAR(25),
    Online BOOLEAN DEFAULT false
);
```

```sql
-- Inserting a user with online status not specified (defaults to false)
INSERT INTO UserOnline (ID, UserName) VALUES (1, 'LemonadeStandBoss');
```

```sql
-- Inserting a user with online status explicitly set to true
INSERT INTO UserOnline (ID, UserName, Online) VALUES (2, 'CodeLikeABoss', true);
```

In this example, the first user record inserted `(“LemonadeStandBoss”)` would have a value of `‘false’` for the column `‘Online’`, since no value was provided. Note that some SQL dialects may use the keyword `DEFAULT` as well within the insert statement.
</details>
<details><summary>Summary</summary> 
<br>

- `DEFAULT` constraints set default values for columns.
- Use `DEFAULT default_value` to set a default constraint to a column.
- Use `ALTER TABLE table_name  ALTER COLUMN col_name SET DEFAULT` to create a `DEFAULT` constraint to a an existing column of a table.
- Use `ALTER TABLE table_name ALTER COLUMN col_name DROP DEFAULT` to delete a `DEFAULT` constraint from an existing column of a table.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
