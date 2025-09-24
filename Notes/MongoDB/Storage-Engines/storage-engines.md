# Overview

This document explains the storage engine options in MongoDB.

# References

- [Mongo Docs Storage Engines](https://docs.mongodb.com/manual/core/storage-engines/)
- [Mongo Docs WiredTiger](https://docs.mongodb.com/manual/core/wiredtiger/)
- [Mongo Docs In-Memory Storage](https://docs.mongodb.com/manual/core/inmemory/)

# Storage Engines

The storage of MongoDB is responsible for managing data storage. Currently, there are two(2) options for storage management:

1. WiredTiger -- default, recommended storage engine for most use-cases. Offers document-level concurrency, compression, checkpointing, and more
2. In-Memory Storage -- available in MongoDB Enterprise. Offers in-memory storage for predictable latencies.

See the linked documents for more specs and feature details.
