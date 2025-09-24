
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:
- Describe the purpose of stored procedure in a database
- Describe how to Create or Alter a Stored Procedure

</details>

<details><summary>Description</summary>
<br>

A stored procedure is similar to functions in other programming languages, in which a set of statements are named and stored to executed at a future point in time as a batch. These stored procedures are stored inside a database schema and which can be invoked from within an SQL command call. A stored procedure can provide additional layers of security between the user interface and the database by abstracting data access because end users may manipulate data through procedure calls without exposing embedded queries in a graphical user interface. Additionally, stored procedures can be used to provide easier interface for complex or batch operations to be executed on database records.

Unlike user defined functions, stored procedures typically do not return data (although some SQL dialects may support this operation). Rather, procedures are used to perform many and/or complex operations or manipulate data in a batch. Additionally, stored procedures are not called through Queries (such as `SELECT`) and are instead called using a specific keyword, such as `CALL`, `EXEC`, or `EXECUTE PROCEDURE` the exact keyword(s) to use depend on the SQL dialect.

</details>

<details><summary>Real World Application</summary>
<br>

Real world applications include:

- Updating database records in a batch
- Providing interface for complex but frequently executed database operations
- Database Error handling or logging
- Performance optimization
- Transaction Management

</details>

<details><summary>Implementation</summary> 
<br>

Stored Procedures are created using the DML command `CREATE`. For the following examples, we are showcasing MySQL, but many SQL dialects support the creation of stored procedures. The exact syntax may vary from Language-to-Language.

## Syntax for creating a procedure

```sql
CREATE PROCEDURE procedure_name ( IN | OUT | INOUT parameter_name parameter_datatype, … )
BEGIN    
    -- SQL statements
END
```

Note: MySQL allows data to be returned from a Stored Procedure using the `OUT` or `INOUT` declaration for parameters. This functionality is not supported in all SQL dialects.

### Example

The following showcases how to create a procedure named UpdateEmployeeSalaries which will update the Salary column of all records in an Employees table based on a PercentageIncrease argument given.
```sql
DELIMITER //

CREATE PROCEDURE UpdateEmployeeSalaries(IN PercentageIncrease DECIMAL(5,2))
BEGIN
    -- Updating the salaries
    UPDATE Employees
    SET Salary = Salary * (1 + PercentageIncrease / 100);

    -- Logging the update
    INSERT INTO SalaryUpdateLog (UpdateDate, PercentageIncrease)
    VALUES (NOW(), PercentageIncrease);
END;

DELIMITER ;
```

Let’s break down this example in more detail:

* `DELIMITER //` is used to change the delimiter temporarily, so that semicolons within the procedure do not end the `CREATE PROCEDURE` statement prematurely.
* This procedure takes a single input parameter, PercentageIncreate which is a `DECIMAL` datatype. This decimal can include up to 5 digits and has a precision (numbers to the right of the decimal point) of two decimal places.
* `BEGIN` marks the start of the procedure statements and END marks the end of the procedure.
* The `UPDATE` statement sets the salary of all employees in the Employees table to a new value increased by the PercentageIncrease argument passed when calling this procedure.
* The `INSERT` statement records a log in a SalaryUpdateLog table which includes the date of the update and the argument given for the PercentageIncrease parameter.
* Finally, `DELIMITER` ; resets the delimiter back to the default, semicolon.

To call this procedure, using MySQL, you would use the keyword `CALL`.
```sql
CALL UpdateEmployeeSalaries(3.0)
```
## Syntax for deleting a procedure

DDL is also used to remove the procedure. As such, the DROP command can be used to remove a previously created stored procedure.

```sql
DROP PROCEDURE [IF EXISTS] stored_procedure_name;
```

Note: The brackets around `IF EXISTS` means that the operators are optional, and will check if the entity exists prior to completing the rest of the operation. In the example below you will see it used with and without:

To remove the UpdateEmployeeSalaries procedure, the syntax would look like this:
```sql
-- Remove the Procedure 'UpdateEmployeeSalaries' if it exists.
DROP PROCEDURE IF EXISTS UpdateEmployeeSalaries; 
```
alternatively:
```sql
-- Remove the Procedure 'UpdateEmployeeSalaries'. May throw an error is the procedure does not exist.
DROP PROCEDURE UpdateEmployeeSalaries;
```

</details>
<details><summary>Summary</summary> 
<br>

- A stored procedure is similar to functions in other programming languages, in which a set of statements are named and stored to executed at a future point in time as a batch
- Procedures are used to perform many and/or complex operations or manipulate data in a batch
- Unlike user defined functions, stored procedures typically do not return data (although some SQL dialects may support this operation)

</details>

<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>