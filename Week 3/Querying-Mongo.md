# MongoDB Querying Guide

## Basic Query Structure

```
db.collection.find(query, projection)
```

- **query**: Selection criteria using query operators
- **projection**: Which fields to return (optional)

## Simple Queries

### Finding Documents

```
// All documents
db.students.find()

// Exact match
db.students.find({grade: "A"})

// Multiple conditions (implicit AND)
db.students.find({age: 21, major: "Computer Science"})

// Find one document
db.students.findOne({studentId: 12345})
```

## Comparison Operators

- `$eq` - Equal to
- `$ne` - Not equal to
- `$gt` - Greater than
- `$gte` - Greater than or equal to
- `$lt` - Less than
- `$lte` - Less than or equal to
- `$in` - Matches any value in array
- `$nin` - Matches none of the values in array

### Examples

```
// Students older than 20
db.students.find({age: {$gt: 20}})

// Students with grades A, B, or C
db.students.find({grade: {$in: ["A", "B", "C"]}})

// Exclude multiple values from same field
db.students.find({last_name: {$nin: ["Plummer", "Lowery"]}})

// Range query
db.students.find({age: {$gte: 18, $lte: 22}})
```

## Logical Operators

### Implicit AND

```
db.students.find({age: {$gte: 20}, grade: "A"})
```

### $or Operator

```
db.students.find({
  $or: [
    {major: "Computer Science"},
    {major: "Engineering"}
  ]
})
```

### Explicit $and

```
db.students.find({
  $and: [
    {age: {$gte: 20}},
    {grade: "A"}
  ]
})
```

### $not and $nor

```
db.students.find({age: {$not: {$lt: 18}}})

db.students.find({
  $nor: [
    {grade: "F"},
    {attendance: {$lt: 75}}
  ]
})
```

## Querying Arrays

```
// Find documents containing "Math" in courses array
db.students.find({courses: "Math"})

// Must contain ALL specified values
db.students.find({courses: {$all: ["Math", "Physics"]}})

// Array has exactly 3 elements
db.students.find({courses: {$size: 3}})

// Contains at least one of these values
db.students.find({courses: {$in: ["Math", "Chemistry"]}})
```

## Querying Nested Documents

Use dot notation to access nested fields:

```
// Document: {name: "Sarah", address: {city: "Boston", state: "MA"}}

db.students.find({"address.city": "Boston"})
db.students.find({"address.state": "MA", "address.city": "Boston"})
```

## Element Operators

```
// Field exists
db.students.find({email: {$exists: true}})

// Field has specific type
db.students.find({age: {$type: "number"}})

// Field is null
db.students.find({grade: null})
```

## Type Conversion in Queries

When fields are stored as wrong type (e.g., age as string "48" instead of number):

```
// Compare string age to number
db.students.find({$expr: {$eq: [{$toInt: "$age"}, 48]}})

db.students.find({$expr: {$gt: [{$toInt: "$age"}, 30]}})
```

Fix the data permanently:

```
db.students.updateMany(
  {age: {$type: "string"}},
  [{$set: {age: {$toInt: "$age"}}}]
)
```

## Projection

Control which fields are returned:

```
// Include only name and grade, exclude _id
db.students.find({}, {name: 1, grade: 1, _id: 0})

// Exclude only address field
db.students.find({}, {address: 0})
```

Note: Cannot mix inclusion and exclusion (except _id).

## Regular Expressions

```
// Names starting with "J"
db.students.find({name: /^J/})

// Case-insensitive search
db.students.find({name: {$regex: "smith", $options: "i"}})
```

## Sorting, Limiting, and Skipping

### Sort
- `1` = ascending
- `-1` = descending

```
db.students.find().sort({age: 1})
db.students.find().sort({grade: -1})

// Multiple sort fields
db.students.find().sort({grade: 1, name: 1})
```

### Limit and Skip

```
// First 10 results
db.students.find().limit(10)

// Skip first 20, get next 10 (pagination)
db.students.find().skip(20).limit(10)
```

### Complete Example

```
db.students.find(
  {grade: "A"}, 
  {name: 1, age: 1, _id: 0}
).sort({age: -1}).skip(10).limit(10)
```

### Pagination Pattern

```
// Page 1
db.students.find({}).sort({name: 1}).skip(0).limit(10)

// Page 2
db.students.find({}).sort({name: 1}).skip(10).limit(10)

// Page 3
db.students.find({}).sort({name: 1}).skip(20).limit(10)
```

## Counting Documents

```
// Count all
db.students.countDocuments()

// Count matching criteria
db.students.countDocuments({grade: "A"})
```

## Common Query Patterns

```
// Missing field
db.students.find({grade: {$exists: false}})

// Recent records
db.students.find({createdAt: {$gte: new Date("2024-01-01")}})

// Complex combination
db.students.find({
  $and: [
    {age: {$gte: 18}},
    {
      $or: [
        {major: "Computer Science"},
        {major: "Engineering"}
      ]
    },
    {gpa: {$gte: 3.0}}
  ]
})

// Everything together
db.students.find(
  {major: "CS", gpa: {$gte: 3.5}},
  {name: 1, gpa: 1, _id: 0}
).sort({gpa: -1}).skip(0).limit(20)
```
