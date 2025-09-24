
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:
* To define and implement `AUTO INCREMENT` or `SERIAL` 

</details>
<details><summary>Description</summary>
<br>

* `AUTO INCREMENT` allows a unique number to be generated automatically when a new row is inserted into a table.
* `SERIAL`  is used to create an auto-incrementing integer column.
* Most often, `AUTO INCREMENT` or `SERIAL` acts as a primary key field that we would like to be created automatically every time a new record is inserted.
* Depending on the dialect of SQL you are using will determine if you use the `AUTO INCREMENT` keyword or `SERIAL` keyword. 
    * The syntax for auto-incrementing columns varies among SQL dialects, with differences in implementation. While the concepts are the same, different database systems may use distinct keywords or mechanisms for achieving similar functionality. It is important to refer to the documentation of the specific database system you are working with to understand the correct syntax for auto-incrementing columns.
      * **PostgreSQL** - `SERIAL` implicitly creates a sequence to generate unique values.
      * **MySQL** - `AUTO_INCREMENT` automatically increments the value for each new row.
      * **SQLite** - `AUTOINCREMENT` ensures that each new row inserted into the table will automatically receive a unique and incrementing value.

</details>
<details><summary>Real World Application</summary>
<br>

Consider a table where we want to keep track of users. Users should not have the same identifier so as a new user is added to the database we would want to auto-increment their id. 

Table: Users

```sql
CREATE TABLE users (
 user_id SERIAL PRIMARY KEY,
 first_name VARCHAR(30),
 last_name VARCHAR(30),
 address VARCHAR(30),
 city VARCHAR(30),
 state VARCHAR(2),
 zip VARCHAR(5),
 social_number VARCHAR(11),
 username VARCHAR(30),
 password TEXT,
 email VARCHAR(50)
);
```

</details>
<details><summary>Implementation</summary> 
<br>

Syntax to create a table with employee_id as an attribute which will `AUTO_INCREMENT` on inserting new record.

``` sql
CREATE TABLE table_name(
variable_name variable_datatype AUTO_INCREMENT
);
```

Example:

``` sql
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT
);
```

This same table written using `SERIAL` would look as follows:

```sql
CREATE TABLE table_name (
    variable_name SERIAL PRIMARY KEY,
    -- Other columns...
);
```

Example:

```sql
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT
);
```

Notice the syntactical differences between the two table queries. This example is why it is important to always refer to documentation when working with different dialects of SQL. 

You can modify auto incremented values, however, it is highly discouraged as the value is automatically managed by the system and should represent a unique identifier for each row. 


</details>
<details><summary>Summary</summary> 
<br>

* In some cases, you may not have any unique identifying characteristics in data; therefore, it makes sense to create a Primary Key.
* Explicitly initializing and modifying the `AUTO-INCREMENT` or `SERIAL` value is possible at any time though highly discouraged.
* Record identifiers can be created that are unique to each record.
* Automatic incrementing allows flexibility in handling gaps between rows.
* Different database systems may use distinct keywords or mechanisms for achieving similar functionality. It is important to refer to the documentation.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
