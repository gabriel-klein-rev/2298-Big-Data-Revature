
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- Define the `CASCADE` keyword
- Implement examples of `CASCADE`
- Differentiate between a `CASCADE` with `DELETE` or `UPDATE`



</details>
<details><summary>Description</summary>
<br>

In SQL, `CASCADE` is a keyword used to simultaneous delete or update data from both the child and parent tables and is used in conjunction while writing the query with `ON DELETE` or `ON UPDATE`. Applying `CASCADE` keyword to the command applies the changes in both parent and child tables accordingly to the execution of that query. `CASCADE` is appended to the reference command for the foreign key when creating a table.

## ON DELETE

Appending `ON DELETE CASCADE` to the foreign keys within our child table allow us the opportunity to delete the parent record and subsequently delete all relational information in any referenced table through one command. Otherwise, due to referential integrity it would require multiple commands to delete all of the referenced records inside of the child tables first, before removing the parent record.

## ON UPDATE

Appending `ON UPDATE CASCADE` to the foreign key within our child table allows us to update information in a singular command by updating the parent table record will apply to all subsequent child tables information. This also helps reduce the amount of commands and keeps our referential integrity intact.
</details>
<details><summary>Real World Application</summary>
<br>

Imagine students enrolled in a courses at a college, but some students drop out mid-way through the semester and the school is not required to keep the records of students who drop out. In this example, we would want to structure our tables such that the foreign keys have an `ON DELETE CASCADE` to maintain referential integrity when removing that students records from the gradebooks of all courses they attended.

Keeping with the student examples, imagine the students in the database need their primary key id reset to adjust for the students that dropped out and make room for the freshman. Through this we need to update all the current records for each of these individuals to match accordingly in both the parent and child tables. When the foreign key is applied with `ON UPDATE CASCADE` it will make sure that every record's primary key association in the child tables is updated accordingly.
</details>
<details><summary>Implementation</summary> 
<br>

Sticking with the students in college theme let's look at students in a college course and use `CASCADE` to handle deletions and updates.

- Define the table for students

```sql
CREATE TABLE students(
    student_id INT PRIMARY KEY,
    student_name VARCHAR(40),
    email VARCHAR(20) UNIQUE
);
```

- Define the table for courses

```sql
CREATE TABLE courses(
    course_id INT PRIMARY KEY,
    course_name VARCHAR(20),
    course_length_weeks INT,
    credits INT
);
```

- Finally, lets define a junction table to handle enrollment and uses `CASCADE`
    - for the purposes of this example we will assume that courses never get updated

```sql
CREATE TABLE enrollments(
    course_id INT,
    student_id INT,
    grade INT,
    completion_status boolean,
    PRIMARY KEY(course_id, student_id),
    FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE CASCADE
    FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);
```

- The above command allows for the deletion of all referenced courses through a single command by removing the record from the courses table. Along with this, the command also accounts for any updates or deletion within the students table records.
</details>
<details><summary>Summary</summary> 
<br>

In SQL, `CASCADE` is a keyword used to simultaneous delete or update data from both the child and parent tables and is used in conjunction while writing the query with `ON DELETE` or `ON UPDATE`. 
- `ON DELETE CASCADE` allows us with one command to delete records in a parent table and all subsequent records in the child tables. 
- `ON UPDATE CASCADE` allows us with one command to update records in a parent table and all subsequent records in the child tables.  
</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
