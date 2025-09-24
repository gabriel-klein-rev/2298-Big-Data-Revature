# Overview

This document offers explanation of using MongoDB to model tree structures.

# References

- [MongoDB Docs Modeling Tree Structures](https://docs.mongodb.com/manual/applications/data-models-tree-structures/)

# Prerequisites

- [Data Modeling](./data-modeling.md)

# Tree structures

Tree structures are hierarchical structures that model parent-child relationships between entities. Tree structures are commonly seen in uses like OOP inheritance diagrams and HTML Node trees. Trees are good structures for search for data relationships. Tree store each entity as a node on the tree with logical relationship being expressed through parent-child associations.

In the `paintstore` database from previous examples, we may see a hierarchy as such.
![Modeling Tree Structure](./imgs/tree-structure.png)

Modeling the tree structure allows for easy queries based on the hierarchy. Common patterns are

- [Parent References](#parent-references)
- [Child References](#child-references)
- [Array of Ancestors](#array-of-ancestors)
- [Materialized Paths](#materialized-paths)
- [Nested Sets](#nested-sets)

## Parent References

Documents can be inserted with information about their parent.

Insert the items into the database

```shell
db.items.insertMany([
    {_id: "Item", parent: null},
    {_id: "Tool", parent: "Item"},
    {_id: "Brush", parent: "Tool"},
    {_id: "Scrapper", parent: "Tool"},
    {_id: "Stirrer", parent: "Tool"},
    {_id: "Coating", parent: "Item"},
    {_id: "Finish", parent: "Coating"},
    {_id: "Paint", parent: "Coating"},
    {_id: "Exterior", parent: "Paint"},
    {_id: "Interior", parent: "Paint"}
])
```

Results

```shell
{
    "acknowledged" : true,
    "insertedIds" : [
            "Item",
            "Tool",
            "Brush",
            "Scrapper",
            "Stirrer",
            "Coating",
            "Finish",
            "Paint",
            "Exterior",
            "Interior"
    ]
}
```

From here queries can be performed based on parent structure.

```shell
db.items.find({parent: "Tool"})
```

```shell
{ "_id" : "Brush", "parent" : "Tool" }
{ "_id" : "Scrapper", "parent" : "Tool" }
{ "_id" : "Stirrer", "parent" : "Tool" }
```

```shell
db.items.findOne({_id: "Exterior"}).parent
```

Result

```shell
Paint
```

Create an index for faster searching. This creates an ascending index.

```shell
db.items.createIndex({parent: 1})
```

Result

```shell
{
        "createdCollectionAutomatically" : false,
        "numIndexesBefore" : 1,
        "numIndexesAfter" : 2,
        "ok" : 1
}
```

## Advanced case (Optional)

The `$graphLookup` operator can be used to do subtree queries.

```shell
db.items.aggregate([
    {
        $graphLookup: {
            from: "items",
            startWith: "$parent",
            connectFromField: "parent",
            connectToField: "_id",
            as: "hierarchy"
        }
    },
    {
        $match: {
            _id: "Interior"
        }
    }
])
```

Result

```shell
{ "_id" : "Interior", "parent" : "Paint", "hierarchy" : [ { "_id" : "Item", "parent" : null }, { "_id" : "Paint", "parent" : "Coating" }, { "_id" : "Coating", "parent" : "Item" } ] }
```

This lookup query is similar to a self join. It recursively searches the `items` collection and for each document, matches the `_id` field to the `parent` field. If there is a match it adds the document to the `hierarchy` field of the result document. The `$match` stage searches the full results for any document with an `_id` of "Interior". If the `$match` stage is removed you will get the full `$graphLookup` results.

## Child References

Child references are similar to [Parent References](#parent-references), but instead of a single value in the child, it is usually and array of all direct children.

![Modeling Tree Structure](./imgs/tree-structure.png)

Drop the current collection

```shell
db.items.drop()
```

Insert the new documents

```shell
db.items.insertMany([
    {_id: "Item", children: ["Tool", "Coating"]},
    {_id: "Tool", children: ["Brush", "Scrapper", "Stirrer"]},
    {_id: "Brush", children: []},
    {_id: "Scrapper", children: []},
    {_id: "Stirrer", children: []},
    {_id: "Coating", children: ["Finish", "Paint"]},
    {_id: "Finish", children: []},
    {_id: "Paint", children: ["Exterior", "Interior"]},
    {_id: "Exterior", children: []},
    {_id: "Interior", children: []}
])
```

Results

```shell
{
    "acknowledged" : true,
    "insertedIds" : [
            "Item",
            "Tool",
            "Brush",
            "Scrapper",
            "Stirrer",
            "Coating",
            "Finish",
            "Paint",
            "Exterior",
            "Interior"
    ]
}
```

After the documents are inserted queries similar to parent structure can be performed.

## Array of Ancestors

Array of ancestors is similar to other tree structures only the documents container a list of all ancestors.

![Modeling Tree Structure](./imgs/tree-structure.png)

Drop current collection.

```shell
db.items.drop()
```

```shell
db.items.insertMany([
    {_id: "Item", ancestors: null},
    {_id: "Tool", ancestors: ["Item"]},
    {_id: "Brush", ancestors: ["Tool", "Item"]},
    {_id: "Scrapper", ancestors: ["Tool", "Item"]},
    {_id: "Stirrer", ancestors: ["Tool", "Item"]},
    {_id: "Coating", ancestors: ["Item"]},
    {_id: "Finish", ancestors: ["Coating", "Item"]},
    {_id: "Paint", ancestors: ["Coating", "Item"]},
    {_id: "Exterior", ancestors: ["Paint", "Coating", "Item"]},
    {_id: "Interior", ancestors: ["Paint", "Coating", "Item"]}
])
```

Result

```shell
{
    "acknowledged" : true,
    "insertedIds" : [
            "Item",
            "Tool",
            "Brush",
            "Scrapper",
            "Stirrer",
            "Coating",
            "Finish",
            "Paint",
            "Exterior",
            "Interior"
    ]
}
```

Again similar queries can be done as with the other tree structures.

## Materialized Paths

`Materialized Paths` pattern stores the documents ancestor path as a delimited string. `Materialized Paths` do require more processing to use the value stored, but do allow for the use of `regex` to query by partial path.

Drop the current collection

```shell
db.items.drop()
```

Insert the new docs

```shell
db.items.insertMany([
    {_id: "Item", path: null},
    {_id: "Tool", path: ",Item,"},
    {_id: "Brush", path: ",Item,Tool,"},
    {_id: "Scrapper", path: ",Item,Tool,"},
    {_id: "Stirrer", path: ",Item,Tool,"},
    {_id: "Coating", path: ",Item,"},
    {_id: "Finish", path: ",Item,Coating,"},
    {_id: "Paint", path: ",Item,Coating,"},
    {_id: "Exterior", path: ",Item,Coating,Paint,"},
    {_id: "Interior", path: ",Item,Coating,Paint,"}
])
```

Results

```shell
{
        "acknowledged" : true,
        "insertedIds" : [
                "Item",
                "Tool",
                "Brush",
                "Scrapper",
                "Stirrer",
                "Coating",
                "Finish",
                "Paint",
                "Exterior",
                "Interior"
        ]
}
```

Retrieve the whole tree

```shell
db.items.find().sort({path: 1})
```

Results

```shel
{ "_id" : "Item", "path" : null }
{ "_id" : "Tool", "path" : ",Item," }
{ "_id" : "Coating", "path" : ",Item," }
{ "_id" : "Finish", "path" : ",Item,Coating," }
{ "_id" : "Paint", "path" : ",Item,Coating," }
{ "_id" : "Exterior", "path" : ",Item,Coating,Paint," }
{ "_id" : "Interior", "path" : ",Item,Coating,Paint," }
{ "_id" : "Brush", "path" : ",Item,Tool," }
{ "_id" : "Scrapper", "path" : ",Item,Tool," }
{ "_id" : "Stirrer", "path" : ",Item,Tool," }
```

Find descendants

```shell
db.items.find({path: /,Tool,/})
```

Results

```shell
{ "_id" : "Brush", "path" : ",Item,Tool," }
{ "_id" : "Scrapper", "path" : ",Item,Tool," }
{ "_id" : "Stirrer", "path" : ",Item,Tool," }
```

## Nested Sets

Nested Sets is an advanced used querying subtrees. Nested sets considers each document as a stop on a round trip. Each document is visited twice on a round true, 1 for initial stop (left), 2. for return trip (right).

Nested sets offer fast and efficient subtree queries, but make it very difficult to modify the structure. This pattern is best used for static trees.

![Modeling Tree Structure](./imgs/tree-structure.png)

Set Stops

- Item - 1,20
- Tool - 2,9
- Brush - 3,4
- Scrapper - 5,6
- Stirrer - 7,8
- Coating - 10, 19
- Finish - 11,12
- Paint - 13, 18
- Exterior - 14, 15
- Interior - 16, 17

Drop the current collection

```shell
db.items.drop()
```

Insert the items into the database

```shell
db.items.insertMany([
    {_id: "Item", parent: null, left: 1, right: 20},
    {_id: "Tool", parent: "Item", left: 2, right: 9},
    {_id: "Brush", parent: "Tool", left: 3, right: 4},
    {_id: "Scrapper", parent: "Tool", left: 5, right: 6},
    {_id: "Stirrer", parent: "Tool", left: 7, right: 8},
    {_id: "Coating", parent: "Item", left: 10, right: 19},
    {_id: "Finish", parent: "Coating", left: 11, right: 12},
    {_id: "Paint", parent: "Coating", left: 13, right: 18},
    {_id: "Exterior", parent: "Paint", left: 14, right: 15},
    {_id: "Interior", parent: "Paint", left: 16, right: 17}
])
```

Results

```shell
{
        "acknowledged" : true,
        "insertedIds" : [
                "Item",
                "Tool",
                "Brush",
                "Scrapper",
                "Stirrer",
                "Coating",
                "Finish",
                "Paint",
                "Exterior",
                "Interior"
        ]
}
```

Subtree queries can now be performed by binding to the left and right values

```shell
var toolsTree = db.items.findOne({_id: 'Tool'})
db.items.find({left: {$gt: toolsTree.left}, right: {$lt: toolsTree.right}})
```

Result

```shell
{ "_id" : "Brush", "parent" : "Tool", "left" : 3, "right" : 4 }
{ "_id" : "Scrapper", "parent" : "Tool", "left" : 5, "right" : 6 }
{ "_id" : "Stirrer", "parent" : "Tool", "left" : 7, "right" : 8 }
```

Observe that the correct subtree was retrieved since the query binds to the left and right values of the `Tool` document.
