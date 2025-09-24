
<details><summary>Learning Objectives</summary>

<br>

After completing this module, associates should be able to:
- Describe the DML sublanguage
- Identify the command set of DML
- Execute DML statements on a RDBMS

</details>
<details><summary>Description</summary>
<br>

Data Modification Language is the SQL language subset used for modifying data in the database.

In order to utilize the functions of the DML sublanguage, a database user must have the appropriate permissons on the server and on the particular parent object.

## Commands

- INSERT
- UPDATE
- DELETE

The `INSERT` command is used to add records to a database table.
The `UPDATE` command is used to modify existing data in a database table.
The `DELETE` command is used to remove data from a database table.

</details>
<details><summary>Real World Application</summary>
<br>

DML is used to manipulate the data that is being stored in the database. Often DML is used in enterprise application solutions that utilize bridging libraries like JDBC in Java or EF in .NET, but of course it is possible to use DML directly in a SQL IDE or console. In the real world, DBA could be responsible for adding data to bootstrap the database into a working state for the applications that will rely on the data.

Let's bootstrap the permissions and roles tables in the following IAM schema:
```SQL
CREATE DATABASE IF NOT EXISTS IAM;

USE IAM;

CREATE TABLE IF NOT EXISTS permission_categories (
	id bigint primary key,
    name varchar(30) not null unique,
    description text(255)
);

CREATE TABLE IF NOT EXISTS permissions (
	id bigint primary key,
    categoryId bigint not null,
    name varchar(30) not null unique,
    index(categoryId, name)
);

CREATE TABLE IF NOT EXISTS roles (
	id bigint primary key,
    name varchar(30) not null unique
);

CREATE TABLE IF NOT EXISTS roles_permissions(
	roleId bigint,
    permissionId bigint,
    primary key(roleId, permissionId)
);

CREATE TABLE  IF NOT EXISTS login_activities_lu (
	id bigint primary key,
    type varchar(10) not null unique
);

CREATE TABLE IF NOT EXISTS profiles (
	id bigint primary key,
    firstName varchar(30) not null,
    lastName varchar(40) not null,
    email varchar(100) not null unique
);

CREATE TABLE IF NOT EXISTS users (
	id bigint primary key,
    username varchar(20) not null unique,
    password varchar(20) not null,
    profileId bigint not null,
    isActive boolean default true,
    isLocked boolean default false
);

CREATE TABLE IF NOT EXISTS login_activities (
	id bigint primary key,
    userId bigint not null,
    activityId bigint not null,
    activityDate datetime default NOW()
);

CREATE TABLE IF NOT EXISTS users_roles (
	userId bigint not null,
    roleId bigint not null
);

ALTER TABLE permissions ADD CONSTRAINT fk_permissions_category_id FOREIGN KEY(categoryId) REFERENCES permission_categories(id);
ALTER TABLE roles_permissions ADD CONSTRAINT fk_permissions_role_id FOREIGN KEY(roleId) REFERENCES roles(id);
ALTER TABLE roles_permissions ADD CONSTRAINT fk_roles_permission_id FOREIGN KEY(permissionId) REFERENCES permissions(id);
ALTER TABLE users ADD CONSTRAINT fk_users_profile_id FOREIGN KEY(profileId) REFERENCES profiles(id);
ALTER TABLE login_activities ADD CONSTRAINT fk_login_user_id FOREIGN KEY(userId) REFERENCES users(id);
ALTER TABLE login_activities ADD CONSTRAINT fk_login_activity_id FOREIGN KEY(activityId) REFERENCES login_activities_lu(id);
ALTER TABLE users_roles ADD CONSTRAINT fk_ur_user_id FOREIGN KEY(userId) REFERENCES users(id);
ALTER TABLE users_roles ADD CONSTRAINT fk_ur_role_id FOREIGN KEY(roleId) REFERENCES roles(id);
```

We'll use DML's `INSERT INTO` commands to add information or data into our tables.

```SQL
INSERT INTO roles (id, name) values (1, 'ADMIN'), (2, 'OWNER'), (3, 'EDITOR'), (4, 'VIEWER');
INSERT INTO permission_categories (id, name, description) VALUES (1, 'HR', 'Permissions assigned to members of the HR team'),
	(2, 'Accounting', 'Permissions assigned to members of the accounting team'), (3, 'Technology', 'Permissions assigned to members of the technology team');
INSERT INTO permissions (id, categoryId, name) VALUES (1, 1, 'TIMESHEETS'), (2, 2, 'PAYROLL'), (3, 3, 'EVALUATION');
```

The actual amount of bootstrapping that could be done is dependent on the problem at hand, and of course IAM is a very large problem. The above could demonstrates the use of the insert statements of DML in the schema. Pay attention to the order some of the statements. For instance the `permissions` table has a relationship with `permission_catagories` so in order to insert the categoryId into the `permissions` table we must first insert it into the `permission_catagories` table.

Should the need arise to modify a record in the database, like re-assign the 'PAYROLL' permission from 'Accounting' to 'HR'.

```SQL
UPDATE permissions SET categoryId=1;
```

Or should the need arise to remove the 'VIEWER' role.

```SQL
DELETE FROM roles WHERE name='VIEWER';
```

</details>
<details><summary>Implementation</summary> 

## Insert

The `INSERT` command is used to store new records in a database table.

```SQL
INSERT INTO <table_name> (col1 [, col2, ...]) {VALUE | VALUES} (valuelist) [, (valuelist), ...]
```

The `INSERT` command to insert 1 or more records. Below is an example:

```SQL
INSERT INTO my_table (id, my_value, my_other_value) VALUES (1, 'some data', 1.0);
```

The results of the insert statement are the number of rows affected by the statement. The results should be:
![Single insert result](../../resources/single_insert_results.PNG)

Multiple records can be inserted using a single `INSERT` command.

```SQL
INSERT INTO my_table (id, my_value, my_other_value) VALUES (2, 'misc data', 2.0), (3, 'even data', 100.13);
```

![Multiple insert result](../../resources/multi_insert_result.PNG)

## Update

The `UPDATE` command is used to modify whole records or parts of records in a database table.

```SQL
UPDATE <table_name> SET assignment_list [WHERE where_list]
```

The `UPDATE` command can modify 0 or more records and the results of the command are the number of rows affected by the command.

```SQL
UPDATE my_table SET my_value='new value';
```

![Unfiltered update results](../../resources/unfil_update.PNG)
As you can see with the previous update statement all of the inserted rows were updated. This may or may not be your intended results.

To limit the number or rows that are updated, it is best practice to include the optional `WHERE` clause.

```SQL
UPDATE my_table SET my_value='where val' WHERE id=1;
```

![Filtered update results](../../resources/filtered_update.PNG)
Now the results of the update statement are restricted to the `WHERE` clause. Since there is only a single record with the id of 1, only that single record is updated.

## Delete

The `DELETE` command is used to remove data from a database table.

```SQL
DELETE FROM <table_name> [WHERE where_condition]
```

Much like the `UPDATE` command the `DELETE` command has an optional `WHERE` clause. However, the `DELETE` command can be very destructive, it is best practice to always have a `WHERE` clause on the statement. If you exclude a `WHERE` clause on the `DELETE` command the database will remove all records from the table.

```SQL
DELETE FROM my_table WHERE id=3;
```

The results of the `DELETE` command are the number of rows affected.
![Delete results](../../resources/delete_results.PNG)

<hr/>

## Exercise (Optional)

Using the library database and the books table from [DDL implementation](../001-DDL/Implementation.md)

- Insert 3 books into the `books` table.
- Insert a book titled, 'Learn SQL in a Snap', authored by 'Jim Dandy', published on 01-01-01
- Modify the author of the first book inserted into the database
- Delete the second and third books inserted into the database

</details>
<details><summary>Summary</summary> 
<br>

The DML sublanguage of SQL is utilized to create, update, and delete data in a database. DML consist of the `INSERT`, `UPDATE`, and `DELETE` commands, Using DML the records in database are manipulated to reflect to overall state of the applications that utilize the database for persistence.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
