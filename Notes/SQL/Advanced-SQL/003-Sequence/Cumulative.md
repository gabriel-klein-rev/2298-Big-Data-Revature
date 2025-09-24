
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:
- Describe the use of sequence in a database
- Create a sequence

</details>
<details><summary>Description</summary>
<br>

A database sequence is an object in a relational database management system (RDBMS) that generates a sequence of numeric values according to a specified pattern. Sequences are often used to generate unique identifiers for primary keys in database tables, especially when the primary keys need to be generated independently of the data being inserted into the table.

Popular database systems, such as Oracle, PostgreSQL, and SQL Server, support sequences as a built-in feature. Note that each database system may have its own syntax and options for creating and using sequences.


</details>
<details><summary>Real World Application</summary>
<br>

Real world applications include:

- creating primary keys for database tables
- Priority based ticket booking
- Sequence of students waiting to receive their awards


</details>
<details><summary>Implementation</summary> 

## Syntax to create a sequence

In PostgreSQL:
```SQL
CREATE SEQUENCE sequence_name
    [ INCREMENT BY increment ]
    [ START WITH start ]
    [ MAXVALUE max_value | NO MAXVALUE ]
    [ MINVALUE min_value | NO MINVALUE ]
    [ CYCLE | NO CYCLE ];

```

- sequence_name: Name of the sequence.
- START WITH: Starting value from where the sequence starts. 
- INCREMENT BY: Value by which sequence will increment itself. Increment_value can be positive or negative.
- MAXVALUE: Maximum value of the sequence.
- MINVALUE: Minimum value of the sequence.
- CYCLE: When sequence reaches its set_limit it starts from beginning.
- NOCYCLE: An exception will be thrown if the sequence exceeds its max_value.


Example 1:
```SQL
CREATE SEQUENCE example_1
AS INT
START WITH 10
INCREMENT BY 10; 
```

Example 2:
```SQL
CREATE SEQUENCE example_2
start with 100
increment by -1
minvalue 1
maxvalue 100
cycle;
```
</details>
<details><summary>Summary</summary> 
<br>

- A sequence is a list of integers produced in an ascending order. 
- Each database system may have its own syntax and options for creating and using sequences.


</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
