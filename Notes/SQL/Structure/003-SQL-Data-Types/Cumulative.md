
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- Identify the categories of common SQL datatypes
- List SQL data types

</details>
<details><summary>Description</summary>
<br>

In a database, each `table` is defined with a set of `columns`. Each `column` must have a data type which restricts the type of data that can be assigned to it. Each vendor can support any number of the data types. Below is a list of the most common types broken into categories.

| Category  | Sub 1        | Sub 2           | Sub 3          |
| --------- | ------------ | --------------- | -------------- |
| Character | Fixed-length | Variable-length | --             |
| Numeric   | Decimal      | Integer         | Floating point |
| Temporal  | Date         | Time            | Timestamp      |


## Character

Character types can represent character data as either `fixed` or `variable`-length character types like 'a' or 'cat' or a social media post.

### Fixed-length character types

Fixed length character types store a fixed number of bytes in storage regardless of the string or number of characters being stored. The fix length types can be declared as `char(n)` or `character(n)` (depends on the database) and each character will take up 1 byte.

```SQL
middle_initial character(1);
```

or

```SQL
middle_initial character;
```

The above column `middle_initial` will be 1 byte in storage regardless if the column actually has a value or not. Remaining characters are padded with spaces.

```SQL
pet_type char(10);
```

The column `pet_type` will always take up 10 bytes regardless if the column is empty or contains 'dog', 'feline', 'lizard', 'fish', or whatever. For instance if the value of `pet_type` is 'dog' the actual value stored in the database is, 3 bytes for 'd', 'o', 'g' + 7 bytes for the remaining spaces.

### Variable-length character types

Variable length character types store a variable number of bytes in storage with a minimum of 2 bytes for storing the length of the string. Variable length types can be declared as `character varying(n)` or `varchar(n)`

```SQL
first_name varchar(20);
```

Although the column `first_name` is declared with a 20 byte length, the actual length can range from 2-20 bytes. **Remember the last 2 bytes are reserved for storing the length.** If the column `first_name` contains the value 'John' the actual size in storage is 6 bytes. 4 bytes are used for the characters 'J', 'o', 'h', 'n' and 2 bytes are used for the length.

## Numeric

Numeric types store type of numbers either whole or fractional. The minimum and maximum of the different numeric types will depend on the SQL implementation. The different type of numeric types are.

- bit(n)
- bit varying(n)
- integer
- smallint
- bigint
- real(s)
- float(p,s)
- double precision(p,s)
- decimal(p,s)

### Decimal

Decimal types are used to store exact fractional number values like money.

```SQL
annual_income decimal(10,2);
```

The `decimal` data types `decimal`, `float`, `double` have a syntax that includes `type(p,s)`. In the syntax 'p' is the precision that represents the number of significant digits, 's' is the scale that represents the number of digits after the decimal point. In the example of above `annual_income` will have a maximum of 10 digits with 8 before the decimal and 2 after it, with a max value of `99,999,999.99`

### Integer

Integer data types store signed and unsigned whole numbers.

```SQL
age int;
```

### Floating point

Floating point types store approximate fractional number values. The precision and scale of floating point numbers are variable length.

```SQL
avg_temp float(10);
```

## Temporal

Temporal types store data related to dates and times.

### Date

The date type represents a date value with 3 parts year, month, and day. The range for date types is typically `0001-01-01` to `9999-12-31`. Dates are also typically stored in the format `YYYY-MM-DD`.

```SQL
dob date;
```

### Time

The time type represents data related to time of day in hours, minutes, and seconds. The time type has the format `HH:MM:SS`.

```SQL
received_at time;
```

### Timestamp

The timestamp type represents data related to a date and time. Timestamps have the format `YYYY-MM-DD HH:MM:SS`. This format has a space between the date and time sections.

```SQL
created_at timestamp;
```

On top of these very common data types, a database vendor can add any number of other data types to the implementation. Some vendors add spatial types, boolean types, json types, large object types, and more.


</details>
<details><summary>Real World Application</summary>
<br>

Understanding SQL data types is important for several reasons:

- __Data Integrity__: Knowing the appropriate data types ensures data integrity by enforcing constraints and preventing invalid data from being stored in the database. For example, using the VARCHAR data type for storing strings ensures that the data length is within the specified limit, preventing data truncation.

- __Storage Efficiency__: Choosing the correct data types helps optimize storage space in the database. Using data types with appropriate sizes reduces the amount of disk space required to store data. For example, using the INT data type for storing integer values requires less storage space compared to using VARCHAR for the same purpose.

- __Application Compatibility__: Knowledge of SQL data types ensures compatibility between the database schema and application code. Application developers need to understand the data types used in the database to correctly map database columns to application variables and parameters.

In summary, knowing about SQL data types is essential for maintaining data integrity, optimizing storage and performance, and ensuring application compatibility.

</details>
<details><summary>Implementation</summary> 
<br>

Here's an example SQL `CREATE TABLE` statement that demonstrates the use of various common data types:

```SQL

CREATE TABLE Employee (
    EmployeeID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender CHAR(1),
    DateOfBirth DATE,
    Salary DECIMAL(10, 2),
    IsManager BOOLEAN,
    DepartmentID INT,
    JoinDate TIMESTAMP
);

```

Let's explain the columns in this example:

- EmployeeID: INT data type is used for storing integer values.
- FirstName and LastName: VARCHAR data type is used for storing variable-length character strings.
- Gender: CHAR data type is used for storing single-character values.
- DateOfBirth: DATE data type is used for storing date values.
- Salary: DECIMAL data type is used for storing fixed-point numbers with precision and scale.
- IsManager: BOOLEAN data type is used for storing boolean values (true or false).
- DepartmentID: INT data type is used for storing integer values.
- JoinDate: TIMESTAMP data type is used for storing date and time values.
</details>
<details><summary>Summary</summary> 
<br>

Data types enforce the expected types of values inserted into a table. SQL provides a standard list of data types which can be categorized into 3 main categories, each with its own subcategories.

- Character types
  - Fixed-length
  - Variable-length
- Numeric types
  - Decimal
  - Integer
  - Floating point
- Temporal types
  - Date
  - Time
  - Timestamp

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
