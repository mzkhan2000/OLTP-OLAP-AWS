# OLPT to OLAP-data-analytics on AWS
OLPT-to-OLAP-data-analytics on AWS with a use case

![AWS](diagrams/AWS_Architecture_Diagram2.png?raw=true "AWS")

# Note
Data was not properly formatted in CSV so need to clean some data before crawling. 

# Step 01: Upload to S3 

1. Create a bucket with a bucket name for uploading csv datasets. 
2. Create separated folder of each of the csv files in the bucket and name the folder as the table names that will get the data from the data catalog by aws Athena

# Step 02: Create and run a Glue Crawler
A crawler connects to a data store, progresses through a prioritized list of classifiers to determine the schema for your data, and then creates metadata tables in your data catalog.

1. Create a csv classifier that determines the schema of data
2. Create a IAM role for this job (with read and write access to S3)
3. Adding Classifiers to a Crawler
4. Create a database to get the data from the data catalog
5. This will populate data to AWS Glue Data Catalog

# Step 03: Explore the data catalog in aws Athena 
Now we can query and exploring database tables in data catalog using aws Athena

```sql
SELECT * FROM "monir-assignar-db"."order" limit 10;
```
```sql
SELECT * FROM "monir-assignar-db"."project";
```

# Step 04: Creating a MySQL DB instance and connecting to MySQL DB instance with MySQL Workbench

1. MySQL DB instance in AWS RDS
2. Creating appropriate security group for inbound traffic is allowed by default
3. Create database schema in mysql workbench using the sql script provided in the test
4. Create a ERD using the schema by reverse engineering and adding primary and foreign keys
5. Create a database schema using the ERD by forward engineering
6. Create a RDS-Mysql connection in AWS Glue, add proopiuate IAM role and test the connection
7. Create a crawler that crawl the databse schema from MySQL database
8. Create a Glue ETL job to load data from glue datacatalogs to RDS Mysql database

[AWS Glue job for ETL process to digest the provided order file into order table in an OLTP schema as shown in the ERD diagram below](Glue-Jobs/Glue-job-for-Order-Table-load-data.py)

[MySQL-Workbench-script for creating OLTP scema in AWS RDS MySQL database instance](MySQL-Workbench-scripts/prd_demo_monir.sql)
  
![ERD](diagrams/monir-ERD.png?raw=true "ERD")

# Step 05: Use AWS Glue DataBrew for data preparation for dimensional modelling

[AWS Glue DataBrew job and recipe for data preparation for dimensional modelling](Glue-DataBrew/original-order-data-anlysis-recipe.json.txt)
  
![DataBrew](diagrams/My-GlueDataBrew-job-small.png?raw=true "DataBrew")

# Step 06: AWS Glue jobs to convert this OLTP database structure to OLAP(Star/Snowflake) database structure for BI/Reporting purpose

Following Jobs have been created...

 1. [AWS Glue ETL Job for creating Fact table and updating schema](Glue-Jobs/Glue-job-for-Fact_order-project.py)
 2. [AWS Glue ETL Job for creating Dimention tables and updating schemas](Glue-Jobs/Glue-job-for-Dim-user-Dim-client-Dim-suppliers.py)

![GLUEJOB1](Images/Glue-Fact-table-creation-jobs.png?raw=true "GLUE JOB for creating a fact table")

AWS Glue ETL Job for creating Fact table and updating schema  [GlueJob01Code](Glue-Jobs/Glue-job-for-Fact_order-project.py)

![GLUEJOB2](Images/Glue-Dimentional-table-creation-jobs.png?raw=true "GLUE JOB for creating fact table")

AWS Glue ETL Job for creating Dimention tables and updating schemas  [GlueJob02Code](Glue-Jobs/Glue-job-for-Dim-user-Dim-client-Dim-suppliers.py)

# Step 07: Load the data from OLTP schema to OLAP schema in Redshift cluster
[SQL script for creating tables with OLAP STAR SCHEMA in Redshift cluster](Redshift-code/Create-tables-in-Redshift.sql)


![OLAP](diagrams/Monir-Assignar-OLAP.png?raw=true "OLAP")
1. attached the redshift cluster with appropriate IAM role (created)
2. create a database schema, database with the SQL file provided in this test. In this case provide primary and foreign key constraints in creating associated tables.

```sql
CREATE TABLE assignar_olap_db.fact_order-project 
(
order_id INT,
client_id BIGINT,
project_id BIGINT,
suppeliers_id INT,
user_id BIGINT,
order_active_status INT,
job_number VARCHAR(100),
po_number VARCHAR(100),
order_status_name VARCHAR(100),
order_start_date DATE,
order_end_date DATE,
order_date_created DATETIME,
order_modified_time DATETIME,
calendar_year DATETIME,
calendar_quarter DATETIME,
calendar_month DATETIME,
project_start_date DATE,
project_end_date DATE,
project_address VARCHAR(255),
project_address_geo POINT,
project_suburb VARCHAR(100),
project_state VARCHAR(50),
project_postcode VARCHAR(10),
project_active_status INT,
project_duration DATETIME,
PRIMARY KEY(order_id),
FOREIGN KEY(client_id) REFERENCES dimention_client(client_id),
FOREIGN KEY(user_id) REFERENCES dimention_user(user_id),
FOREIGN KEY(suppeliers_id) REFERENCES dimention_suppliers(suppliers_id),
  );
```
3. Using the COPY commands to load data from S3 buckets to Redshift created database

```sql
copy assignar_oltp_db.ffa_order
from 's3://assignar-test-db-bucket/upload-original-file/fact_order-project/'
iam_role 'arn:aws:iam::166809146462:role/RED'
region 'us-east-1'
delimiter ','
ignoreheader AS 1
DATEFORMAT AS 'dd/mm/yyyy'
TIMEFORMAT AS 'dd/mm/yyyy hh:mi'
csv;
```
4. Start analysis data using Redshift Query Editor. 


# Step 8. Using OLAP Schema the answers of the following questions by writing SQL queries.

a.	How many Dashboard users have created orders in the year of 2020.

```sql
SELECT COUNT(user_id)
  FROM assignar_olap_db.dimentaion_user
      INNER JOIN assignar_olap_db.fact_order-project ON dimentaion_user.user_id = fact_order-project.user_id
	WHERE fact_order-project.calendar_year = "2020" 
	   AND dimentaion_user.user_label ="Dashboard User";
   ``` 
b.	Which project has been worked on the longest.

```sql
SELECT fact_order-project.project_id
    FROM fact_order-project
    WHERE project_duration = 
        (SELECT max(project_duration) from fact_order-project);
  ```
  
c.	Which client has the largest  Quarter over Quarter growth (number of orders they have completed) in 2020?

```sql
SELECT distinct client_id
from
(
    SELECT client_id, MAX(COUNT(order_id)) as MXorder 
    FROM fact_order-project where calendar_year ="2020"
    GROUP BY client_id, MXorder 
    HAVING count(distinct calendar_quarter) = 4 
) group by client_id
 ```

# Q5. How would you design the load scripts if the frequency of processing changed from batch to real time? 

Batch processing is a common practice for data processing. In a batch architecture, a scheduled extract-transform-load (ETL) process is executed that processes the transactions and transforms them so they can be loaded into their data warehouse. Depends on the business analysts review the data using a reporting tool, the ETL process can be scheduled daily, weekly, or maybe monthly. In AWS cloud environment, Glue jobs can be configured based on the schedules, and AWS lambda function can be created. 

If the frequency of processing changed from batch to real time, and if the organization uses AWS for their data analytics solution, then the streaming data solution with Amazon Kinesis would be a suitable solution, I think. Amazon Kinesis Data Firehose is a good way to load streaming data into AWS. It can capture, transform, and load streaming data into Amazon Kinesis Data Analytics, Amazon S3 and Amazon Redshift. In this solution, Amazon Kinesis Data Firehose first delivers incoming data to your S3 bucket. If data transformation needed AWS Lambda function can be created that enable streaming data transformations in Kinesis Data Firehose. Kinesis Firehose then issues an Amazon Redshift COPY command to load the data from your S3 bucket to your Amazon Redshift cluster. This is a one suitable solution from many of other solutions in AWS real-time data pipeline.

# Q6. How and what kind of monitoring systems would you set up to make sure the data is correct, accurate and available in a timely manner.? 
Aws lambda function that can receive notifications from amazon sns can be set up to make sure the data is correct, accurate and available in a timely manner