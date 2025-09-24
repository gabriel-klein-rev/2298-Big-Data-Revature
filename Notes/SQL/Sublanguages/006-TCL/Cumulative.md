
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:
- Define TCL
- Define and implement TCL commands

</details>
<details><summary>Description</summary>
<br>

An SQL transaction is a sequence of one or more SQL operations (such as queries, inserts, updates, or deletes) that are treated as a single unit of work. Transactions are managed using Transaction Control Language (TCL) commands.
 
# Commands

1. `START TRANSACTION / BEGIN`: Starts a new transaction.

2. `COMMIT`: 
This command is used to save the data permanently. 
Whenever we perform any of the DML command like `INSERT`, `DELETE` or `UPDATE`, these can be rolled back if the data is not stored permanently. So in order to be at the safer side `COMMIT` command is used. 
 
3. `ROLLBACK`: 
This command is used to get the data or restore the data to the last savepoint or last committed state. If due to some reasons the data inserted, deleted or updated is not correct, you can rollback the data to a particular savepoint or if savepoint is not done, then to the last committed state. 

4. `SAVEPOINT`: 
This command is used to save the data at a particular point temporarily, so that whenever needed can be rolled back to that particular point. 



</details>
<details><summary>Real World Application</summary>
<br>

Here's why TCL is important:

- __Data Integrity__: TCL commands like `COMMIT`, `ROLLBACK`, and `SAVEPOINT` are essential for ensuring data integrity in database transactions. They allow you to control when changes made within a transaction are permanently saved (committed) or discarded (rolled back), thus maintaining the consistency and reliability of the database.
- __ACID Properties__: TCL plays a key role in enforcing the ACID (Atomicity, Consistency, Isolation, Durability) properties of transactions. By providing mechanisms to start, commit, or rollback transactions, TCL ensures that database operations are atomic (either all succeed or none), consistent (maintains database integrity), isolated (transactions do not interfere with each other), and durable (committed changes are permanent).
- __Error Handling__: TCL provides mechanisms for error handling and recovery in database transactions. In case of errors or exceptions during transaction execution, TCL allows you to rollback the transaction to a previous consistent state using `ROLLBACK`, ensuring that no incomplete or erroneous changes are persisted in the database.

Overall, TCL is essential for maintaining data integrity, enforcing transactional properties, and handling errors in relational database systems. 

</details>
<details><summary>Implementation</summary> 
<br>

Consider an example of a transaction where you tried to add a new bank account ACC3 and set the funds to 10000. In that same transaction, you tried to create another account, ACC4, and set its funds to 900000 when it was supposed to be 9000. If the entire transaction is rolled back, the step of creating ACC3 with 10000 initial funds would also be rolled back. To avoid this, a save point can be added soon after creating ACC3 and we can roll back to before the statement of that creates account ACC4.

``` sql
START TRANSACTION;
INSERT INTO bankaccounts VALUES("ACC3", 10000);
SAVEPOINT sv;
INSERT INTO bankaccounts VALUES("ACC4", 900000);
ROLLBACK TO sv;
INSERT INTO bankaccounts VALUES("ACC4", 90000);
COMMIT;
```

</details>
<details><summary>Summary</summary> 
<br>

- TCL stands for Transaction Control Language.
- A single unit of work in a database is formed after the consecutive execution of commands is known as a transaction.
- TCL commands help the user manage the transactions that take place in a database.
- `COMMIT`, `ROLLBACK` and `SAVEPOINT` are the most commonly used TCL commands in SQL.


</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
