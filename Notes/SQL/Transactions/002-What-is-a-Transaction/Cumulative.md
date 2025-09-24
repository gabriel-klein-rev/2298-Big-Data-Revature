
<details><summary>Learning Objectives</summary>

<br>

After completing this module, associates should be able to:
- To define and create transactions
- To understand transaction commands

</details>
<details><summary>Description</summary>
<br>

SQL transactions are a fundamental concept in database management systems (DBMS) that allow you to group multiple SQL operations into a single, atomic unit of work. Transactions ensure the integrity, consistency, and reliability of database operations, especially in multi-user and concurrent environments. Transactions are typically managed using Transaction Control Language (TCL) commands.

## Commands

- `BEGIN` or `START TRANSACTION`: Starts a new transaction.

- `COMMIT`: Commits/saves the changes of a successful transaction.

- `SAVEPOINT`: Sets a point within a transaction to which you can later rollback if needed, without rolling back the entire transaction.

- `ROLLBACK`: Used to undo the changes done by the transaction.



</details>
<details><summary>Real World Application</summary>
<br>

An example for a transaction would be a funds transfer from one bank account to the other. Let's say that you want to debit $100 from Account A and credit that $100 to another account, Account B. If these two updates are not grouped together and only one of the statements is executed, i.e. the amount is debited from Account A but not credited into Account B, then where does the $100 go? To avoid situations like this, both updates should be grouped into a single transaction.

</details>
<details><summary>Implementation</summary> 

## SQL Transactions 

Consider an example where there’s a `bankaccounts` table and we are doing an intra-bank transfer, i.e. person holding account `ACC1` is trying to transfer $100 to account  `ACC2`.

Step 1: Create Table `bankaccount` with columns `account_no` and `funds`.
``` sql
CREATE TABLE bankaccounts(
    account_no varchar(20) PRIMARY KEY NOT NULL,
    funds decimal(8,2)
);
```

Step 2: Add two accounts named `ACC1` and `ACC2` with an initial fund balance of $1000 each.
``` sql
INSERT INTO bankaccounts VALUES("ACC1", 1000);
INSERT INTO bankaccounts VALUES("ACC2", 1000);
```

Step 3: Now, let’s see the transaction of transfering 100$ from `ACC1` to `ACC2`.
``` sql
START TRANSACTION or BEGIN; 
UPDATE bankaccounts SET funds=funds-100 WHERE account_no='ACC1';
UPDATE bankaccounts SET funds=funds+100 WHERE account_no='ACC2';
COMMIT; 
```


</details>
<details><summary>Summary</summary> 
<br>

In SQL transaction is grouping of statements into a single unit. A transaction satisfies all the ACID properties.

## Commands

- `BEGIN` / `START TRANSACTION`
- `COMMIT`
- `SAVEPOINT`
- `ROLLBACK`

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
