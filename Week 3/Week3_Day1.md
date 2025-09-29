## NoSQL, Document Databases, and MongoDB

### NoSQL Databases
NoSQL databases are alternatives to traditional relational (SQL) databases. They don't use tables with rows and columns, and they're designed for:

 - Flexibility: No fixed schema required
 - Scalability: Easy horizontal scaling across multiple servers
 - Performance: Optimized for specific use cases (like fast reads/writes)
 - Variety: Handle different data types (documents, key-value pairs, graphs, etc.)

Common NoSQL types include document databases, key-value stores, column-family stores, and graph databases.

### Document Databases
Document databases store data as "documents" (typically JSON-like format). Each document is a self-contained unit with key-value pairs. Key features:

 - Documents can have different structures (unlike SQL tables where every row must match)
 - Nested data and arrays are natural and easy to work with
 - No need for complex JOIN operations—related data often lives together in one document
 - Schema flexibility allows evolution without migrations

Think of documents like file folders: each contains all the information about one entity, and folders don't all need the same contents.

### MongoDB
MongoDB is the most popular document database. Key points:

 - Documents: Stores data in BSON (Binary JSON) format
 - Collections: Documents are grouped into collections (similar to tables in SQL)
 - Query language: Rich API for queries, updates, and aggregations
 - Indexing: Supports various index types for performance
 - Replication & Sharding: Built-in features for high availability and horizontal scaling

Basic structure: Database → Collections → Documents → Fields
Perfect for applications with evolving requirements, hierarchical data, or where related data should be stored together.


### MongoDB Collections
A collection is a group of MongoDB documents—similar to a table in SQL databases, but without a fixed schema. Key characteristics:

 - All collections live within a database
 - Documents in a collection typically represent the same type of entity (e.g., "users", "products", "orders")
 - No enforced schema: documents in the same collection can have completely different fields
 - Created implicitly when you insert the first document

MongoDB Documents
A document is a single record in MongoDB, stored in BSON format (like JSON with additional data types). Key characteristics:

 - Composed of field-value pairs: { "name": "Alice", "age": 25 }
 - Can contain nested documents and arrays for complex data structures
 - Each document has a unique _id field (auto-generated if not provided)
 - Maximum size: 16MB per document
 - Flexible structure means different documents can have different fields

```BSON
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "age": 28,
  "hobbies": ["reading", "hiking"],
  "address": {
    "city": "Boston",
    "state": "MA"
  }
}
```
