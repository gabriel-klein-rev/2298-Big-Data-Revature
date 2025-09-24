
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:
- Describe Database Consistency
- Discuss the importance of database consistency
- Provide examples of strong vs weak consistency

</details>
<details><summary>Description</summary>

## Database Consistency

Database consistency is where all data points within the database system must align in order to be properly read and accepted. Information that does not meet the predefined values within the database will result in consistency errors with the dataset. Any transactions with the database involved in data written to the database must adhere to the database's established rules by developers. This is defined by specific constraints, triggers, variables, cascades, etc, that will all be described in the modules to follow.

While database consistency helps ensure the appropriate format for data written to the database, it does not account for what the data respresents. This means the information entered may match the appropriate format, but doesn't guarantee that the data corresponds with the actual information. 

These rules applied to our data is what keeps databases working smoothly by keeping inconsistent data out, achieving higher accuracy, increasing database space, and improving data retrieval.

## Database Inconsistency

Database consistency also applies to any changes of the data within the system. If one particular object in the database is updated, but also is present in another table in the database, it must be properly updated in all other tables it is present. If this fails, it results in database inconsistency.

Database inconsistency is when any portion of the information is updated in the table, but is not represented in all other tables utilizing that same information.

</details>
<details><summary>Real World Application</summary>

## Database Consistency

Imagine working at the Pennsylvania DMV and you've been asked to work on the database for the new Driver's License. Due to growing population sizes, they've required a new driver's license number to help identify individuals. Your team has determined that every individuals driver's license number must include the following: 1 Alpha + 6 Numerics + 1 Alpha. All driver license numbers are now required to follow this rule, such that "P123456A" is a valid entry consistent with the format mentioned. Any entry that doesn't fit those stipulations, such as "P12345678", would result in error for inconsistent data as it's format is 1 Alpha + 8 Numerics.

## Database Inconsistency

Keeping with the driver's license example, imagine a driver's home address changes. This update must be represented across all tables where that prior address existed. If any table contains the old address, but others contain the new address for the driver would be a prime example of database inconsistency.

</details>
<details><summary>Implementation</summary> 
<br>

Database consistency implementation, which involves specific constraints, triggers, variables, cascades, etc., will be outlined throughout the remaining modules. These elements are established based on the rules set by you as a developer. Always keep in mind, "how is this affecting my data's consistency?" when applying any implementations in the future.

</details>
<details><summary>Summary</summary> 

<br>

Database consistency is vital for accuracy, improved data retrieval and increasing the database space available. 
- Consistency using established rules by the developer allows for consistent data formats
- Consistency does not account for what the data represents
- Consistency ensures that any inconsistent data attempted to be written to the database results in an error

Database inconsistency is when tables that should have matching information is conflicting with one another.


</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
