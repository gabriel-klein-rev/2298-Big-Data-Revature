# Overview

This document offers explanations and demonstrations of modeling relationships for documents in MongoDB.

# References

- [MongoDB Docs Relationships](https://docs.mongodb.com/manual/applications/data-models/)

# Prequisites

- [Data Modeling](./data-modeling.md)

# Data Modeling Relationships

A key concern to data modeling is determining how an application represents relationships between entities. Entity relationships fall under 3 types.

- [One-To-One](#one-to-one)
- [One-To-Many](#one-to-many)
- Many-To-Many

# One-To-One

`One-To-One` relationships are view as a singular relationship between entities. Enity X has a singular relationship to Entity Y.

Consider the following

```javascript
// provider document
{
    _id: <ObjectId1>,
    name: 'Behr Paints',
    contactName: 'Van Gogh',
    contactEmail: 'van.gogh@behr.com',
    contactPhone: '123-456-7890',
    contactExt: '1234'
}

// paint document
{
    _id: <ObjectId2>,
    colorName: 'Bone White',
    color: 'e4d4ba',
    finish: 'matte',
    price: 3
}
```

With this setup, how does one model a relationship which follows this statement. **One Paint has One Provider**.

## Embedded Document Pattern

Embedded document pattern is a most commonly used when data is frequently queried together. If it is assumed that `Provider` data is always or frequently viewed with a `Paint` datum then it would be good to use this pattern to avoid costly document joins.

Embedded Documents

```javascript
{
    _id: <ObjectId1>,
    colorName: 'Bone White',
    color: 'e4d4ba',
    price: 3,
    finish: 'matte',
    provider: {
        name: 'Behr Paints',
        contactName: 'Van Gogh',
        contactEmail: 'van.gogh@behr.com',
        contactPhone: '123-456-7890',
        contactExt: '1234'
    }
}
```

Here the `Provider` data is embedded as a child document into the parent `Paint` document.

## Subset Pattern

A potential problem with the `embedded document pattern` is document size. The `embedded document pattern` could lead to large document size and documents that contain data that isn't being used by the application at the time of query. The extra data can lead to excess server load and slow read operations.

The `subset pattern` divides the data into multiple sets that contain the most common data relevant to a document. The `subset pattern` is a normalized data pattern where documents reference each related document through some means of linking.

```javascript
// provider document
{
    _id: <ObjectId1>,
    name: 'Behr Paints',
    contactName: 'Van Gogh',
    contactEmail: 'van.gogh@behr.com',
    contactPhone: '123-456-7890',
    contactExt: '1234'
}

// paint document embedded
{
    _id: <ObjectId2>,
    colorName: 'Bone White',
    color: 'e4d4ba',
    price: 3,
    finish: 'matte'
    provider: {
        provider_id: <ObjectId1>,
        name: 'Behr Paints'
    }
}
```

Here the data is separated into multiple document and the pattern works if we make this assumption. `Paint` contains only data that will be used together most often and `Provider` contains all data relevant to the provider. Observer that `Paint` contains a subset of `Provider` data.

### Subset Pattern Tradeoff

The subset pattern makes documents smaller becuase they contain data that is more frequently accessed. This lessens the load on the server per request and improves read performance. However, splitting the data will require either multiple requests to fullfil a few data request or a **JOIN** to be performed.

## One-To-Many

A `one-to-many` relationship is modeled through the statement, Entity X has One or Many Entity Y. In MongoDB `one-to-many` relationships can be achieved through.

- Embedded and Subset Patterns
- Referencing

### Embedded One-To-Many

```javascript
// paint document
{
    _id: <ObjectId2>,
    colorName: 'Bone White',
    color: 'e4d4ba',
    price: 3,
    finish: 'matte',
    provider: {
        provider_id: <ObjectId1>,
        name: 'Behr Paints'
    },
    reviews: [
        {
            review_id: 1,
            title: 'Dull is beatiful',
            body: 'Perfect amount of light diffusing matte finish.',
            rating: 5
        },
        ...
        {
            review_id: 1000,
            title: 'Deja View',
            body: 'There is something familiar about this color.',
            rating: 4.5
        },
    ]
}
```

Observer the `Paint` document has a `one-to-many` relationship with **reviews**. One `Paint` a has many **reviews**, In this case, 1000 reviews

### Subset One-To-many

It is easy to see that the `embedded` pattern could grow large very quickly. To use the `subset` pattern in this model the following solution could be applied.

```javascript
// Paint Document
{
    _id: <ObjectId2>,
    colorName: 'Bone White',
    color: 'e4d4ba',
    price: 3,
    finish: 'matte',
    provider: {
        provider_id: <ObjectId1>,
        name: 'Behr Paints'
    },
    reviews: [
        {
            review_id: 1,
            title: 'Dull is beatiful',
            body: 'Perfect amount of light diffusing matte finish.',
            rating: 5
        },
        ...
        {
            review_id: 10,
            title: 'Middle of the road',
            body: 'Neutral is a strength',
            rating: 2.5
        },
    ]
}

// Reviews Collection
    {
    review_id: 1,
    title: 'Dull is beatiful',
    body: 'Perfect amount of light diffusing matte finish.',
    rating: 5
    paint_id: <ObjectId2>
    },
    ...
    ..{
    review_id: 1000,
    title: 'Deja View',
    body: 'There is something familiar about this color.',
    rating: 4.5,
    paint_id: <ObjectId2>
    }
```

The `subset` pattern is applied here by storing a subset of `Review` documents in the `Paint` document. In the example the subset is the first 10 reviews, while all reviews are stored in the `Reviews` collection.

### One-To-Many Referencing

If embedding and subsetting don't meet the needs of the application, then referencing can be applied to model the relationship.

```javascript
// Paint Document
{
    _id: <ObjectId2>,
    colorName: 'Bone White',
    color: 'e4d4ba',
    price: 3,
    finish: 'matte',
    provider: {
        provider_id: <ObjectId1>,
        name: 'Behr Paints'
    },
    reviews: [1, 2, 3, 4, ..., 1000]
}
// Reviews Collection
{
review_id: 1,
title: 'Dull is beatiful',
body: 'Perfect amount of light diffusing matte finish.',
rating: 5
paint_id: <ObjectId2>
},
...
..{
review_id: 1000,
title: 'Deja View',
body: 'There is something familiar about this color.',
rating: 4.5,
paint_id: <ObjectId2>
}
```

With referencing applied the `Paint` document contains an array of `Review` ids.

## Many-To-Many

A `many-to-many` relationship is a complex relationship where Many Entity X have Many Entity Y. Out of context, in a SQL database it takes 3 entities to represent this type of relationship: Entity X, Entity Y, and Entity X_Y. Entity X_Y hold the data relevant to the relationship between any Entity X and Entity Y.

### Decomposing the relationship

`Many-To-Many` relationships are really just 2 `one-to-many` relationships. One Entity X to Many Entity Y and One Entity Y to Many Entity X. Modeling this in SQL is difficult, but in MongoDB its simple.

```javascript
// Tag collection
{
    tag_id: 1,
    tag: 'premium',
    paints: [1, 2, 50, ..., 1000]
}
{
    tag_id: 2,
    tag: 'exterior',
    paints: [43, 120, 78]
}
...
{
    tag_id: 100,
    tag: 'favorite',
    paints: [27, 11, 36]
}

// Paint Document
{
    _id: <ObjectId2>,
    colorName: 'Bone White',
    color: 'e4d4ba',
    price: 3,
    finish: 'matte',
    provider: {
        provider_id: <ObjectId1>,
        name: 'Behr Paints'
    },
    reviews: [
        {
            review_id: 1,
            title: 'Dull is beatiful',
            body: 'Perfect amount of light diffusing matte finish.',
            rating: 5
        },
        ...
        {
            review_id: 10,
            title: 'Middle of the road',
            body: 'Neutral is a strength',
            rating: 2.5
        },
    ],
    tags: [1, 2, 100]
}
```

Observe that `Tag` documents contain a `one-to-many` relationship with `Paint` documents, through referencing, and `Paint` documents contain a `one-to-many` relationship with `Tag` documents, also through referencing. This is called two-way referencing.

**Note** this example uses referencing, but since the relationship has been decomposed to multiple `one-to-many` relationships `subset` pattern could be used depending on the need of the application.
