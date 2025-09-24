
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- Define a constraint
- Describe the different SQL constraints

</details>
<details><summary>Description</summary>
<br>

SQL constraints are used to help validate data beyond just a simple data type. Below is a set of commonly used SQL constraints.

| Constraint   | Use                                                                       |
| ------------ | ------------------------------------------------------------------------- |
| Not Null     | Ensures that a column's value is not null.                                |
| Unique       | Ensures that a column's value is unique in the table.                     |
| Primary Key  | Combines `unique` and `not null`. Uniquely identifies each row.           |
| Foreign Key  | Links to a row in another table. Prevents the destruction of those links. |
| Default      | Specifies a value for a column, if one is not given.                      |
| Check        | Ensures the value of a column satisfies a specific condition.             |


Each column of a table can use a combination of these constraints, but some are mutually exclusive in some vendors or context. For instance:

* Although it is possible to establish both `NOT NULL` and `DEFAULT` constraints for a column, this is superfluous since the `DEFAULT` constraint will be used if a value is not given when the record is inserted. This makes the `NOT NULL` constraint functionally useless. 
* `DEFAULT` with a `CHECK` constraint might lead to conflicting requirements. 
* Since a `FOREIGN KEY` constraint establishes a relationship between two tables based on the values of a column in both tables, using a `CHECK` constraint to enforce similar conditions is redundant. 
* Lastly, a `PRIMARY KEY` constraint implies that a column (or a set of columns) is both `UNIQUE` and `NOT NULL` . Therefore, explicitly adding a `UNIQUE` constraint to the same column is redundant.

Constraints are used to define a database schema and are the backbone for defining `integrity constraints` of the schema. `Integrity constraints` are rules or conditions defined on a database schema to maintain the accuracy, consistency, and reliability of data within a database.
`Integrity constraints` collectively help maintain the quality and reliability of data in a database, preventing errors, inconsistencies, and ensuring that data remains meaningful for the applications and users interacting with the database. They play a crucial role in upholding the integrity of the data model and supporting data accuracy and reliability. 


</details>
<details><summary>Real World Application</summary>
<br>

Constraints are tied directly to the table and define the integrity of the data as part of the schema. Administrators use constraints to apply database level validation according to application and database requirements.

Table 1: Vendor

```sql
CREATE TABLE Vendor(
 vendorId  CHAR(2) NOT NULL,
 vendorName VARCHAR(25) UNIQUE NOT NULL,
 PRIMARY KEY (vendorId)
); 
```


This table demonstrated the `NOT NULL`, `PRIMARY KEY`, and `UNIQUE` constraints

Table 2: SalesTransaction

```sql
CREATE TABLE SalesTransaction(
 transId VARCHAR(8) PRIMARY KEY,
 customerId CHAR(7) NOT NULL REFERENCES Customer(customerId),
 storeId INT NOT NULL REFERENCES Store(StoreId),
-- Using DEFAULT to default to the current date cannot be null because a default value will be given
 transDate DATE DEFAULT now()
);
```

The above table demonstrated the use of `PRIMARY KEY`, `NOT NULL`, `FORIEGN KEY`, and `DEFAULT` constraints.
</details>
<details><summary>Implementation</summary> 
<br>

Adding constraints to a column can be done when the table is being created or afterward if the requirements should change. Specific disscussion on the command associated with creating or altering tables is out of the scope of this document, but will discussed in the appropriate section.

```SQL
-- adding constraints during creation
create table <table_name> (
    <col_name> datatype constraint1 constraint2,
    constraint <constraint_name> <constraint_type>(constraint_option, ...)
)
```

```SQL
-- adding constraints after creation
alter table <table_name> add constraint <constraint_name> <constraint_type>(constraint_option, ...)
```

<hr/>

## Exercises (Optional)

Discuss how to model a table for a rideshare application. The table will be called "scheduled_pickups". As the name suggests, the table should manage riders who have scheduled rides immediately and in the future.

</details>
<details><summary>Summary</summary> 
<br>

Constraints help define the integrity constraints of the database schema. Common constraints include:

* Primary key
* Foreign Key
* Not Null
* Unique
* Default
* Check


</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
