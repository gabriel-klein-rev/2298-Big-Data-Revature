
<details><summary>Learning Objectives</summary>

<br>

After completing this module, associates should be able to:

- Define the `DELETE` command
- Differentiate from `TRUNCATE` and `DROP` from DDL
- Implementation for `DELETE` Commands
- Understand the risks invovled with `DELETE`

</details>
<details><summary>Description</summary>

<br>

`DELETE` is a keyword command in SQL used to remove a specific record from a table or relation. The `DELETE` command, generally, includes a `WHERE` clause to specify the records for deletion. However, much like the `UPDATE` command there is a risk that if the `WHERE` clause is not specified it will remove all records from the table. The `DELETE` command removes one record at a time and logs each deleted row, which is why it's not considered good practice to delete all records in a table using `DELETE` when you want to maintain the table structure. This is where `TRUNCATE` offers a better solution as it's both faster and removes the data by deallocating the data pages used to store the records. `DELETE` commands can also activate a trigger and work with indexed views.
</details>
<details><summary>Real World Application</summary>

<br>

Deleting records from a database is common when we need to remove unwanted data, such as looking at student records maintained at a college. When a student drops out from a course before the drop deadline, all grades and assessments from that course are deleted from the records as they no longer impact the student's GPA or show as a registered course. So they would include a few `DELETE` commands to both remove the student from the course, along with commands to remove any records or assessments associated with the course and that student.
</details>
<details><summary>Implementation</summary> 

<br>


- Basic Syntax for `DELETE` command

```sql
DELETE FROM TABLE_NAME
WHERE [condition];
```

- Example to `DELETE` Student, student_id = 'student1@uni.edu' from an enrollment table for course_id = 101

```sql
DELETE FROM enrollment
WHERE student_id = 'student1@uni.edu' AND course_id = 101;
```

- Example of `DELETE` all the above student's grades from a student_assessments table

```sql
DELETE FROM student_assessments
WHERE student_id = 'student1@uni.edu';
```
</details>
<details><summary>Summary</summary> 

<br>

`DELETE` is a keyword command in SQL used to remove a specific record from a table or relation. The `DELETE` command, generally, includes a `WHERE` clause to specify the records for deletion. 
- However, much like the `UPDATE` command there is a risk that if the `WHERE` clause is not specified it will remove all records from the table. 
- The `DELETE` command removes one record at a time and logs each deleted row.
    - This why it's not considered good practice to delete all records in a table using `DELETE` when you want to maintain the table structure. 
    - `TRUNCATE` offers a better solution for deleting all records from a table as it's both faster and removes the data by deallocating the data pages used to store the records. 
- `DELETE` commands can also activate a trigger and work with indexed views.
</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
