# MongoDB Review

1.  What does BASE stand for?

    a.  Basic Availability, Soft-state, Eventual consistency

2.  What is a database in Mongo?

    a.  A database in Mongo is a grouping of unstructured data in JSON
        format

3.  What is a collection?

    a.  Equates to a table

4.  What is a document?

    a.  Equates to a row

5.  What rules does Mongo enforce about the structure of documents
    inside a collection?

6.  What is a distributed application? A distributed data store?

7.  What is High Availability? How is it achieved in Mongo?

    a.  High availability is the ability of a system to operate
        continuously without failing for a designated period of time.
        Mongo achieves it through replica sets

8.  What is Scalability? How is it achieved in Mongo?

    a.  Scalability is the ability of a database to grow in size. It is
        achieved both vertically and horizontally in MongoDB.
        Horizontally through sharding and replica sets

9.  Explain replica sets and sharding

10. What are NoSQL databases? What are the different types of NoSQL
    databases?

    a.  NoSQL is a type of nonrelational database query language.

    b.  Wide column, document, key-value, graph

11. What kind of NoSQL database MongoDB is?

    a.  It is a document database

12. Which are the most important features of MongoDB?

    a.  Can handle unstructured data

13. What is a Namespace in MongoDB?

    a.  The name of the collection, including the database.

14. Which all languages can be used with MongoDB?

15. Compare SQL databases and MongoDB at a high level.

    a.  SQL databases are structured while MongoDB is used to save
        unstructured data

16. How is MongoDB better than other SQL databases?

    a.  It is much faster than other SQL databases

    b.  Much more scalable

    c.  More flexible

17. Does MongoDB support foreign key constraints?

    a.  No

18. Does MongoDB support ACID transaction management and locking
    functionalities?

    a.  YES, but not innately

19. How can you achieve primary key - foreign key relationships in
    MongoDB?

    a.  By embedding a document inside another

20. When should we embed one document within another in MongoDB?

    a.  When we want to relate the two documents

21. Mention what is Objecld composed of?

    i.  4-byte timestamp value representing object's creation

    ii. 5-byte random value

    iii. 3-byte incrementing counter


# Linux Commands

### pwd
    - print absolute path of present working directory
    - Absolute Path
        - Path to directory or file starting from the root directory
    - Relative path
        - Path to directory or file starting from the pwd
    - Home directory
        - Denoted with ~
    - Root directory
        - Uppermost parennt directory in fs
        - Denoted with /

### ls
    - list files/directories in pwd
    - commonly used with -al

### cd
    - change directory
    - followed by path to wanted directory
        - Can use absolute path or relative path

### mkdir [directory name]
    - Create new directory

### echo [text ]
    - prints text to console
    - Output can be redirected with > or >>

### cat [file name]
    - Concatenate file
    - Prints file contents to console

### cp [file name] [new location]
    - copy a file

### mv [file name] [location/new file name]
    - move a file
    - can be used to rename a file

### rm [file name]
    - remove file
    - can be used with -r to recursively delete a directory

### grep [pattern ] [file name]
    - Search a file for a pattern and return the matching lines
    - -i
        - Case insensitive
    - -c
        - Count of lines that match

### chmod
    - Changing permissions on a file

# Computer Basics

### Processor
    - Brain of your computer
    - Runs commands written in machine code

### Storage (HDD, SSD)
    - Long term memory
    - Only part of your computer that preserves data after you shut it down

### Memory (RAM - Random Access Memory)
    - Short term memory
    - Fast
    - Where inputs/outputs of commands are stored, and where your running programs are "stored"

### OS (operating system, Windows, MacOS, Linux)
    - Linux
    - Many big-data tools work only/better on Unix-like OS

### Kernel
    - Core of our OS
    - Controls all tasks of the system

### Terminal/Shell/CLI
    - Interface that allows us to communicate with the kernel

### Node
    - Single machine inside a cluster

### Cluster 
    - Network of multiple systems (nodes) that work together as a single unit

### VM (virtual machine)
    - Like running an OS on hardware, but on virtual "hardware"
    - Resources are allocated from actual hardware remotely to run a VM