# Overview

This document provides explanation and demonstrations of aggregation operations in MongoDB.

# References

[Mongo Docs Aggregation](https://docs.mongodb.com/manual/aggregation)

# Prequisites

- [CRUD Operations](./crud-operations.md)

# Aggregation

Aggregation operations process data records and return a computed result. Aggregation operation group values from multiple documents together and can perform a variety of operations. MongoDB provides the following ways to perform aggregation.

- aggregation pipeline
- map-reduce pipeline
- single purpose aggregation.

## Aggregation Pipeline

MongoDB aggregation framework is modeled through a multi-staged, data processing pipeline. Documents enter the pipeline and are transformed from one stage to the other.

```shell
db.paints.aggregate([
    {$match: {finish: 'matte'}},
    {$group: {_id: "$finish", total: {$sum: "$price"}}}
])
```

Results

```shell
{ "_id" : "matte", "total" : 6 }
```

With current dataset in the collection, there are 2 paints with a matte finish at 3 for the price.

The stages for this query are as follows

1. `$match` stage filters the documents by **finish** and those documents are passed to the second stage.
2. `$group` stage groups the documents by the **finish** field to calculate the `$sum` of the price for each unique **finish**.

A basic aggregation pipeline, like above, provide filters for document transformation. More advanced pipelines provide tools for grouping, sorting, array aggregation. Also aggregation pipelines can use other operators for calculation or transformations.

## Single Purpose Aggregation Pipeline

MongoDB provides the following aggregation methods for single purpose use.

- db.collection.estimatedDocumentCount()
- db.collection.count()
- db.colleciton.distinct()

The single purpose pipeline is used for quick access to common aggregation processes, they are less flexible and capable than the aggregation pipeline

Count all

```shell
db.paints.count()
```

Results

```shell
4
```

Count all with finish filter

```shell
db.paints.count({finish: 'matte'})
```

Results

```
2
```

## Map-Reduce

Map-Reduce operations are more commonly done with the aggregation pipeline, since it provides better performance. For custom map-reduce operations, MongoDB
proved the `$accumulator` and `$function`(v4.4) operators.
