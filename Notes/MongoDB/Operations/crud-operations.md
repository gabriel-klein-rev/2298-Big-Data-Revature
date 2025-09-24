# Overview

This document offers notes and examples for performing CRUD operations on a MongoDB database.

# References

- [MongoDB Docs CRUD](https://docs.mongodb.com/manual/tutorials/crud/)
- [MongoDB Docs Queries](https://docs.mongodb.com/manual/tutorials/query-documents/)
- [MongoDB Docs](https://docs.mongodb.com/manual/tutorials/query-documents/)

# MongoDB databases

MongoDB databases are a set of collections of documents. Each database can have one or more collections, with each containing many documents. A Mongo collection is similar to a SQL table. A Mongo document is similar to a SQL table row. A Mongo document contains fields that represent the document values similarly to how a SQL table row has columns.

# Create a database

To create a database connect to your desired mongo cluster.

Connect to a local cluster (from your local mongodb server directory)

```shell
./mongo.exe
```

To create a dabase issue the `use` command in the terminal. With the `use` command, mongodb will attempt to connect to the database. If the database doesn't exist, the cluster will create it.

```shell
use paintstore
```

If you issue `show dbs` command, which lists all databases, you won't see the bookstore database. You must do something to the database for MongoDB to complete the creation.

# Inserting

Inserting into a database can using the following commands

- db.collection.insert({})
- db.collection.insertOne({})
- db.collection.inserMany([{}])

**BE SURE** you are switched to the `paintstore` database

Insert a single document

```shell
db.paints.insertOne({"colorName" : "Bone White", "color" : "e4d4ba", finish: 'matte', price: 2.99})
```

`insertOne()` returns a document that includes the newly inserted document's \_id

```json
{
  "acknowledged": true,
  "insertedId": ObjectId("606b7ce95939206d9bb2dc28")
}
```

Insert many documents

```shell
db.paints.insertMany([
    {"colorName" : "Fiat Jaune", "color" : "fce903", "finish" : "gloss", "price": 1.50},
    {"colorName": "Vivid Malachite", "color" : "00cc33", "finish" : "semi-gloss", "price": 3.25},
    {"colorName" : "HootSuite", "color" : "003366", "finish" : "matte", "price": 2.99}
])
```

`insertMany()` returns a document that includes the new inserted documents \_id field values.

```shell
{
        "acknowledged" : true,
        "insertedIds" : [
                ObjectId("606b7ce95939206d9bb2dc29"),
                ObjectId("606b7ce95939206d9bb2dc2a"),
                ObjectId("606b7ce95939206d9bb2dc2b")
        ]
}
```

## Read Operations

### Find all

There are many ways to read data from a collection. The simplest way to query is to read all documents from a collection using `db.collection.find()`

**BE SURE** you are switched to the paintstore database.

```shell
db.paints.find()
```

`find()` without any arguments or 'matchers' will return a list of all documents in the collection.

```shell
{ "_id" : ObjectId("606b7ce95939206d9bb2dc28"), "colorName" : "Bone White", "color" : "e4d4ba", "finish" : "matte", "price" : 2.99 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc29"), "colorName" : "Fiat Jaune", "color" : "fce903", "finish" : "gloss", "price" : 1.5 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2a"), "colorName" : "Vivid Malachite", "color" : "00cc33", "finish" : "semi-gloss", "price" : 3.25 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2b"), "colorName" : "HootSuite", "color" : "003366", "finish" : "matte", "price" : 2.99 }
```

### Specifying Equality

To find documents that have certain values for fields you can provide `query filter document` to the find query.

Find all 'matte' finishes.

```shell
db.paints.find({finish: 'matte'})
```

Results

```shell
{ "_id" : ObjectId("606b7ce95939206d9bb2dc28"), "colorName" : "Bone White", "color" : "e4d4ba", "finish" : "matte", "price" : 2.99 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2b"), "colorName" : "HootSuite", "color" : "003366", "finish" : "matte", "price" : 2.99 }
```

### Query operators

The `query filter document` can include [query operators](https://docs.mongodb.com/manual/reference/operator/query/#std-label-query-selectors) to specify conditions on document fields

Find all 'matte' and 'semi-gloss' finishes.

```shell
db.paints.find({finish: {$in: ['matte', 'semi-gloss']}})
```

Results

```shell
{ "_id" : ObjectId("606b7ce95939206d9bb2dc28"), "colorName" : "Bone White", "color" : "e4d4ba", "finish" : "matte", "price" : 2.99 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2a"), "colorName" : "Vivid Malachite", "color" : "00cc33", "finish" : "semi-gloss", "price" : 3.25 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2b"), "colorName" : "HootSuite", "color" : "003366", "finish" : "matte", "price" : 2.99 }
```

`$in` operator returns any document with a field that has a value specified in the operator array. Query Operators start with a '$'. There are many `query` and `projection` operators. Pleas see the link for more information.

### And Conditions

`And` conditions can be specified by including multiple fields in the `query filter document`.

```shell
db.paints.find({colorName: 'HootSuite', finish: {$in: ['matte', 'semi-gloss']}})
```

Results

```shell
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2b"), "colorName" : "HootSuite", "color" : "003366", "finish" : "matte", "price" : 2.99 }
```

### Or Conditions

`Or` conditions are specified with the `$or` operator.

```shell
db.paints.find({$or: [{colorName: 'HootSuite'}, {finish: 'semi-gloss'}]})
```

Result

```shell
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2a"), "colorName" : "Vivid Malachite", "color" : "00cc33", "finish" : "semi-gloss", "price" : 3.25 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2b"), "colorName" : "HootSuite", "color" : "003366", "finish" : "matte", "price" : 2.99 }
```

### And/Or Conditions

`And` and `Or` conditions can specified together.

```shell
db.paints.find({price: {$lt: 3.0}, $or: [{colorName: 'Bone White'}, {color: 'fce903'}]})
```

Results

```shell
{ "_id" : ObjectId("606b7ce95939206d9bb2dc28"), "colorName" : "Bone White", "color" : "e4d4ba", "finish" : "matte", "price" : 2.99 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc29"), "colorName" : "Fiat Jaune", "color" : "fce903", "finish" : "gloss", "price" : 1.5 }
```

# Update Operations

Update operations modify data that already exist in a document. Updating documents can be performed by one of the following operations.

- db.collection.updateOne()
- db.collection.updateMany()
- db.collection.replaceOne()

## Update One

The signature for updateOne is`db.collection.updateOne(<filter>, <update>, <options>)`. This operation will only update the first matched document.

```shell
db.paints.updateOne({price: {$lt: 3.0}}, {$set: {price: 3.0}})
```

Result

```shell
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

The result of the update operation contains a `matchCount`, `modifiedCount`. The result document will `upsertId` if the `upsert` option is set to true.

`Upsert` can be used to either update a document or insert a new document if the filters don't match an existing document.

After running this `updateOne` operation, run a `find` query.

```shell
db.paints.find()
```

Results

```shell
{ "_id" : ObjectId("606b7ce95939206d9bb2dc28"), "colorName" : "Bone White", "color" : "e4d4ba", "finish" : "matte", "price" : 3 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc29"), "colorName" : "Fiat Jaune", "color" : "fce903", "finish" : "gloss", "price" : 1.5 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2a"), "colorName" : "Vivid Malachite", "color" : "00cc33", "finish" : "semi-gloss", "price" : 3.25 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2b"), "colorName" : "HootSuite", "color" : "003366", "finish" : "matte", "price" : 2.99 }
```

Observe that the price for only the first document was changed.

## Update Many

The signature for `updateMany` is similar to `updateOne`. This operation will update all matching documents.

```shell
db.paints.updateMany( {price: {$lt: 3.0}}, {$set: {price: 3.0}} )
```

Results

```shell
{ "acknowledged" : true, "matchedCount" : 2, "modifiedCount" : 2 }
```

The results are similar to `updateOne`, but this time multiple documents were updated. Run a `find` query again.

```shell
{ "_id" : ObjectId("606b7ce95939206d9bb2dc28"), "colorName" : "Bone White", "color" : "e4d4ba", "finish" : "matte", "price" : 3 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc29"), "colorName" : "Fiat Jaune", "color" : "fce903", "finish" : "gloss", "price" : 3 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2a"), "colorName" : "Vivid Malachite", "color" : "00cc33", "finish" : "semi-gloss", "price" : 3.25 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2b"), "colorName" : "HootSuite", "color" : "003366", "finish" : "matte", "price" : 3 }
```

Observe that all prices that were less than 3.0 have now been updated.

# Delete Operations

Delete operations remove documents from a collection. Deleting documents can be done with one of the following.

- db.collection.deleteOne()
- db.collection.deleteMany()
- db.collection.remove()

## Delete One

The `deleteOne` operation deletes the first document that matches the filter. The `deleteOne` signature is `db.collection.deleteOne(<filter>, <options>)`.

**BE SURE** you are switched to the paintstore database

```shell
db.paints.deleteOne({finish: 'matte'})
```

Result

```shell
{ "acknowledged" : true, "deletedCount" : 1 }
```

The result will contain the number of documents deleted.

Running a `db.paints.find()` will show that even though the collection contains multiple documents that match the filter, only the first matched document is deleted.

```shell
{ "_id" : ObjectId("606b7ce95939206d9bb2dc29"), "colorName" : "Fiat Jaune", "color" : "fce903", "finish" : "gloss", "price" : 3 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2a"), "colorName" : "Vivid Malachite", "color" : "00cc33", "finish" : "semi-gloss", "price" : 3.25 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2b"), "colorName" : "HootSuite", "color" : "003366", "finish" : "matte", "price" : 3 }
```

The `deleteOne` operation is best used with a **unique index** field like `_id` for precision deletion.

## Delete Many

The `deleteMany` operation deletes all documents that match the filter. The `deleteMany` signature is `db.collection.deleteMany(<filter>, <options>)`.

**NOTE** Re-insert the previously deleted document.

```shell
db.paints.insertOne({ "_id" : ObjectId("606b7ce95939206d9bb2dc28"), "colorName" : "Bone White", "color" : "e4d4ba", "finish" : "matte", "price" : 3 })
```

Delete all matte paints

```shell
db.paints.deleteMany({finish: 'matte'})
```

Result

```shell
{ "acknowledged" : true, "deletedCount" : 2 }
```

The results containt the number of documents deleted. Not that this time multiple documents have been deleted.

```shell
{ "_id" : ObjectId("606b7ce95939206d9bb2dc29"), "colorName" : "Fiat Jaune", "color" : "fce903", "finish" : "gloss", "price" : 3 }
{ "_id" : ObjectId("606b7ce95939206d9bb2dc2a"), "colorName" : "Vivid Malachite", "color" : "00cc33", "finish" : "semi-gloss", "price" : 3.25 }
```
