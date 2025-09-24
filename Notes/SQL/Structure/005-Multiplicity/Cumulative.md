
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:
- To define and implement `MULTIPLICITY`

</details>
<details><summary>Description</summary>
<br>

### Multiplicity vs Cardinality
Although these two terms are often used interchangeably, technically they are different. Generally, you can think of __multiplicity__ as the _possible range_ of associations between one entity and another. __Cardinality__ represents a _specific number_ of associations. For example, let's say we have an application to manage apartment buildings and we want to model two entities, a Person and a Pet. We want to have a constraint of each person having at most 2 pets. In ER Diagrams, the multiplicity could be seen as 0..2 or a range of 0 to 2 associations between Person and Pet. The cardinalities defined are 0 and 2. If there is no upper limit then we can use an asterisk (\*) rather than a number. For example, the multiplicity for the relationship between a social media influencer and their followers could be 0...*. 


We often look at multiplicity in simpler terms by just referring to a type of relationship entities can have with one another. 
- These relationships are:
     - **one to one relationship**
        - Definition: In a one-to-one relationship, each record in one table is associated with only one record in another table, and vice versa.
        - Example: A person might have only one passport, and each passport belongs to only one person.
        - Implementation: A one-to-one relationship can be implemented by adding a unique foreign key in one of the tables that references the primary key of the other table. Alternatively, both tables can share the same primary key.
    - **one to many relationship**
        - This is described from the perspective of the "one" side.
        - Definition: In a one-to-many relationship, a single record in the "one" table can be associated with multiple records in the "many" table.
        - Example: A single author can have multiple books. Here, "author" is the "one" side, and "books" are the "many" side.
        - Implementation: The "many" table (books) includes a foreign key that references the primary key in the "one" table (author).
    - **many to one relationship**
        - This is described from the perspective of the "many" side.
        - Definition: In a many-to-one relationship, multiple records in the "many" table can be associated with a single record in the "one" table.
        - Example: Many employees can belong to a single department. Here, "employees" are the "many" side, and "department" is the "one" side.
        - Implementation: The "many" table (employees) includes a foreign key that references the primary key in the "one" table (department).
    - **many to many relationship**
        - Definition: In a many-to-many relationship, multiple records in one table can be associated with multiple records in another table.
        - Example: A student can enroll in multiple courses, and each course can have multiple students enrolled in it.
        - Implementation: This type of relationship requires a junction table (also called a bridge or join table) that holds foreign keys referencing the primary keys of the two tables involved. For example, a student_courses table might store references to both student_id and course_id to track which students are in which courses.

**NOTE**: the difference between a one-to-many relationship and a many-to-one is strictly perspective. They are actually the same.
</details>
<details><summary>Real World Application</summary>

<br>

A real-world example of multiplicity can be seen in the relationship between entities within a school. Let's consider a simplified scenario where we have the different entities: School, Student, Course, Student ID Card. The different types of relationships are:


- One School to Many Students:
    - A school can have many students enrolled in it, but each student is associated with only one school.

- Many Courses to Many Students:
    - Many courses can have many students enrolled in them, and each student can be enrolled in many courses.

- One Student ID Card to One Student:
    - Each student has exactly one Student ID card, and each ID card can only be associated with one student.


</details>
<details><summary>Implementation</summary> 

## One to Many Relationship

A good example of a one to many relationship could be an `albums` and `songs` table. 1 album can have many songs however 1 song cannot be on many albums (excluding "Greatest Hits" albums). This is a one-to-many relationship. As stated in the previous section, to implement a one-to-many relationship we need to have a foreign key in the "many" table that references the "one" table. In our case, the many is the `songs` table and the one is the `albums` table. 


***albums table***

|album_id | album_name | 
| ------- | ---------- |
| 1 | 'Thriller' |
| 2 | 'Abbey Road'|

***songs table***

|song_id |song_name |album_fk |
| ------ | -------- | ------- |
| 1 | 'Billie Jean' | 1 |
| 2 | 'Beat it' | 1 | 
| 3 | 'Come Together' | 2 |

## Many to One Relationship

The only difference between a one-to-many relationship and a many-to-one relationship is perspective. People generally refer to a relationship as a many-to-one because they are thinking in relation to the "many" table. However, many-to-one and One-to-many are actually the same thing. Please refer to the one-to-many example on how to implement this.

## Many to Many Relationship

One example of a many-to-many relationship could be `doctors` table and a `patients` table. 1 doctor can have many patients and 1 patient can have many doctors. Since the relationship goes both ways, this is a many-to-many relationship. We achieve a many-to-many relationship utilizing a third table called a junction table (as shown below).

***doctors table***

|doctor_id | doctor_name | 
| ------- | ---------- |
| 1 | 'Dr. Smith' |
| 2 | 'Dr. Adams'|
| 3 | 'Dr. Keen'|

***patients table***

|patient_id | patient_name | 
| ------- | ---------- |
| 1 | 'Abbey Jones' |
| 2 | 'Jane Stevens'|
| 3 | 'Devin Kennedy'|

***doctors_patients table (this is the junction table)***

|doctor_id_fk | patient_id_fk | 
| ------- | ---------- |
| 1 | 1 |
| 1 | 2 | 
| 3 | 2 | 
| 2 | 1 | 
| 2 | 2 | 




## One to One Relationship

For a one-to-one relationship, let's have a table for `students` as well as `backpacks`. A student posesses one backpack and alternatively a backpack only belongs to one student. Let's see how these tables would look like below. 

***students table***

|student_id | student_name | 
| ------- | ---------- |
| 1 | 'Mike Jones' |
| 2 | 'Steven Nguyen'|
| 3 | 'Jane Jackson' |

***backpacks table***

|backpack_id | book_count| student_id_fk |
| ------ | -------- | -------- |
| 1 | 3 | 2 |
| 2 | 3 | 3 |
| 3 | 3 | 1 | 

The example above looks very similar to a one-to-many relationship. This is because it is! The only difference in the implementation of a one-to-one relationship and a one-to-many relationship is that in a one-to-one relationship, a `UNIQUE` constraint needs to be added on the foreign key.


</details>
<details><summary>Summary</summary> 
<br>

- `Multiplicity` defines the relationship between two tables
- There are 4 different multiplicity relationships


</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
