
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- To define Normalization
- To define Normal forms 1NF, 2NF, 3NF and BCNF.

</details>
<details><summary>Description</summary>

## Normalization

Normalization is the process of efficiently organizing data in a database. The two main objectives of normalization are to eliminate redundant data (to make sure that the same data is not stored twice) and to ensure data dependencies make sense (to store only relational data in tables). Both of these are important because they reduce the amount of space of a database and ensure that data is logically stored.

## Normal Forms

First, second, and third normal forms are stepping stones to the Boyce-Codd normal form and, when appropriate, the higher normal forms.

### First Normal Form
The first normal form (1NF) is conclusive of a relational database. If we are to consider a database relational, then all relations in the database are in 1NF.

A database is considered relational if all the fields in the tables are atomic, every column is a unique attribute, and a unique identifier or primary key is used. It can also be described as the elimination of recurring groups of relations. 1NF doesn't allow hierarchies of data values.

### Second Normal Form
Second normal form (2NF) deals with the elimination of circular dependencies from a relation. We say a relation is in 2NF if it is in 1NF and if every non-key attribute is completely dependent only on the Primary Key.

A non-key attribute is any column that cannot be used to uniquely identify the table.

### Third Normal Form
Third normal form (3NF) deals with the elimination of non-key attributes that do not describe the Primary Key. For a relation to be in 3NF, the relationship between any two non-key attributes, or groups of non-key attributes, must not be in a one-to-one relation.

The attributes should be mutually independent which means, none of the attributes should be functionally dependent on any combination of attributes. This mutual independence makes sure that any update on the individual attribute will not affect other attributes in a row.

### Boyce-Codd Normal Form
Boyce-Codd Normal Form or BCNF is an extension to the third normal form, and is also known as 3.5 Normal Form.

A table should follow these two conditions to satisfy BCNF:
- It should be in the Third Normal Form.
- And, for any dependency A → B, A should be a super key. which means that A should be a key attribute if B is a key attribute.



</details>
<details><summary>Real World Application</summary>
<br>

Normalization is an essential concept in database design and plays a crucial role in ensuring the efficiency, integrity, and scalability of databases. Here are several key reasons why normalization is important:

- __Data Integrity__: Normalization reduces data redundancy and eliminates anomalies such as insertion, update, and deletion anomalies. By organizing data into well-structured tables and relationships, normalization helps maintain data integrity and consistency.

- __Query Performance__: Normalized databases typically have better query performance because they require fewer joins and provide efficient access paths to data. Well-designed normalized databases allow for faster query execution, resulting in improved application performance.

- __Ease of Maintenance__: Normalization makes databases easier to maintain and modify over time. It simplifies database schema changes, such as adding new tables or modifying existing ones, without causing disruptions to the application or compromising data integrity.

In summary, normalization is important because it promotes data integrity and efficiency and also ensures that databases are well-structured, optimized for performance, and capable of supporting evolving business requirements.
</details>
<details><summary>Implementation</summary> 
<br>

Let's demonstrate normalizing an unnormalized table. In our example, we have a `zookeepers` table. Zookeepers can be responsible for more than one exhibit, and each each exhibit can contain more than one animal for them to take care of, and each exhibit can be taken care of by more than one zookeeper.

## Unnormalized
``` sql
CREATE TABLE zookeepers(
	first_name varchar(100),
	last_name varchar(100),
	exhibit varchar(100),
	animal_type1 varchar(100),
	animal_type2 varchar(100),
	animal_type3 varchar(100),
	salary integer,
	position_title varchar(100)
);
```

This table is unnormalized because it does not have a primary key and some columns are redundant.

## 1NF

```sql

CREATE TABLE zookeepers(
	id integer auto_increment PRIMARY KEY,
	first_name varchar(100),
	last_name varchar(100),
	exhibit varchar(100),
	animal_type varchar(100),
	salary integer,
	position_title varchar(100)
);

```

To put the example in 1NF, we added a PK column as well as removed redundant columns. 

## 2NF

``` sql
CREATE TABLE zookeepers(
	id integer auto_increment PRIMARY KEY,
	first_name varchar(100),
	last_name varchar(100),
	salary integer,
	position_title varchar(100)
);

CREATE TABLE exhibits(
	id integer auto_increment PRIMARY KEY, 
	exhibit_name varchar(100)
);

CREATE TABLE animals(
	id integer auto_increment PRIMARY KEY, 
	species varchar(100),
	FOREIGN KEY (exhibit_id) REFERENCES exhibits(id) ON DELETE SET NULL
);

CREATE TABLE zookeepers_exhibits(
	zookeeper_id integer,
	exhibit_id integer,
	FOREIGN KEY (zookeeper_id) REFERENCES zookeepers(id) ON DELETE CASCADE,
	FOREIGN KEY (exhibit_id) REFERENCES exhibits(id) ON DELETE CASCADE,
	PRIMARY KEY (zookeeper_id, exhibit_id)
);
```
In order to move our table to 2NF, we needed to remove any columns that don't fully depend on or describe the key or zookeeper entity. Notice we moved exhibit and animal related columns out of the `zookeepers` table. Because there is a many to many relationship between zookeepers and exhibits, we have a bridge or join table that represents the pairings between the two entities. The `animals` table is created and contains a foreign key that references the exhibit table, since an animal would depend on / live within an exhibit.

## 3NF

```sql
CREATE TABLE zookeepers(
	id integer auto_increment primary key,
	first_name varchar(100),
	last_name varchar(100),
  	FOREIGN KEY (position_title_id) REFERENCES position_titles(id) ON DELETE SET NULL

);

CREATE TABLE position_titles(
	id integer auto_increment primary key,
	position_title_name varchar(100),
	salary integer
);

```
Lastly, we need to remove a transitive dependency so we can move our `zookeepers` table into 3NF. The two columns `salary` and `position_title` did describe the `zookeeper` entity, however if a change is made to the `position_title` column, for example if they are promoted to a `Level 2 Zookeeper` rather than a `Level 1 Zookeeper`, then a change should also be made to the `salary` column. This violates 3NF, so we would need to move these two columns into their own `position_title` table and have the `zookeepers` table depend on it instead.


</details>

<details><summary>Summary</summary> 

## Normalization

- Normalization is the process of organizing the data and the attributes of a database. it is performed to reduce the data redundancy.

## Normal Forms

- 1NF: A relation is in 1NF if all its attributes have an atomic value.

- 2NF: A relation is in 2NF if it is in 1NF and all non-key attributes are fully functionaly dependent on the candidate key.

- 3NF: A relation is in 3NF if it is in 2NF and there is no transitive dependency.

- BCNF: A relation is in BCNF if it is in 3NF and for every functional dependency, the left-hand side of the dependency is a super key.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
