# MongoDB Activity

Complete the following using MongoDB.

### 1) Insert 

Insert the following documents into a movies collection.

    ```
    [
    {
    title : "Fight Club",
    writer : "Chuck Palahniuk",
    year : 1999,
    actors : [
      "Brad Pitt",
      "Edward Norton"
    ]
    },
    {
    title : "Pulp Fiction",
    writer : "Quentin Tarantino",
    year : 1994,
    actors : [
      "John Travolta",
      "Uma Thurman"
    ]
    },
    {
    title : "Inglorious Basterds",
    writer : "Quentin Tarantino",
    year : 2009,
    actors : [
      "Brad Pitt",
      "Diane Kruger",
      "Eli Roth"
    ]
    },
    {
    title : "The Hobbit: An Unexpected Journey",
    writer : "J.R.R. Tolkein",
    year : 2012,
    franchise : "The Hobbit"
    },
    {
    title : "The Hobbit: The Desolation of Smaug",
    writer : "J.R.R. Tolkein",
    year : 2013,
    franchise : "The Hobbit"
    }
    ]

    ```

### 2) Query / Find Documents

Query the movies collection to:

- get all documents
- get all documents with writer set to "Quentin Tarantino"
- get all documents where actors include "Brad Pitt"
- get all documents with franchise set to "The Hobbit"
- get all movies released in the 90s
- get all movies released before the year 2000 or after 2010



### 3) Update Documents

- Add a synopsis to "The Hobbit: An Unexpected Journey"
    ```
    "A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug."
    ```

- Add a synopsis to "The Hobbit: The Desolation of Smaug"
    ```
    "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring."
    ```

- Add an actor named "Samuel L. Jackson" to the movie "Pulp Fiction"


### 4) Text Search

- Find all movies that have a synopsis that contains the word "Bilbo"
- Find all movies that have a synopsis that contains the word "Gandalf"
- Find all movies that have a synopsis that contains the word "Bilbo" and not the word "Gandalf"
- Find all movies that have a synopsis that contains the word "dwarves" or "hobbit"
- Find all movies that have a synopsis that contains the word "gold" and "dragon"


### 5) Delete Documents

- Delete the movie "Pee Wee Herman's Big Adventure"
- Delete the movie "Avatar"