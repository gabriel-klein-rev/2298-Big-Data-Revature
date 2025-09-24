
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- Identify and describe the use of data and databases

</details>
<details><summary>Description</summary>

## What is data

Data is information with a purpose. In enterprise applications, data provides aggregated state information for the application. Businesses will use this data for various reasons including, marketing, usage statistics, error reporting, and more. Data is specifically designed to provide insights and persistence information for the applications which they support.

## What is a database

A database is a system of software and capabilites that make validating, storing, searching, filtering, aggregating, grouping, and administering data possible. In enterprise applications databases fall into 2 main categories `SQL` and `NoSQL`.

### SQL databases

SQL databases are a type of RDBMS which use the standard Structured Query Language to administer the data. Data in a SQL database are stored in objects called tables. Tables provide the relational information for the data stored in the database.

### NoSQL databases

NoSQL (Not Only SQL) databases are not necessarily based on the relational model, unlike RDBMS. NoSQL databases typically use some other means or DSL (domain-specific language) for administering data and use different structures for storing data and relational information.

</details>
<details><summary>Real World Application</summary>

<br>

From the start of digital revolution, we have witnessed the utmost requirement of storing data effectively and efficiently. Data is the lifeblood of business solutions and having an accurate database management system is an important tool for handling such large volumes of data.

Each database management system offers particular solutions as per business requirements, and decision-makers are often left wondering which system would be appropriate for their use. We will cover various RDBMS vendors in another module to help understand these differences.

</details>
<details><summary>Implementation</summary> 
<br>

The general syntax for creating a `DATABASE` in MySQL is:

``` sql
CREATE DATABASE database_name;
```
Example:

``` sql
CREATE DATABASE employee;
```

The general syntax to use a newly created schema:

``` sql
USE database_name;
```

Example:

``` sql
USE employee;
```


</details>
<details><summary>Summary</summary> 
<br>

- Data is information with a purpose. In enterprise applications, data provides aggregated state information for the application. 
- A database is a system of software and capabilites that make validating, storing, searching, filtering, aggregating, grouping, and administering data possible.
- SQL databases are a type of RDBMS which use the standard Structured Query Language to administer the data.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
