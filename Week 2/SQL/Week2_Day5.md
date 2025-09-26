## Indexing
Indexing is a way of speeding up lookups on tables. We index columns so that lookups based on that column can complete quicker. This effeciency in lookups does cost us elsewhere though. We ned to dedicate extra space to hold the index, and we incur a speed cost when doing insertions, updates, and deletions to that column as the indexes need to be maintained.
 - Indexes create a separate structure that points to rows in the main table
 - They speed up SELECT operations but can slow down INSERT, UPDATE, and DELETE operations
 - Indexes consume additional storage space
 - MySQL automatically creates an index for PRIMARY KEY and UNIQUE constraints

### Primary (Clustered) Index
```SQL
CREATE TABLE users (
    id INT PRIMARY KEY,  -- Primary index automatically created
    name VARCHAR(100),
    email VARCHAR(100)
);
```

### Unique Index (MySQL)
```SQL
-- Create unique index during table creation
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE  -- Unique index created
);

-- Add unique index to existing table
ALTER TABLE users ADD UNIQUE INDEX idx_email (email);
-- or
CREATE UNIQUE INDEX idx_email ON users(email);
```

### Regular Index
```SQL
-- Create index during table creation
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50),
    INDEX idx_name (name),        -- Single column index
    INDEX idx_name_city (name, city)  -- Composite index
);

-- Add index to existing table
CREATE INDEX idx_city ON users(city);
-- or
ALTER TABLE users ADD INDEX idx_city (city);
```
### Fulltext Index
 - Used for full-text searches
 - Works with CHAR, VARCHAR, and TEXT columns
```SQL
CREATE TABLE articles (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    content TEXT,
    FULLTEXT(title, content)
);

-- Usage
SELECT * FROM articles 
WHERE MATCH(title, content) AGAINST('database optimization');
```

### When to Use Indexes
Good Candidates for Indexing:
 - Columns frequently used in WHERE clauses
 - Columns used in JOIN conditions
 - Columns used in ORDER BY clauses
 - Foreign key columns
 - Columns with high selectivity (many unique values)

Poor Candidates for Indexing:
 - Small tables (under 1000 rows?)
 - Columns with low selectivity (few unique values like boolean columns)
 - Tables with high INSERT/UPDATE/DELETE activity

## Views
A view in MySQL is a virtual table based on the result of a SQL statement. It contains rows and columns just like a real table, but the data is dynamically generated from one or more underlying tables when the view is queried. Think of a view as a "saved query" that you can treat like a table.

```SQL
-- Create sample tables
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    grade_level INT,
    enrollment_date DATE
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100),
    credits INT,
    department VARCHAR(50)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    semester VARCHAR(20),
    grade DECIMAL(3,2),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Insert sample data
INSERT INTO students VALUES 
(1, 'John', 'Smith', 'john.smith@email.com', 12, '2023-09-01'),
(2, 'Sarah', 'Johnson', 'sarah.j@email.com', 11, '2023-09-01'),
(3, 'Mike', 'Brown', 'mike.brown@email.com', 12, '2023-09-01'),
(4, 'Emily', 'Davis', 'emily.d@email.com', 10, '2024-01-15');

INSERT INTO courses VALUES
(1, 'Advanced Mathematics', 4, 'Mathematics'),
(2, 'English Literature', 3, 'English'),
(3, 'Physics', 4, 'Science'),
(4, 'World History', 3, 'History');

INSERT INTO enrollments VALUES
(1, 1, 1, 'Fall 2024', 3.8),
(2, 1, 2, 'Fall 2024', 3.5),
(3, 2, 1, 'Fall 2024', 3.9),
(4, 2, 3, 'Fall 2024', 3.7),
(5, 3, 4, 'Fall 2024', 3.2),
(6, 4, 2, 'Spring 2024', 3.6);

-- Create a view showing only student contact information
CREATE VIEW student_contacts AS
SELECT 
    student_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    email,
    grade_level
FROM students;

-- Query the view
SELECT * FROM student_contacts;
```

## Set Operations
If we think of `JOIN` as combining columns horizontally, we can conceptualize set operations like `UNION` to be combining rows verttically. These operations are all a matter of combining two results sets into a single result set in some fashion. 
 - `UNION` - Combine both sets
 - `INTERSECT` - Combine both sets and include only those rows which are found in both sets
 - `EXCEPT` - Subtract the second set from the first set and return what remains
`INTERSECT` and `EXCEPT` are now supported by MySQL even if MySQL Workbench doesn't yet realize. You can ignore intellisense warnings about those two, the query will run.

#### UNION
```SQL
-- Get all customer names from two different tables
SELECT customer_name FROM customers_north
UNION
SELECT customer_name FROM customers_south;
```
#### INTERSECT
```SQL
SELECT student_id, student_name FROM students_math
INTERSECT
SELECT student_id, student_name FROM students_science;
```
#### EXCEPT
```SQL
SELECT student_id, student_name FROM students_math
EXCEPT
SELECT student_id, student_name FROM students_science;
```

## Normalization
Normalization is "opinionation", it's a set of best practices that allow us to best leverage optimizations put in place by the authors of the database engine.  

#### Dependant
 - honorific: Miss (This is dependant on marital_status. If this person were married it would be 'Mrs')
 - first_name: Danielle  
 - last_name: Plummer  
 - full_name: Miss Danielle Plummer (This is dependant on first_name, last_name, as well as honorific, and because honorific is dependant on marital_status, this is also transitively dependant on marital_status.)
 - marital_status: unmarried  

full_name is dependant on honorific, honorific is dependant on marital_status, which means that full_name is transitively dependant on marital_status  
A -> B, B -> C, and so A -> C (transitively)  

1NF
 - Every row can be uniquely identified
 - Atomicity - The data should be as indivisible or "granular" as possible.
   - full_name: Kyle Plummer -> first_name: Kyle, last_name: Plummer
   - 123 street ave
 - No repeated data

2NF (only applies to tables with composite keys)
 - Must be in 1NF
 - Eliminate partial dependencies
 - Non-key columns must depend on the entire primary key, not just part of it (the primary key)

3NF
 - Must be in 2NF
 - No transitive dependencies
 - Non-key attributes should depend only on the primary key or nothing???

"The key, the whole key, and nothing but they key."

There are additional normal forms above 3 that only university professors care about.




## Code Challenges
### [The Pads](https://www.hackerrank.com/challenges/the-pads/problem)
```SQL
/*Enter your query here.*/
SELECT CONCAT(name, '(', SUBSTRING(occupation, 1, 1), ')') 
FROM occupations
ORDER BY CONCAT(name, '(', SUBSTRING(occupation, 1, 1), ')');

SELECT CONCAT('There are a total of ', COUNT(occupation),' ',LCASE(occupation),'s.')
FROM occupations
GROUP BY occupation
ORDER BY COUNT(occupation)
```


### Binary Search
#### Python
```Python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```
#### Recursive Python
```Python
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
```
