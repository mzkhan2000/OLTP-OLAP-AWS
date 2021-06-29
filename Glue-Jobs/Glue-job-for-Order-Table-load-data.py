import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "assignartestdb", table_name = "ffa_order_csv", transformation_ctx = "DataSource0"]
## @return: DataSource0
## @inputs: []
DataSource0 = glueContext.create_dynamic_frame.from_catalog(database = "assignartestdb", table_name = "ffa_order_csv", transformation_ctx = "DataSource0")
## @type: ApplyMapping
## @args: [mappings = [("id", "long", "id", "long"), ("active", "long", "active", "long"), ("job_number", "string", "job_number", "string"), ("po_number", "string", "po_number", "string"), ("client_id", "long", "client_id", "long"), ("project_id", "long", "project_id", "long"), ("job_description", "string", "job_description", "string"), ("shift_duration", "string", "shift_duration", "string"), ("start_date", "string", "start_date", "string"), ("end_date", "string", "end_date", "string"), ("comments", "string", "comments", "string"), ("user_id", "long", "user_id", "long"), ("date_created", "string", "date_created", "string"), ("modified_time", "string", "modified_time", "string"), ("status_id", "long", "status_id", "long"), ("supplier_id", "long", "supplier_id", "long")], transformation_ctx = "Transform0"]
## @return: Transform0
## @inputs: [frame = DataSource0]
Transform0 = ApplyMapping.apply(frame = DataSource0, mappings = [("id", "long", "id", "long"), ("active", "long", "active", "long"), ("job_number", "string", "job_number", "string"), ("po_number", "string", "po_number", "string"), ("client_id", "long", "client_id", "long"), ("project_id", "long", "project_id", "long"), ("job_description", "string", "job_description", "string"), ("shift_duration", "string", "shift_duration", "string"), ("start_date", "string", "start_date", "string"), ("end_date", "string", "end_date", "string"), ("comments", "string", "comments", "string"), ("user_id", "long", "user_id", "long"), ("date_created", "string", "date_created", "string"), ("modified_time", "string", "modified_time", "string"), ("status_id", "long", "status_id", "long"), ("supplier_id", "long", "supplier_id", "long")], transformation_ctx = "Transform0")
## @type: DataSink
## @args: [database = "assignardb", table_name = "order", transformation_ctx = "DataSink0"]
## @return: DataSink0
## @inputs: [frame = Transform0]
DataSink0 = glueContext.write_dynamic_frame.from_catalog(frame = Transform0, database = "assignardb", table_name = "order", transformation_ctx = "DataSink0")
job.commit()