import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "monir-assignar-db", table_name = "order", transformation_ctx = "DataSource0"]
## @return: DataSource0
## @inputs: []
DataSource0 = glueContext.create_dynamic_frame.from_catalog(database = "monir-assignar-db", table_name = "order", transformation_ctx = "DataSource0")
## @type: DataSource
## @args: [database = "monir-assignar-db", table_name = "order_status", transformation_ctx = "DataSource2"]
## @return: DataSource2
## @inputs: []
DataSource2 = glueContext.create_dynamic_frame.from_catalog(database = "monir-assignar-db", table_name = "order_status", transformation_ctx = "DataSource2")
## @type: ApplyMapping
## @args: [mappings = [("status_id", "long", "(right) status_id", "long"), ("status_name", "string", "(right) status_name", "string")], transformation_ctx = "Transform0"]
## @return: Transform0
## @inputs: [frame = DataSource2]
Transform0 = ApplyMapping.apply(frame = DataSource2, mappings = [("status_id", "long", "(right) status_id", "long"), ("status_name", "string", "(right) status_name", "string")], transformation_ctx = "Transform0")
## @type: Join
## @args: [columnConditions = ["="], joinType = left, keys2 = ["(right) status_id"], keys1 = ["status_id"], transformation_ctx = "Transform1"]
## @return: Transform1
## @inputs: [frame1 = DataSource0, frame2 = Transform0]
DataSource0DF = DataSource0.toDF()
Transform0DF = Transform0.toDF()
Transform1 = DynamicFrame.fromDF(DataSource0DF.join(Transform0DF, (DataSource0DF['status_id'] == Transform0DF['(right) status_id']), "left"), glueContext, "Transform1")
## @type: DataSource
## @args: [database = "monir-assignar-db", table_name = "project", transformation_ctx = "DataSource1"]
## @return: DataSource1
## @inputs: []
DataSource1 = glueContext.create_dynamic_frame.from_catalog(database = "monir-assignar-db", table_name = "project", transformation_ctx = "DataSource1")
## @type: ApplyMapping
## @args: [mappings = [("project_id", "long", "(right) project_id", "long"), ("client_id", "long", "(right) client_id", "long"), ("start_date", "string", "(right) start_date", "string"), ("end_date", "string", "(right) end_date", "string"), ("email", "string", "(right) email", "string"), ("address", "string", "(right) address", "string"), ("address_geo", "string", "(right) address_geo", "string"), ("suburb", "string", "(right) suburb", "string"), ("state", "string", "(right) state", "string"), ("postcode", "string", "(right) postcode", "string"), ("external_id", "string", "(right) external_id", "string"), ("active", "long", "(right) active", "long"), ("parent_id", "long", "(right) parent_id", "long"), ("project_duration", "string", "(right) project_duration", "string")], transformation_ctx = "Transform3"]
## @return: Transform3
## @inputs: [frame = DataSource1]
Transform3 = ApplyMapping.apply(frame = DataSource1, mappings = [("project_id", "long", "(right) project_id", "long"), ("client_id", "long", "(right) client_id", "long"), ("start_date", "string", "(right) start_date", "string"), ("end_date", "string", "(right) end_date", "string"), ("email", "string", "(right) email", "string"), ("address", "string", "(right) address", "string"), ("address_geo", "string", "(right) address_geo", "string"), ("suburb", "string", "(right) suburb", "string"), ("state", "string", "(right) state", "string"), ("postcode", "string", "(right) postcode", "string"), ("external_id", "string", "(right) external_id", "string"), ("active", "long", "(right) active", "long"), ("parent_id", "long", "(right) parent_id", "long"), ("project_duration", "string", "(right) project_duration", "string")], transformation_ctx = "Transform3")
## @type: Join
## @args: [columnConditions = ["="], joinType = outer, keys2 = ["(right) project_id"], keys1 = ["project_id"], transformation_ctx = "Transform4"]
## @return: Transform4
## @inputs: [frame1 = Transform1, frame2 = Transform3]
Transform1DF = Transform1.toDF()
Transform3DF = Transform3.toDF()
Transform4 = DynamicFrame.fromDF(Transform1DF.join(Transform3DF, (Transform1DF['project_id'] == Transform3DF['(right) project_id']), "outer"), glueContext, "Transform4")
## @type: DropFields
## @args: [paths = ["(right) external_id", "quarter", "po_number", "job_description", "shift_duration", "comments", "status_id", "(right) status_id", "(right) project_id", "(right) client_id", "(right) email"], transformation_ctx = "Transform2"]
## @return: Transform2
## @inputs: [frame = Transform4]
Transform2 = DropFields.apply(frame = Transform4, paths = ["(right) external_id", "quarter", "po_number", "job_description", "shift_duration", "comments", "status_id", "(right) status_id", "(right) project_id", "(right) client_id", "(right) email"], transformation_ctx = "Transform2")
## @type: ApplyMapping
## @args: [mappings = [("id", "long", "order_id", "long"), ("active", "long", "order_active_status", "long"), ("job_number", "string", "job_number", "string"), ("client_id", "long", "client_id", "long"), ("project_id", "long", "project_id", "long"), ("start_date", "string", "order_start_date", "string"), ("end_date", "string", "order_end_date", "string"), ("user_id", "long", "user_id", "long"), ("date_created", "string", "order_date_created", "string"), ("modified_time", "string", "order_modified_time", "string"), ("supplier_id", "long", "supplier_id", "long"), ("calendar_quarter", "long", "order_calendar_quarter", "long"), ("calendar_year", "long", "order_calendar_year", "long"), ("calendar_month", "long", "order_calendar_month", "long"), ("(right) status_name", "string", "order_status_name", "string"), ("(right) start_date", "string", "project_start_date", "string"), ("(right) end_date", "string", "project_ end_date", "string"), ("(right) address", "string", "project_ address", "string"), ("(right) address_geo", "string", "project_ address_geo", "string"), ("(right) suburb", "string", "project_ suburb", "string"), ("(right) state", "string", "project_ state", "string"), ("(right) postcode", "string", "project_ postcode", "string"), ("(right) active", "long", "project_ active", "long"), ("(right) project_duration", "string", "project_duration", "string")], transformation_ctx = "Transform5"]
## @return: Transform5
## @inputs: [frame = Transform2]
Transform5 = ApplyMapping.apply(frame = Transform2, mappings = [("id", "long", "order_id", "long"), ("active", "long", "order_active_status", "long"), ("job_number", "string", "job_number", "string"), ("client_id", "long", "client_id", "long"), ("project_id", "long", "project_id", "long"), ("start_date", "string", "order_start_date", "string"), ("end_date", "string", "order_end_date", "string"), ("user_id", "long", "user_id", "long"), ("date_created", "string", "order_date_created", "string"), ("modified_time", "string", "order_modified_time", "string"), ("supplier_id", "long", "supplier_id", "long"), ("calendar_quarter", "long", "order_calendar_quarter", "long"), ("calendar_year", "long", "order_calendar_year", "long"), ("calendar_month", "long", "order_calendar_month", "long"), ("(right) status_name", "string", "order_status_name", "string"), ("(right) start_date", "string", "project_start_date", "string"), ("(right) end_date", "string", "project_ end_date", "string"), ("(right) address", "string", "project_ address", "string"), ("(right) address_geo", "string", "project_ address_geo", "string"), ("(right) suburb", "string", "project_ suburb", "string"), ("(right) state", "string", "project_ state", "string"), ("(right) postcode", "string", "project_ postcode", "string"), ("(right) active", "long", "project_ active", "long"), ("(right) project_duration", "string", "project_duration", "string")], transformation_ctx = "Transform5")
## @type: DataSink
## @args: [connection_type = "s3", catalog_database_name = "monir-olap-bd", format = "csv", connection_options = {"path": "s3://assignar-test-db-bucket/OLAP/fact-order-project/", "partitionKeys": [], "enableUpdateCatalog":true, "updateBehavior":"UPDATE_IN_DATABASE"}, catalog_table_name = "fact_order-project", transformation_ctx = "DataSink0"]
## @return: DataSink0
## @inputs: [frame = Transform5]
DataSink0 = glueContext.getSink(path = "s3://assignar-test-db-bucket/OLAP/fact-order-project/", connection_type = "s3", updateBehavior = "UPDATE_IN_DATABASE", partitionKeys = [], enableUpdateCatalog = True, transformation_ctx = "DataSink0")
DataSink0.setCatalogInfo(catalogDatabase = "monir-olap-bd",catalogTableName = "fact_order-project")
DataSink0.setFormat("csv")
DataSink0.writeFrame(Transform5)

job.commit()