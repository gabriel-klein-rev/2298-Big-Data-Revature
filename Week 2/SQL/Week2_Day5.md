### Normalization
Normalization is "opinionation", it's a set of best practices that allow us to best leverage optimizations put in place by the authors of the database engine.

honorific: Mrs
first_name: Danielle
last_name: Plummer
full_name: Mrs Danielle Plummer (This column is dependant on both the other columns. We concatinate first and last into full)
marital_status: Married

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





