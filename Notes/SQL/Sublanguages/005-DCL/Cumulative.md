
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:
- Describe the DCL sublanguage
- Identify the command set of DCL
- Execute DCL statements on a RDBMS

</details>
<details><summary>Description</summary>
<br>

The Data Control Language of SQL is used to control rights, and permissions of users on database objects.

## Commands

- `GRANT`
- `REVOKE`

### Grant

The `GRANT` command is used to give users access privileges to the database or specific objects

### Revoke

The `REVOKE` command removes users' access privileges to the database or specific objects.

</details>
<details><summary>Real World Application</summary>
<br>

The DCL sublanguage is used to control acces to databases and objects. In large scale applications, databases could be providing data to numerous applications. In practice, each one of those applications would represent a distinct user. Each one of those applications could possibly have a different set of access privileges to the different databases on the server and different objects in the databases.

In general, these privileges are granted before the database is accessed by the user, so the DBA would be responsible to setup user access prior to the user attempting to login to the database.

</details>
<details><summary>Implementation</summary> 
<br>

The DCL sublanguage provides a means of defining access control to a database and its objects. Privileges can be granted or revoked on users.

## Privileges

A database can have numerous privileges which can be permitted to users. Below is a summary of more common privileges.

| Privilege | Description                        |
| --------- | ---------------------------------- |
| `SELECT`    | allows `SELECT` statements on tables |
| `INSERT`    | allows `INSERT` statements on tables |
| `DELETE`    | allows `DELETE` statements on tables |
| `UPDATE`    | allows `UPDATE` statements on tables |
| `INDEX`    | allows creating indexes on tables  |
| `CREATE`    | allows `CREATE` table statements     |
| `ALTER`     | allows `ALTER` table statements      |
| `DROP`     | allows `DROP` table statements       |
| `ALL`       | allow all permissions except `GRANT` |
| `GRANT`     | allows `GRANT` statements            |

## GRANT

The `GRANT` command is used to add permissions to a user. To `GRANT` permissions, the user executing the statement must have the `GRANT` permission.

```sql
GRANT PRIVILEGES ON object TO user;
```

To `GRANT` a simple privilege like `SELECT` on a table named 'posts' to a user named 'john.user'.

```sql
GRANT SELECT ON posts TO 'john.user';
```

To `GRANT` all of the CRUD abilities on a table named 'posts' to a user named 'community.manager'.

```sql
GRANT SELECT,  INSERT, UPDATE, DELETE ON posts TO 'community.manager';
```

## Revoke

The `REVOKE` command is used to remove permissions from a user.

```sql
REVOKE PRIVILEGES ON object FROM user;
```

To revoke the `SELECT` privilege on the 'posts' table from 'john.user'

```sql
REVOKE SELECT ON posts FROM 'john.user';
```

To remove the CRUD privileges on 'posts' from 'community.manager'.

```sql
revoke SELECT, INSERT, UPDATE, DELETE ON posts FROM 'community.manager';
```


</details>
<details><summary>Summary</summary> 
<br>

- The DCL sublanguage is used to `GRANT` or `REVOKE` access privileges to databases and database objects.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
