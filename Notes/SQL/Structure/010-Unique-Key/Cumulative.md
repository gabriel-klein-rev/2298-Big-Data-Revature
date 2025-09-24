
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- To define and implement `UNIQUE KEY`

</details>
<details><summary>Description</summary>
<br>

* The `UNIQUE` constraint is used to ensure every value of a column is different. This means that each row must have a distinct value in the specified column.

* The `UNIQUE` key interacts with NULL values somewhat, unintuitively, so let’s dive deeper into this.

    A `UNIQUE` key allows for `NULL` column values for records.

    There is often confusion around how many `NULL` values a `UNIQUE` constraint can have in a column. Each database may have slight differences in the amount of `NULL` values that are allowed with a `UNIQUE` constraint. Some database systems only allow a single `NULL` value; however, databases often allow multiple `NULL` values.

    In other words, when a column is declared as `UNIQUE` and allows `NULL`, the `UNIQUE` constraint applies only to the non-null values. Rows with `NULL` values in that column are not considered duplicates in terms of the `UNIQUE` constraint. This is because `NULL` is actually the absence of a value. However, keep in mind that each non-null value must still be unique across all rows.

    It's essential to consult the documentation of the specific database system you are using to understand its behavior regarding `UNIQUE` constraints and `NULL` values. Always consider the unique constraints enforced by your database to ensure the correct behavior based on your requirements. 

    Keep in mind that a column can have multiple constraints applied to it. To ensure that there is only a single NULL value, you can use the UNIQUE constraint alongside the NOT NULL constraint in your DDL statements.

    
</details>
<details><summary>Real World Application</summary>
<br>

* **Primary Keys**: The primary key of a table is often enforced using a `UNIQUE` constraint. This ensures that each record in the table has a unique identifier, helping maintain data integrity and providing a reliable way to reference and link records from other tables.
* **Email Addresses and Usernames**: In user management systems, it's common to enforce `UNIQUE` constraints on email addresses or usernames to ensure that each user has a distinct identifier. This helps prevent duplicate accounts and ensures a unique mapping between users and their login credentials.
* **Product Codes or SKUs**: In inventory or e-commerce systems, product codes or Stock Keeping Units (SKUs) are often assigned as unique identifiers. Applying a `UNIQUE` constraint to these columns helps avoid confusion and ensures that each product is uniquely identified in the system.
* **Identification Numbers**: Various entities, such as social security numbers, employee IDs, or customer IDs, are typically required to be unique. Enforcing a `UNIQUE` constraint on these columns helps prevent errors and ensures the uniqueness of each identifier.
* **Reference Codes in Relationships**: Establishing relationships between tables, it's common to use `UNIQUE` constraints on columns that serve as foreign keys. This ensures that the relationship is well-defined and that each reference corresponds to a unique record in the referenced table.
* **Phone Numbers (if used as identifiers)**: In certain applications, phone numbers may serve as unique identifiers. Enforcing a `UNIQUE` constraint on phone number columns helps avoid confusion and ensures that each phone number corresponds to a single entity.
* **URLs or Website Addresses**: In web-related applications, URLs or website addresses may be used as unique identifiers. Enforcing a `UNIQUE` constraint on these columns ensures that each web address is associated with a unique resource.
* **License Plate Numbers**: In systems that track vehicles or manage parking, license plate numbers are often used as unique identifiers. Applying a `UNIQUE` constraint ensures that each vehicle is uniquely identified.

These are just a few examples and uses of why developers would use the `UNIQUE` constraint. Each of these cases, the `UNIQUE` constraint helps maintain data integrity and ensures that the data in the database accurately represents the real-world entities it is modeling. It prevents duplicate or conflicting information, which is crucial for reliable and effective database management.

</details>
<details><summary>Implementation</summary> 
<br>

```sql
-- Create a table with a UNIQUE constraint allowing NULL values
CREATE TABLE students (
    studentId INT UNIQUE,
    firstName VARCHAR(255),
    lastName VARCHAR(255)
);

-- Insert rows with unique non-null values and multiple NULL values
-- This is valid, as NULL values are not considered duplicates for the UNIQUE constraint
INSERT INTO students (studentId, firstName, lastName) VALUES
    (1, 'Jane', 'Smith'),
    (2, 'Suzanne', 'Brown'),
    (NULL, 'Abdul', 'Singh'),
    (NULL, 'Soria', 'Waler');

```

In the example above, we can see the use of the `UNIQUE` constraint, as well as columns that lack this constraint. Notice that we have two students who do not have a student ID, represented by Null values. 
This may represent that their student account profiles are pending some information, so we have not generated a student ID for them, or perhaps these students moved and no longer have an active student Id, although we still keep records of them in our database.

The first and last name columns may or may not contain duplicate values so it is possible to have matching values for both first and last name (two students named “John Doe” for instance).
</details>
<details><summary>Summary</summary> 
<br>

- The `UNIQUE` constraint ensure that all values in a column are different and unique.
- The `UNIQUE` as well as `PRIMARY KEY` constraints provide a guarantee for uniqueness for a column or set of columns.
- A `PRIMARY KEY` constraint automatically has a `UNIQUE` constraint.
- We can have many `UNIQUE` constraints per table, but only one `PRIMARY KEY` constraint per table.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
