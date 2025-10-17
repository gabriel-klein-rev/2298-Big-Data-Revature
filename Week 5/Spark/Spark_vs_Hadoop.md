# Cumulative for the  Hadoop vs Spark

## Learning Objectives

- After completing this module, anyone can be able to understand the difference between Hadoop and Spark.


## Description

## Speed 

- Apache spark - Spark is a cluster computing technology developed by Apache. Compared to Hadoop, Apache Spark can run applications up to 100 times faster in memory and 10 times quicker on storage. Spark makes it possible by minimizing the number of reading/writing cycles to disk and storing intermediate data in memory.

- Hadoop MapReduce - As MapReduce reads and writes data to and from the disc, processing performance is slowed.

## Difficulty

- Apache Spark - RDD, or Resilient Distributed Dataset, allows Spark to have a large number of high-level operators, making it simple to programme.

- Hadoop MapReduce - Hadoop MapReduce - Every operation in MapReduce must be manually coded, which makes it extremely challenging to use.

## latency

- Apache Spark – It provides low-latency computing.
  
- Hadoop MapReduce – It is a high latency computing framework.

## Interactive mode

- Apache Spark – It can process data interactively.
  
- Hadoop MapReduce – It doesn’t have an interactive mode.

## Streaming

- Apache Spark – It will process real-time data through Spark Streaming.
  
- Hadoop MapReduce – With MapReduce, we can only process data in batch mode.

## Category

- Apache Spark – It is data analytics engine.
  
- Hadoop MapReduce – MapReduce is basic data processing engine.

## Language Developed

- Apache Spark – It is developed in Scala.
  
- Hadoop MapReduce – It is developed in Java language.

## Latency

- Apache spark - It provides low-latency computing.

- Hadoop MapReduce - It provides high latency computing.

</br>

|     **Factors**    |                      **Hadoop**                      |                                **Spark**                                |
|:------------------:|:-------------------------------------------------------:|:-----------------------------------------------------------------------:|
| _Ease of Use_      | It is difficult to use with no Interactive mode               | Easy to Use and supports interactive mode                               |
| _Data processing_  | Data Processing is ideal for batch processing           | Can handle all data processing requirements (batch, graph etc.)         |
| _Performance_      | Faster than traditional system                          | Runs 100 times faster in-memory and 10 times faster on disk than Hadoop |
| _Failure Recovery_ | Resume where it left off when it restarts               | start all over from beginning when it restarts                          |
| _Security_         | More secure as it uses all Hadoop security capabilities | less secure as the security is set to "OFF" by default                  |
| _Cost_             | MapReduce is a cheaper option in terms of cost.         | expensive due to its in-memory processing power and RAM requirement     |
| _Scheduler_        | Dependent on external job scheduler like Oozie          | can schedule all its tasks by itself                                    |



