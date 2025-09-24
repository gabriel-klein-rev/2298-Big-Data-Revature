# Overview

This document offers and overview of data types used in MongoDB.

# BSON

MongoDB stores data in BSON format. [BSON](http://bsonspec.org/) is a binary serialization format used to store documents and make remote procedure calls. BSON has support for the following data types (v4.x):
| Type | Alias |
|---|---|
| Double | "double" |
| String | "string" |
| Object | "object" |
| Array | "array" |
| Binary Data | "binData" |
| ObjectId | "objectId" |
| Boolean | "bool" |
| Date | "date" |
| Null | "null" |
| Regular Expression | "regex" |
| JavaScript | "javascript" |
| 32-bit Integer | "int" |
| Timestamp | "timestamp" |
| 64-bit integer | "long" |
| Decimal128 | "decimal" |
| Min key | "minKey" |
| Max key | "maxKey" |

# Special Data type notes

Most data types are self explanatory, but some require a some special considerations.

## String

BSON strings are `UTF-8` encoded. Most programming languages convert from native format to `UTF-8` when serializing and deserializing BSON. This gives support for most international characters in BSON string.

## Timestamps

BSON timestamps have an internal MongoDB use and is separate from the `Date` data type. BSON timestamps are 64-bit values:

- The most significant 32-bits are **time_t** (seconds from Unix epoch)
- The least significant 32-bits are an increment **ordinal** for operations within a given second.

Although BSON format is little-endian (least significant bits first), the `mongod` always compares the **time_t** field before the **ordinal** field on all platforms.

## Date

BSON Date is a 64-bit signed integer that represents the number of milliseconds since the Unix Epoch (Jan 1, 1970). This results in a range of 290 million years in the past and future. Negative number represent times before 1970.

## ObjectId

ObjectIds are small, likely unique identifiers. ObjectId values are 12 byte values consisting of:

- 4-byte timestamp representing the ObjectId's creation
- 5-byte random value
- 3-byte incrementing counter initialized to a random value

Although BSON is little-endian, ObjecId's timestamp and counter are big-endian, with the most significant bytes appearing first in the byte sequence.

MongoDB documents stored in a collection require a unique \_id field which acts as a primary key. If a document is inserted without an \_id field the MongoDB driver will automatically generate an ObjectId for the \_id value. This also works on operations with `upsert: true`
