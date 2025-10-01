# MongoDB: Linked vs Embedded Documents

## Embedded Documents
Store related data together in a single document. This is MongoDB's denormalized approach where all related information lives in one place.

```javascript
{
  _id: ObjectId("..."),
  name: "Alice",
  address: {
    street: "123 Main St",
    city: "Boston",
    zip: "02101"
  },
  orders: [
    { product: "Laptop", total: 999.99, date: ISODate("2025-01-15") },
    { product: "Mouse", total: 25.00, date: ISODate("2025-02-10") }
  ]
}
```

**Key characteristics:**
- Single query retrieves all data
- Atomic operations - updates to embedded docs happen in one transaction
- Better read performance (no joins needed)
- Data duplication if same info embedded in multiple documents
- 16MB document size limit
- Entire document is read/written even for small updates

## Linked Documents (References)
Store ObjectId references to documents in other collections. This is MongoDB's normalized approach, conceptually similar to foreign keys in relational databases.

```javascript
// users collection
{
  _id: ObjectId("507f1f77bcf86cd799439011"),
  name: "Alice",
  email: "alice@example.com"
}

// orders collection
{
  _id: ObjectId("..."),
  userId: ObjectId("507f1f77bcf86cd799439011"),  // reference (like FK)
  product: "Laptop",
  total: 999.99
}
```

**Key characteristics:**
- Smaller documents, no duplication (normalized like SQL)
- Can reference same data from multiple places
- Flexible - related docs updated independently
- Requires multiple queries or `$lookup` for complete data (similar to SQL JOINs)
- **Critical difference from SQL:** No enforced referential integrity—the database won't prevent you from deleting a user who has orders, or creating an order with an invalid userId. Your application code must manage these relationships and maintain data consistency.
- Better for large, unbounded relationships (one user, thousands of orders)

## Querying Linked Documents

**Simple query:**
```javascript
db.orders.find({ userId: ObjectId("507f1f77bcf86cd799439011") })
```

**Using $lookup (join):**
```javascript
db.users.aggregate([
  {
    $lookup: {
      from: "orders",           // collection to join
      localField: "_id",        // field in users
      foreignField: "userId",   // field in orders
      as: "orders"              // output array
    }
  }
])

// Result:
{
  _id: ObjectId("507f1f77bcf86cd799439011"),
  name: "Alice",
  email: "alice@example.com",
  orders: [
    { _id: ObjectId("..."), userId: ObjectId("..."), product: "Laptop", total: 999.99 },
    { _id: ObjectId("..."), userId: ObjectId("..."), product: "Mouse", total: 25.00 }
  ]
}
```

**Filter joined results:**
```javascript
db.users.aggregate([
  {
    $lookup: {
      from: "orders",
      localField: "_id",
      foreignField: "userId",
      as: "orders"
    }
  },
  { $match: { "orders.total": { $gt: 50 } } }
])
```

## Choosing Your Strategy

The decision between embedded and linked documents hinges on several key factors that you should evaluate together rather than in isolation.

**Access patterns are your primary guide.** If data is consistently retrieved together (user + address), embed it for single-query performance. If data is often accessed independently (viewing orders without user details), linking provides flexibility to fetch only what you need without loading unnecessary information.

**Relationship cardinality matters significantly.** One-to-one and one-to-few relationships (user has one address, post has 5 comments) work well embedded. One-to-many relationships with unbounded growth (user has thousands of orders) must be linked to avoid hitting the 16MB document limit and to prevent loading massive documents when you only need parent data.

**Update frequency creates different tradeoffs.** Embedded documents provide atomic updates but require rewriting the entire parent document, even for small changes. This is fine for infrequently updated data like addresses, but problematic for rapidly changing data like order statuses. Linked documents allow surgical updates to individual records without touching parents, though you lose cross-document atomicity.

**Data duplication has consequences.** Embedding often means duplicating shared data across multiple parents (product details in every order). This uses more storage and requires updating many documents when shared data changes. Linking maintains a single source of truth, making updates consistent but requiring joins to retrieve complete information.

**Query complexity versus performance.** Embedded documents offer the fastest, simplest queries—one query returns everything. Linked documents require multiple queries or `$lookup` joins, which add complexity and latency. However, if you rarely need all the data together, the cost of loading unnecessary embedded data can outweigh join overhead.

### Hybrid Approach
Mix strategies to optimize for different access patterns. Embed frequently accessed data while linking to less common data:

```javascript
{
  _id: ObjectId("..."),
  name: "Alice",
  address: { street: "123 Main", city: "Boston" },  // embedded - always needed
  recentOrderIds: [ObjectId("..."), ObjectId("...")]  // linked - accessed separately
}
```
