
<details><summary>Learning Objectives</summary>

<br>

After completing this module, associates should be able to:
- Define SQL Sublanguages
- Describe the purpose of using SQL Sublanguages


</details>
<details><summary>Description</summary>
<br>

Structured Query Language or SQL is the standard language for working with RDBMS systems. SQL is used to administer and manipulate SQL servers. SQL is a scripting language that is interpreted by the database server. SQL is used to:

- Define database structure
- Manipulate stored data
- Define data access permissions
- Control concurrent data access
- Query stored data

To accommodate the operations of the above categories, SQL is broken into 5 sublanguages.

| Sublanguage | Description                                                                 |
| ----------- | --------------------------------------------------------------------------- |
| DDL         | Data Definition Language. Defines the data structure                            |
| DML         | Data Manipulation Language. Insert, Update, Delete record                   |
| DCL         | Data Control Language. Grant or revoke access permissons to database object |
| TCL         | Transaction Control Language. Defines boundaries for concurrent operations.        |
| DQL         | Data Query Language. Search, filter, group, aggregate stored data           |

Each sublanguage is responsible for a specific set of operations and have a specific set of commands associated with them. Further details on each sublanguage will be discussed in their respective sections.


</details>
<details><summary>Real World Application</summary>
<br>

Consider a scenario where we have to use all 5 SQL sublanguages commands, so we have to be familiar with all the commands in each of DDL, DML, DCL, and DQL and we should be able to use them in our project development.
The commands are:

- DDL
    - CREATE
    - ALTER
    - DROP
    - TRUNCATE
    - RENAME

- DML
    - INSERT
    - UPDATE
    - DELETE

- DQL
    - SELECT

- DCL
    - GRANT
    - REVOKE

Some TCL commands include COMMIT, ROLLBACK, SAVEPOINT.


</details>
<details><summary>Implementation</summary> 
<br>

The DDL sublanguage of SQL is utilized to create and manage the structure of a database. DDL consists of the commands `CREATE`, `DROP`, `ALTER`, `TRUNCATE`, and `RENAME`. Using DDL the overall structure is modeled by creating objects like tables where the specific columns, data types, constraints, and relationships are defined.

The DML sublanguage of SQL is utilized to create, update, and delete data in a database. DML consist of the `INSERT`, `UPDATE`, and `DELETE` commands. Using DML, the records in database are manipulated to reflect to overall state of the applications that utilize the database for persistence.

The SQL DQL sublanguage is the backbone for querying a database for data. The command set consists of the single `SELECT` command. However, the sublangage is built on a grammar structure that is used to:

- Search data
- Project record views
- Filter records
- Group values
- Offset resultsets

The `SELECT` statement is the crux of the DQL sublanguage and is composed of clauses that determine how records are selected from the database.

| Phrase  | Clause 1                   | Clause 2                |
| ------- | -------------------------- | ----------------------- |
| Search  | ... FROM table_ref         |                         |
| Project | SELECT col_1 [, col_2] ... |                         |
| Filter  | WHERE where_condition      |                         |
| Group   | Group By group_list        | Having having_condition |
| Offset  | Limit count                | Offset count            |


The DCL sublanguage is used to `GRANT` or `REVOKE` access privileges to databases and database objects.

</details>
<details><summary>Summary</summary> 
<br>

Structured Query Language is the language used to administer SQL-based RDBM systems. SQL is based on ANSI standard `ISO/IEC 9075:2016 (ANSI X3.135)`. There are many vendor specific implementations of the SQL standard, but the standard itself can be divided into 5 sublanguage categories: `DDL`, `DML`, `DCL`, `TCL`, `DQL`. Each sublanguage is responsible for a specific set of operations on the database.


</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
