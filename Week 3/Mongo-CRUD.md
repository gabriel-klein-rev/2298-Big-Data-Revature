# MongoDB: CRUD Operations

## Creating Documents

### Insert One Document
```javascript
db.collection.insertOne({ 
  name: "John",
  age: 30
})
```

### Insert Multiple Documents
```javascript
db.collection.insertMany([
  { name: "John", age: 30 },
  { name: "Jane", age: 25 }
])
```

## Reading Documents

### Find All
```javascript
db.collection.find()
```

### Find with Filter
```javascript
db.collection.find({ age: { $gte: 25 } })
```

### Find One
```javascript
db.collection.findOne({ name: "John" })
```

### Common Query Operators
- `$eq` - Equal
- `$gt` / `$gte` - Greater than / or equal
- `$lt` / `$lte` - Less than / or equal
- `$in` - Match any value in array
- `$and` / `$or` - Logical operators

### Projection (select fields)
```javascript
db.collection.find(
  { age: { $gte: 25 } },
  { name: 1, age: 1, _id: 0 }  // 1=include, 0=exclude
)
```

### Sorting and Limiting
```javascript
db.collection.find()
  .sort({ age: -1 })  // -1=descending, 1=ascending
  .limit(10)
  .skip(20)
```

## Updating Documents

### Update One Document
```javascript
db.collection.updateOne(
  { filter },
  { $set: { field: "value" } }
)
```

### Update Multiple Documents
```javascript
db.collection.updateMany(
  { filter },
  { $set: { field: "value" } }
)
```

### Replace Entire Document
```javascript
db.collection.replaceOne(
  { _id: ObjectId("...") },
  { newField: "newValue" }
)
```

### Common Update Operators
- `$set` - Set field value
- `$unset` - Remove field
- `$inc` - Increment numeric value
- `$push` - Add to array
- `$pull` - Remove from array
- `$addToSet` - Add to array if not exists

### Examples
```javascript
// Update multiple fields
db.users.updateOne(
  { username: "john" },
  { 
    $set: { email: "john@example.com" },
    $inc: { age: 1 },
    $push: { tags: "active" }
  }
)

// Remove fields with $unset
db.users.updateOne(
  { username: "john" },
  { 
    $unset: { 
      temporaryField: "",  // value doesn't matter
      deprecatedField: 1   // any value works
    }
  }
)
```

## Deleting Documents

### Delete One Document
```javascript
db.collection.deleteOne({ filter })
```

### Delete Multiple Documents
```javascript
db.collection.deleteMany({ filter })
```

### Delete All Documents in Collection
```javascript
db.collection.deleteMany({})
```

## Managing Collections

### Drop Collection
```javascript
db.collection.drop()
```

### Drop Database
```javascript
db.dropDatabase()
```

## Return Values
All operations return:
- `acknowledged`: true/false
- `matchedCount`: documents matched
- `modifiedCount`: documents changed (update)
- `deletedCount`: documents removed (delete)
