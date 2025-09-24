
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- To define and implement `CHECK`

</details>
<details><summary>Description</summary>
<br>

- The `CHECK` constraint is used to limit the range value that can be placed in a column.
- It determines whether the value associated with the column is valid or not with the given criteria.
- It helps to check what type of values are to be stored in a table's column.

</details>
<details><summary>Real World Application</summary>
<br>

The `CHECK` constraint in SQL is used to enforce specific conditions on the data that is being inserted or updated in a table. The `CHECK` constraint ensures that values in a column meet certain criteria, and it helps maintain data integrity by preventing the insertion of incorrect or inappropriate data.

* **Data Validation**: Developers use CHECK to validate the values that can be inserted into a column. 

For example, you might want to ensure that a column only contains negative numbers or that a string column only accepts values with a certain length.

* **Date and Time Constraints**: Developers often use CHECK to enforce date and time constraints. For instance, ensuring that a date falls within a certain range.

* **Enum-like Values**: If a column is supposed to store values from a predefined set, you can use CHECK to restrict the allowed values.

An aquarium database may use the `CHECK` constraint to ensure that the tank size and temperature values for your fish tank are within acceptable ranges. A small example of this is below. 

 **Table 1**: FishTank

 ```sql
 CREATE TABLE FishTank (
    FishID INT PRIMARY KEY,
    Species VARCHAR(50),
-- Ensure tank size is positive and not too large
    TankSize DECIMAL CHECK (TankSize > 0 AND TankSize <= 100), 
-- Ensure temperature is within a reasonable range
    Temperature DECIMAL CHECK (Temperature >= 0 AND Temperature <= 30)
);  
```

In this example, the `TankSize` `CHECK` constraint `(TankSize > 0 AND TankSize <= 100)` ensures that the value is not only within the specified range but is also greater than 0, effectively enforcing that `TankSize` must be a positive number.

</details>
<details><summary>Implementation</summary>  
 <br>

An example table for the syntax is as follows. Please note that certain column names and attributes in this example would need to be modified depending on what you are trying to accomplish in your table. 

```sql
CREATE TABLE products (
    productID INT PRIMARY KEY,
    productPrice DECIMAL CHECK (productPrice > 0)
);
```

This particular example is checking that the `NumericColumn` contains values greater than 0. 



</details>
<details><summary>Summary</summary> 
<br>

- `CHECK` constraint is declared during table creation. 
- It is used to protect the integrity of the table as similar to other constraint.
- It helps us to get only those values that are valid for the condition and our requirements.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
