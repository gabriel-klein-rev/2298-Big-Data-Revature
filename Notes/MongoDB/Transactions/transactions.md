# Overview

This document offers explanations and demonstrations on database transactions in MongoDB.

**NOTE** This shell example **WILL NOT** work in a shell running locally with `mongod`. Transactions are not supported on single node databases. Running a sharded cluster or replica set is out of scoper in this document. A replica set can be simulated by connecting to a local instance of `mongod` and running `rs.initiate()`

# References

[MongoDB Docs Transactions](https://docs.mongodb.com/master/core/transactions/)

# Prequisites

- [MongoDB Operations CRUD](../d-operations/crud-operations.md)
- [MongoDB Data Modeling](../e-data-modeling/data-modeling.md)
- [MongoDB Data Modeling Relationships](../e-data-modeling/relationship.md)

# Transactions

A `transaction` is an exchange performed under an agreed-upon protocol. In the physical world, people engage in transactions daily. Common types of physical world transactions

- Verbal conversations
- Bank Transaction
- Grocery Checkout

Each example has an established. In the context of a database, a transaction is an exchange of data from an application to the database and vis-a-versa. Transactions are integral to data flow in an application and should be considered as a primary concern in design.

# MongoDB transactions

In MongoDB operations on a single document are always atomic. Utilizing patterns like embedded documents and arrays to model relationships in data alleviates the need to use normalized models and also the need for multi-document transactions in many use cases.

In situations that require multiple document atomicity, MongoDB supports multi-document transactions that can span over multiple documents, collections, databases, document operations, and shards.

MongoDB transactions use configurations for:

- transaction-level write concern
- transaction-level read concern
- transaction-level read preference

## Transaction Write Concern

The 'write concern`describes the level of acknowledgement from MongoDB for writes to`mongod`, `replica set`, or `sharded clusters`.

- If transaction-level concern is not set, it defaults to session-level
- If transaction-level concern and session-level concern are not set, it defaults to the client-level concern which `w: 1` by default.

Write Concern levels
| Level | Description |
|---|---|
| <number> | request acknowledgement that the write has propagated to <number> of specified replicas |
| majority | request acknowledgement that the write has propagated to the calculated majority of data-bearing voting members |

## Transaction Read Concern

The `read concern` controls the consistency and isolation of data read from replica sets and replica set shards. Read concerns can be set on the transaction, session, and client.

- if the transaction-level is unset, it defaults to the session-level
- if the transaction-level and session-level are unset, they default to the client-level which is set to **local** be default for reads against the primary.

Read Concern levels
| Level | Description |
|---|---|
| local | returns the most recent data available from the node, but can be rolled back. |
| available | returns the most recent data available from the node, but can be rolled back. Not available for `causally consistent sessions`.|
| majority | returns data that has been acknowledged by a majority of the replica set memebers. |
| linearlizable | returns data that reflects all successful majority-acknowledged writes that completed prior to the start of the read operation. The query may wait for concurrently executing writes to propagate to a majority of replica set members before returning results. |
| snapshot | returns data from a snapshot of majority committed data **if** the transaction is committed with `write concern` "marjority". If `write concern` "majority" is not used `snapshot` can not guarantee the read uses a snapshot of majority-committed data. For sharded clusters the "snapshot" view is sync'd across shards. |

## Shell Example

**BE SURE** to switch to `paintstore` database and drop all collections

Insert a new color into `paints` collection

```shell
db.paints.insertOne({"colorName" : "Bone White", "color" : "e4d4ba", finish: 'matte', price: 2.99}, {writeConcern: {w: "majority", wtimeout: 2000}})
```

This first statement issues write concerns at the opertion level.

Start a session and set transaction-level concerns

```shell
var session = db.getMongo().startSession({readPreference: {mode: "primary"}});

var paints = session.getDatabase("paintstore").paints;

session.startTransaction({readConcern: {level: "local"}, writeConcern: {w: "majority"}});

try {
    paints.insertOne({"colorName" : "Fiat Jaune", "color" : "fce903", "finish" : "gloss", "price": 1.50});
    paints.insertOne({"colorName": "Vivid Malachite", "color" : "00cc33", "finish" : "semi-gloss", "price": 3.25})
} catch(error) {
    session.abortTransaction();
    throw error;
}
session.commitTransaction();
session.endSession();
```
