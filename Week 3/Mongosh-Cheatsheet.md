# MongoDB Shell (mongosh) Cheat Sheet

## Connection

```bash
# Connect to local MongoDB
mongosh

# Connect to specific host and port
mongosh "mongodb://localhost:27017"

# Connect with authentication
mongosh "mongodb://username:password@localhost:27017"

# Connect to Atlas or remote cluster
mongosh "mongodb+srv://cluster.mongodb.net" --username youruser

# Connect to specific database
mongosh "mongodb://localhost:27017/myDatabase"
```

## Database Operations

```javascript
// Show all databases
show dbs

// Switch to or create a database
use myDatabase

// Show current database
db.getName()

// Drop current database
db.dropDatabase()
```

## Collection Operations

```javascript
// Show all collections in current database
show collections

// Create a collection
db.createCollection("users")

// Drop a collection
db.users.drop()
```

## Insert Documents

```javascript
// Insert one document
db.users.insertOne({ name: "Alice", age: 30, email: "alice@example.com" })

// Insert multiple documents
db.users.insertMany([
  { name: "Bob", age: 25, email: "bob@example.com" },
  { name: "Charlie", age: 35, email: "charlie@example.com" }
])
```

## Query Documents

```javascript
// Find all documents
db.users.find()

// Find with pretty formatting
db.users.find().pretty()

// Find one document
db.users.findOne()

// Find with filter
db.users.find({ age: 30 })

// Find with multiple conditions (AND)
db.users.find({ age: 30, name: "Alice" })

// Find with OR condition
db.users.find({ $or: [{ age: 25 }, { age: 35 }] })

// Find with comparison operators
db.users.find({ age: { $gt: 25 } })  // greater than
db.users.find({ age: { $gte: 25 } }) // greater than or equal
db.users.find({ age: { $lt: 35 } })  // less than
db.users.find({ age: { $lte: 35 } }) // less than or equal
db.users.find({ age: { $ne: 30 } })  // not equal

// Find with IN operator
db.users.find({ age: { $in: [25, 30, 35] } })

// Find with regex pattern
db.users.find({ name: /^A/ })  // names starting with 'A'

// Projection (select specific fields)
db.users.find({}, { name: 1, email: 1, _id: 0 })

// Limit results
db.users.find().limit(5)

// Skip results
db.users.find().skip(10)

// Sort results
db.users.find().sort({ age: 1 })   // ascending
db.users.find().sort({ age: -1 })  // descending

// Count documents
db.users.countDocuments()
db.users.countDocuments({ age: { $gt: 25 } })
```

## Update Documents

```javascript
// Update one document
db.users.updateOne(
  { name: "Alice" },
  { $set: { age: 31 } }
)

// Update multiple documents
db.users.updateMany(
  { age: { $lt: 30 } },
  { $set: { status: "young" } }
)

// Replace entire document
db.users.replaceOne(
  { name: "Alice" },
  { name: "Alice", age: 31, email: "newalice@example.com" }
)

// Increment a field
db.users.updateOne(
  { name: "Bob" },
  { $inc: { age: 1 } }
)

// Add to array
db.users.updateOne(
  { name: "Alice" },
  { $push: { hobbies: "reading" } }
)

// Remove from array
db.users.updateOne(
  { name: "Alice" },
  { $pull: { hobbies: "reading" } }
)
```

## Delete Documents

```javascript
// Delete one document
db.users.deleteOne({ name: "Alice" })

// Delete multiple documents
db.users.deleteMany({ age: { $lt: 25 } })

// Delete all documents in collection
db.users.deleteMany({})
```

## Aggregation

```javascript
// Basic aggregation pipeline
db.users.aggregate([
  { $match: { age: { $gte: 25 } } },
  { $group: { _id: "$status", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
])

// Average calculation
db.users.aggregate([
  { $group: { _id: null, avgAge: { $avg: "$age" } } }
])
```

## Indexes

```javascript
// Create index
db.users.createIndex({ email: 1 })

// Create compound index
db.users.createIndex({ name: 1, age: -1 })

// Create unique index
db.users.createIndex({ email: 1 }, { unique: true })

// Show indexes
db.users.getIndexes()

// Drop index
db.users.dropIndex("email_1")
```

## Utility Commands

```javascript
// Get collection stats
db.users.stats()

// Explain query execution
db.users.find({ age: 30 }).explain("executionStats")

// Exit mongosh
exit
// or
quit()
```
