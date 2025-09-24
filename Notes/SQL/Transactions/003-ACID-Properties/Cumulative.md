
<details><summary>Learning Objectives</summary>

<br>

After completing this module, associates should be able to:
- Define Atomicity
- Define Consistency
- Define Isolation
- Define Durability
</details>
<details><summary>Description</summary>
<br>

The ACID properties are a set of four properties that guarantee the reliability and consistency of database transactions. They can be remembered using the acronym ACID: Atomicity, Consistency, Isolation, and Durability.

## Atomicity

A transaction is considered to be atomic if it cannot be further broken down into individual operations, and all of the operations that occur within a transaction either succeed or fail as a single unit. If a single operation fails during a transaction, then everything is considered to have failed and must be rolled back.

## Consistency

One of the advantages of using a transaction is that, even if the transaction is a success or a failure, the database is consistent, and the data integrity is maintained.

## Isolation

Every transaction is isolated from other transactions. Therefore, a transaction shouldn't affect other transactions running at the same time. Stated another way, data modifications made by one transaction should be isolated from the data modifications made by other transactions. So, while a transaction can see data in the state it was in before another concurrent transaction modified it, as well as after the second transaction has completed, it cannot see any intermediate states.

## Durability

Data modifications that take place within a successful transaction may be safely considered to be stored in the database regardless of whatever else may occur. As each transaction is completed, a row is entered in the database transaction log. Thus, in the event of a system failure that requires the database to be restored from a backup, you can use this transaction log to get the database back to the state it was in after a successful transaction.
</details>
<details><summary>Real World Application</summary>
<br>

Database transactions are a backbone of using a database for small and large-scale applications. It may be difficult at first to see how each of the properties of these transactions are applied to this larger context, so please review these examples:

## Atomicity

A bank transaction of debiting $100 from ACC1 and crediting it to ACC2 should be atomic, if either of the statements in this transaction fails, the transaction of transferring funds from ACC1 to ACC2 should fail.

## Consistency

Consider two bank accounts ACC1 and ACC2 with funds of 10000 and 9000, which is is total of 19000, after a transaction of transferring $50 from ACC2 to ACC1 the funds in ACC1 is $10050 and ACC2 are $8950, which means the totals funds in AC1 and ACC2 adds up to $19000, So the funds in ACC1 and ACC2 are consistent before and after the Transaction.

## Isolation

Consider that the user A withdraws $100 and user B withdraws $250 from user ACC1 account, which has a balance of $1,000. Since both A and B draw from ACC1 account, one of the users is required to wait until the other user transaction is completed, avoiding inconsistent data.

## Durability

Any real-life changes made to any database like transferring funds, crediting or debiting funds, updating employee details and updating grades of a student, etc are durable. once these transactions are successfully executed, the changes made to the database are permanent even if an unexpected system failure or an error occurs.
</details>
<details><summary>Implementation</summary>
<br>

For the following examples consider a banking application which allows funds to transfer between accounts.

## Atomicity

Consider transferring 50$ from an account (ACC1) to another account (ACC2) where we check if ACC1 has sufficient funds.
```sql
START TRANSACTION;
UPDATE TABLE bankaccounts SET funds = funds-50 WHERE account_no= ACC1 AND funds>50;
UPDATE TABLE bankaccounts SET funds = funds+50 WHERE account_no= ACC2;
COMMIT;
```

In the above example debiting 50$ from ACC1 and crediting 50$ to ACC2 is a single transaction. If the entire transaction was not atomic, then it would be possible that our application debits ACC1 but does not credit ACC2 due to some error.

## Consistency

Building off of this example, let's examine ACC1 and ACC2

```sql
SELECT * FROM bankaccounts;
```
**RESULT**:

|account_no |funds|
|-----------|-----|
| ACC1      | 850 |
| ACC2      |1,150|

From the above table we can conclude that the sum of funds in ACC1 and ACC2 is 2000$.

Consider a transaction of transfering 150$ funds from ACC2 to ACC1.  

```sql
START TRANSACTION;
UPDATE TABLE bankaccounts SET funds = funds-150 WHERE account_no= ACC2;
UPDATE TABLE bankaccounts SET funds = funds+150 WHERE account_no= ACC1;
COMMIT;
```

```sql
SELECT * FROM bankaccounts;
```

**RESULT**:

|account_no |funds|
|-----------|-----|
| ACC1      |1,000|
| ACC2      |1,000|

From the above table it can be observed that the total funds in ACC1 and ACC2 are 2000$, from this we can conclude that the database is consistent before and after the transaction.

## Isolation

Expanding on this code, we take the following steps:

**Step 1**: create a new bank account named ACC3

```sql
INSERT INTO bankaccounts VALUES("ACC3", 1000);
```
**Step 2 (transaction 1)**: crediting 1000$ funds to ACC3

```sql
START TRANSACTION or BEGIN;
UPDATE bankaccounts SET funds=funds+1000 WHERE account_no='ACC3';
COMMIT;
```

**Step 3 (transaction 2)**: transferring 100$ from ACC2 to ACC1.

```sql
START TRANSACTION or BEGIN;
UPDATE bankaccounts SET funds=funds-100 WHERE account_no='ACC2';
UPDATE bankaccounts SET funds=funds+100 WHERE account_no='ACC1';
COMMIT;
```
In the above example, transaction 1 and transaction 2 are concurrent, as we are affecting different accounts with each update statement.

## Durability

Let's look at a database before and after a successful transaction:
```sql
SELECT * FROM banckaccounts;
```
|account_no |funds|
|-----------|-----|
| ACC1      |1,100|
| ACC2      |  900|
| ACC3      |1,000|

```sql
START TRANSACTION or BEGIN;
UPDATE bankaccounts SET funds=funds+100 WHERE account_no='ACC3';
COMMIT;
```

```sql
SELECT * FROM banckaccounts;
```  

|account_no |funds|
|-----------|-----|
| ACC1      |1,100|
| ACC2      |  900|
| ACC3      |1,100|

From the above example, it can be observed that the results of the transaction, which is crediting 100$ to ACC3 are successfully updated into the database.


</details>
<details><summary>Summary</summary> 
<br>

* Atomicity is combining all statements into a single unit.
    * if a database crashes for some reason, atomicity makes sure that the entire transaction is rolled back, and partial results are not updated in the database.
* Consistency is important to maintain data integrity, a database should consistent before and after a transaction.
   * All inconsistent data is removed, and all transactions that might cause inconsistency are aborted and an error is created or transcribed into an error log.
* Isolation is a property that guarantees the individuality of each transaction and prevents them from being affected from other transactions.
    * It ensures that transactions are securely and independently processed at the same time without interference, but it does not ensure the order of transactions.
* Durability ensures that the data changes caused by the successful execution of a transaction become permanent in the database.
   * The durability of the data is so permanent that even if the system fails or leads to a crash, the database still survives, and the changes of a transaction are updated in the database.
* The ACID property of DBMS plays a vital role in maintaining the consistency and availability of data in the database.


</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
