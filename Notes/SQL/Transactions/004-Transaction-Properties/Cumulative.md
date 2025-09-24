# Cumulative for the  Transaction Properties
<details><summary>Learning Objectives</summary>

# Learning Objectives for Transaction Properties topic.

### Learning Objectives

- Implementation of the previous transaction properties: ACID
</details>
<details><summary>Description</summary>

# Description

There are four (4) properties of a transaction which define key aspects related to its behavior. They can be remembered using the acronym *ACID* description the previous topic: 
- ***A***tomicity 
- ***C***onsistency
- ***I***solation
- ***D***urability

</details>
<details><summary>Real World Application</summary>

# Real World Application

Please review how each of these properties can affect real-world applications

## Atomicity
A bank transaction of debiting 100$ from ACC1 and crediting it to ACC2  should be atomic, if either of the statements in this transaction fails, the transaction of transferring funds from ACC1 to ACC2 should be failed.

## Consistency
Consider two bank accounts ACC1 and ACC2 with funds of 10000$ and 9000$, which is is total of 19000$, after a transaction of transferring 50$ from ACC2 to ACC1 the funds in ACC1 is 10050$ and ACC2 are 8950$, which means the totals funds in AC1 and ACC2 adds up to 19000, So the funds in ACC1 and ACC2 are consistent before and after the Transaction.

## Isolation
Consider that the user A withdraws $100 and user B withdraws $250 from user ACC1 account, which has a balance of $1,000. Since both A and B draw from ACC1 account, one of the users is required to wait until the other user transaction is completed, avoiding inconsistent data.

## Durability
Any real life changes made to any database like transferring funds, crediting or debiting funds, updating employee details and updating grades of a student, etc are durable. once these transactions are successfully executed, the changes made to the database are permanent even if an unexpected system failure or an error occurs.
</details>
<details><summary>Implementation</summary> 

# Implementation

For the following examples consider a banking application which allows funds to tranfer between accounts.

## Atomicity
Consider transferring 50$ from an account (ACC1) to another account (ACC2) where we check if ACC1 has sufficient funds.

``` sql
START TRANSACTION;
UPDATE TABLE bankaccounts SET funds = funds-50 WHERE account_no= ACC1 AND funds>50;
UPDATE TABLE bankaccounts SET funds = funds+50 WHERE account_no= ACC2;
COMMIT;
```
In the above example debiting 50$ from ACC1 and crediting 50$ to ACC2 is a single transaction. If the entire transaction was not atomic, then it would be possible that our application debits ACC1 but does not credit ACC2 due to some error.


## Consistency
Building off of this example, lets examine ACC1 and ACC2 

``` sql
SELECT * FROM bankaccounts;
```
result:
| account_no | funds   |
|------------|---------|
| ACC1       |  850.00 |
| ACC2       | 1150.00 |

from the above table we can conclude that the sum of funds in ACC1 and ACC2 is 2000$.

Consider a transaction of transfering 150$ funds from ACC2 to ACC1.
``` sql
START TRANSACTION;
UPDATE TABLE bankaccounts SET funds = funds-150 WHERE account_no= ACC2;
UPDATE TABLE bankaccounts SET funds = funds+150 WHERE account_no= ACC1;
COMMIT;
```
``` sql
SELECT * FROM bankaccounts;
```
result:
| account_no | funds   |
|------------|---------|
| ACC1       | 1000.00 |
| ACC2       | 1000.00 |

from the above table it can be observed that the total funds in ACC1 and ACC2 are 2000$, from this we can conclude that the database is consistent before and after the transaction.

## Isolation
Expanding on this code, we take the following steps:

step 1:create a new bank account named ACC3
``` sql
INSERT INTO bankaccounts VALUES("ACC1", 1000);
```
step 2:transaction 1:crediting 1000$ funds to ACC3
```sql 
START TRANSACTION or BEGIN;
UPDATE bankaccounts SET funds=funds+1000 WHERE account_no='ACC3';
COMMIT;
```
step 3: transaction 2: transfering 100$ from ACC2 to ACC1.
```sql
START TRANSACTION or BEGIN;
UPDATE bankaccounts SET funds=funds-100 WHERE account_no='ACC2';
UPDATE bankaccounts SET funds=funds+100 WHERE account_no='ACC1';
COMMIT;
```
in the above example, transaction 1 and transaction 2 are concurrent, as we are effecting different accounts with each update statement.

## Durability
Now, if we examine our database:

``` sql 
SELECT * FROM banckaccounts;
```
| account_no | funds   |
|------------|---------|
| ACC1       | 1100.00 |
| ACC2       |  900.00 |
| ACC3       | 1000.00 |



```sql
START TRANSACTION or BEGIN;
UPDATE bankaccounts SET funds=funds+100 WHERE account_no='ACC3';
COMMIT;
```
``` sql 
SELECT * FROM banckaccounts;
```
| account_no | funds   |
|------------|---------|
| ACC1       | 1100.00 |
| ACC2       |  900.00 |
| ACC3       | 1100.00 |

from the above example, it can be observed that the results of the transaction, which is crediting 100$ to ACC3 are successfully updated into the database.
</details>
<details><summary>Summary</summary> 

# Summary

- atomicity is combining all statements into a single unit.
  - if a database crashes for some reason, atomicity makes sure that the entire transaction is rolled back and partial results are not updated in the database
- Consistency is important to maintain data integrity, a database should consistent before and after a transaction.
  - All inconsistent data is removed, and all transactions that might cause inconsistency are aborted and an error is created or transcribed into an error log.
- Isolation is a property that guarantees the individuality of each transaction, and prevents them from being affected from other transactions. 
  - It ensures that transactions are securely and independently processed at the same time without interference, but it does not ensure the order of transactions.
- In DBMS, durability ensures that the data changes caused by the successful execution of a transaction become permanent in the database. 
  - The durability of the data is so permanent that even if the system fails or leads to a crash, the database still survives and the changes of a transaction are updated in the database.
- The ACID property of DBMS plays a vital role in maintaining the consistency and availability of data in the database.
</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
