# MongoDB Indexing Notes

## Index Basics

**What are indexes?**
Data structures that improve query performance by allowing MongoDB to quickly locate documents without scanning entire collections.

**Default behavior:**
- Every collection has an `_id` index automatically
- Queries without indexes = collection scans (slow)

## Creating Indexes

```javascript
// Single field index
db.collection.createIndex({ field: 1 })  // 1 = ascending, -1 = descending

// Compound index
db.collection.createIndex({ field1: 1, field2: -1 })

// Unique index
db.collection.createIndex({ email: 1 }, { unique: true })

// Sparse index (only indexes docs with the field)
db.collection.createIndex({ optional: 1 }, { sparse: true })
```

## Index Types

- **Single Field**: Index on one field
- **Compound**: Multiple fields, order matters for queries
- **Multikey**: Automatically created for array fields
- **Text**: Full-text search on string content
- **Geospatial**: 2d or 2dsphere for location queries
- **Hashed**: For hash-based sharding

## Query Performance

```javascript
// Explain query execution
db.collection.find({ field: value }).explain("executionStats")

// Key metrics:
// - totalDocsExamined: docs scanned
// - executionTimeMillis: query time
// - IXSCAN = using index, COLLSCAN = full scan
```

## Compound Index Rules

**Index prefix rule**: Query can use compound index if it queries left-to-right fields

Given index: `{ a: 1, b: 1, c: 1 }`
- ✓ Can use: `{a}`, `{a,b}`, `{a,b,c}`
- ✗ Cannot use: `{b}`, `{c}`, `{b,c}`

**How it speeds up queries:**
The compound index speeds up lookups on any left-prefix, not just all columns together. Think of it like a phone book sorted by (LastName, FirstName) - you can quickly find "Smith" or "Smith, John", but can't efficiently find all "Johns" without scanning.

**Sort optimization**: Compound indexes can optimize sorting when sort order matches index order

## Best Practices

- Index fields used in query filters, sorts, and joins
- Limit indexes (each index costs write performance and storage)
- Use compound indexes for multiple field queries
- Put equality filters before range filters in compound indexes
- Monitor index usage: `db.collection.aggregate([{$indexStats:{}}])`
- Drop unused indexes

## Index Management

```javascript
// List indexes
db.collection.getIndexes()

// Drop index
db.collection.dropIndex("index_name")

// Create in background (for large collections)
db.collection.createIndex({ field: 1 }, { background: true })

// Rebuild indexes
db.collection.reIndex()
```

## Common Patterns

**Pagination**: Index sort fields
**Search**: Use text indexes or Atlas Search
**Time-series**: Compound index with timestamp
**Uniqueness**: Unique indexes for emails, usernames
