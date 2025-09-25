# Week 2 Day 4 Notes

### Constraints
Constraint - A rule in schema that defines some limitation about the data. For instance: UNIQUE which tells the database engine that no data can be inserted or modified in this column if it would break the UNIQUE rule, that there can only be one of each value in that column.
 - PRIMARY KEY - Sets the primary index on the table and gurantees that every row can be uniquely identified. Implies INDEXED, UNIQUE, & NOT NULL
 - FOREIGN KEY - Sets a reference and enforces referential integrity. 
 - UNIQUE - Every value in the column must be unique.
 - NOT NULL - The column cannot hold `null` values.
 - DEFAULT - Sets a default value, if a `null` value would be inserted, replace it with the default instead. Works well with NOT NULL, but doesn't work with UNIQUE

### Nested Queries

### Distinct
Distinct - SQL keyword used in a query to only select one of each value from a column, if more of the same values are encountered, they are not included in the seleciotn.

### Delete, Drop, & Truncate
 - Delete - DML - Remove data from a table one row at a time with the potential to filter using WHERE clause.
 - Drop - DDL - Drops the whole table, which necessarioly ejects all data in that table.
 - Truncate - DDL(?!) - This apparently counts as DDL because of the way it ejects data.


### Alter Table

### Group By 

### Having



### Functions
Function - Take some input, perform some operation, and produce some output

Scalar Functions - one input value, one output value.
 - LCASE()
 - UCASE()
 - MID()
 - LEN()
 - ROUND()


Aggregate Functions - many input values, exactly one output value
 - SUM()
 - AVG()
 - MEDIAN()
 - COUNT()
 - MIN()
 - MAX()

What about NOW()? GeeksforGeeks says this is a scalar function. I suppose we can think of aggregate functions as taking in ONE OR MORE inputs, and producing exactly one output. With NOW() taking in no inputs, we're left with scalar. It's really not important, Kyle just thought this was interesting.


