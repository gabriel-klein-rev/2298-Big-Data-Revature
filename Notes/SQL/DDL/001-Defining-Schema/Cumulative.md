
<details><summary>Learning Objectives</summary>

<br>

After completing this module, associates should be able to:

- Define what a Schema is
- Explain advantages of the schema
- Understand all components within a schema

</details>
<details><summary>Description</summary>
<br>

A database schema is the collection of database objects and elements that are logically connected through tables, stored procedures, views, triggers, functions and more. The schema defines how the table relationships should be built and organized within a particular database. 

Note: Regarding MySQL, "schema" and "database" are synonymous. For other RDBMSs, multiple schemas are allowed in a database and each schema allows the ability to grant specific access and permissions to users.

## Advantages

- Allow several users per schema
- Multiple Schemas
- Move database objects between schema
- Manage Database objects in a logical group




</details>
<details><summary>Real World Application</summary>
<br>

When a business is working with a relational database, it leverages schemas to manage all of its information, especially related to sales of product. The business has tables of relational data stored inside the schema for all of their products and related sales. Along with this they have stored procedures, views and functions associated with this sales information for repeated queries to generate for repeated analysis such as quarterly reports to deliver to the company, sales reports for specific items, profit margins, etc.
</details>
<details><summary>Implementation</summary> 
<br>

When working with SQL you use the keyword `CREATE` to generate a schema, along with all the other components utilized by the schema.

- Generate a new schema in SQL

```sql
CREATE SCHEMA employment;
GO
```

- Generate a table inside a specific schema

```sql
CREATE TABLE employment.employees(
    employee_id INT PRIMARY  KEY IDENTITY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50)
);
```

- Generate a view inside of a specific schema

```sql
CREATE VIEW employment.employees AS
SELECT first_name, last_name
FROM employment.employees
WHERE department = 'HR';
```
</details>
<details><summary>Summary</summary> 
<br>

A database schema is the collection of database objects and elements, such as tables, stored procedures, views, triggers, functions and more, that are logically connected to one another. 
- The schema defines how the table relationships should be built and organized within a particular database. 
- Multiple schemas are allowed in a database and each schema allows the ability to grant specific access and permissions to users.
- We can move database objects between schema
- Manage Database objects in a logical group
</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
