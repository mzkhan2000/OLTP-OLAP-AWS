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
## @args: [database = "monir-assignar-db", table_name = "user_type", transformation_ctx = "DataSource0"]
## @return: DataSource0
## @inputs: []
DataSource0 = glueContext.create_dynamic_frame.from_catalog(database = "monir-assignar-db", table_name = "user_type", transformation_ctx = "DataSource0")
## @type: ApplyMapping
## @args: [mappings = [("ut_id", "long", "(right) ut_id", "long"), ("user_type", "string", "(right) user_type", "string"), ("label", "string", "(right) label", "string")], transformation_ctx = "Transform3"]
## @return: Transform3
## @inputs: [frame = DataSource0]
Transform3 = ApplyMapping.apply(frame = DataSource0, mappings = [("ut_id", "long", "(right) ut_id", "long"), ("user_type", "string", "(right) user_type", "string"), ("label", "string", "(right) label", "string")], transformation_ctx = "Transform3")
## @type: DataSource
## @args: [database = "monir-assignar-db", table_name = "user", transformation_ctx = "DataSource3"]
## @return: DataSource3
## @inputs: []
DataSource3 = glueContext.create_dynamic_frame.from_catalog(database = "monir-assignar-db", table_name = "user", transformation_ctx = "DataSource3")
## @type: Join
## @args: [columnConditions = ["="], joinType = left, keys2 = ["(right) ut_id"], keys1 = ["ut_id"], transformation_ctx = "Transform2"]
## @return: Transform2
## @inputs: [frame1 = DataSource3, frame2 = Transform3]
DataSource3DF = DataSource3.toDF()
Transform3DF = Transform3.toDF()
Transform2 = DynamicFrame.fromDF(DataSource3DF.join(Transform3DF, (DataSource3DF['ut_id'] == Transform3DF['(right) ut_id']), "left"), glueContext, "Transform2")
## @type: ApplyMapping
## @args: [mappings = [("user_id", "long", "user_id", "long"), ("suburb", "string", "suburb", "string"), ("state", "string", "state", "string"), ("postcode", "string", "postcode", "string"), ("employment_type", "long", "employment_type", "long"), ("active", "long", "user_active_status", "long"), ("modified_time", "string", "user_modified_time", "string"), ("(right) user_type", "string", "user_type", "string"), ("(right) label", "string", "user_label", "string")], transformation_ctx = "Transform4"]
## @return: Transform4
## @inputs: [frame = Transform2]
Transform4 = ApplyMapping.apply(frame = Transform2, mappings = [("user_id", "long", "user_id", "long"), ("suburb", "string", "suburb", "string"), ("state", "string", "state", "string"), ("postcode", "string", "postcode", "string"), ("employment_type", "long", "employment_type", "long"), ("active", "long", "user_active_status", "long"), ("modified_time", "string", "user_modified_time", "string"), ("(right) user_type", "string", "user_type", "string"), ("(right) label", "string", "user_label", "string")], transformation_ctx = "Transform4")
## @type: DataSink
## @args: [connection_type = "s3", catalog_database_name = "monir-olap-bd", format = "csv", connection_options = {"path": "s3://assignar-test-db-bucket/OLAP/dim-user/", "partitionKeys": [], "enableUpdateCatalog":true, "updateBehavior":"UPDATE_IN_DATABASE"}, catalog_table_name = "Dim-user", transformation_ctx = "DataSink0"]
## @return: DataSink0
## @inputs: [frame = Transform4]
DataSink0 = glueContext.getSink(path = "s3://assignar-test-db-bucket/OLAP/dim-user/", connection_type = "s3", updateBehavior = "UPDATE_IN_DATABASE", partitionKeys = [], enableUpdateCatalog = True, transformation_ctx = "DataSink0")
DataSink0.setCatalogInfo(catalogDatabase = "monir-olap-bd",catalogTableName = "Dim-user")
DataSink0.setFormat("csv")
DataSink0.writeFrame(Transform4)

## @type: DataSource
## @args: [database = "monir-assignar-db", table_name = "suppliers", transformation_ctx = "DataSource2"]
## @return: DataSource2
## @inputs: []
DataSource2 = glueContext.create_dynamic_frame.from_catalog(database = "monir-assignar-db", table_name = "suppliers", transformation_ctx = "DataSource2")
## @type: ApplyMapping
## @args: [mappings = [("id", "long", "suppliers_id", "long"), ("city", "string", "city", "string"), ("postcode", "long", "postcode", "long"), ("state", "string", "state", "string"), ("active", "long", "suppliers_active", "long"), ("date_added", "string", "suppliers_date_added", "string"), ("date_modified", "string", "suppliers_date_modified", "string"), ("modified_time", "string", "suppliers_modified_time", "string")], transformation_ctx = "Transform0"]
## @return: Transform0
## @inputs: [frame = DataSource2]
Transform0 = ApplyMapping.apply(frame = DataSource2, mappings = [("id", "long", "suppliers_id", "long"), ("city", "string", "city", "string"), ("postcode", "long", "postcode", "long"), ("state", "string", "state", "string"), ("active", "long", "suppliers_active", "long"), ("date_added", "string", "suppliers_date_added", "string"), ("date_modified", "string", "suppliers_date_modified", "string"), ("modified_time", "string", "suppliers_modified_time", "string")], transformation_ctx = "Transform0")
## @type: DataSink
## @args: [connection_type = "s3", catalog_database_name = "monir-olap-bd", format = "csv", connection_options = {"path": "s3://assignar-test-db-bucket/OLAP/dim-suppliers/", "partitionKeys": [], "enableUpdateCatalog":true, "updateBehavior":"UPDATE_IN_DATABASE"}, catalog_table_name = "Dim-suppliers", transformation_ctx = "DataSink1"]
## @return: DataSink1
## @inputs: [frame = Transform0]
DataSink1 = glueContext.getSink(path = "s3://assignar-test-db-bucket/OLAP/dim-suppliers/", connection_type = "s3", updateBehavior = "UPDATE_IN_DATABASE", partitionKeys = [], enableUpdateCatalog = True, transformation_ctx = "DataSink1")
DataSink1.setCatalogInfo(catalogDatabase = "monir-olap-bd",catalogTableName = "Dim-suppliers")
DataSink1.setFormat("csv")
DataSink1.writeFrame(Transform0)

## @type: DataSource
## @args: [database = "monir-assignar-db", table_name = "client", transformation_ctx = "DataSource1"]
## @return: DataSource1
## @inputs: []
DataSource1 = glueContext.create_dynamic_frame.from_catalog(database = "monir-assignar-db", table_name = "client", transformation_ctx = "DataSource1")
## @type: ApplyMapping
## @args: [mappings = [("client_id", "long", "client_id", "long"), ("city", "string", "city", "string"), ("postcode", "string", "postcode", "string"), ("state", "string", "state", "string"), ("active", "long", "client_active", "long")], transformation_ctx = "Transform1"]
## @return: Transform1
## @inputs: [frame = DataSource1]
Transform1 = ApplyMapping.apply(frame = DataSource1, mappings = [("client_id", "long", "client_id", "long"), ("city", "string", "city", "string"), ("postcode", "string", "postcode", "string"), ("state", "string", "state", "string"), ("active", "long", "client_active", "long")], transformation_ctx = "Transform1")
## @type: DataSink
## @args: [connection_type = "s3", catalog_database_name = "monir-olap-bd", format = "csv", connection_options = {"path": "s3://assignar-test-db-bucket/OLAP/dim-client/", "partitionKeys": [], "enableUpdateCatalog":true, "updateBehavior":"UPDATE_IN_DATABASE"}, catalog_table_name = "Dim-client", transformation_ctx = "DataSink2"]
## @return: DataSink2
## @inputs: [frame = Transform1]
DataSink2 = glueContext.getSink(path = "s3://assignar-test-db-bucket/OLAP/dim-client/", connection_type = "s3", updateBehavior = "UPDATE_IN_DATABASE", partitionKeys = [], enableUpdateCatalog = True, transformation_ctx = "DataSink2")
DataSink2.setCatalogInfo(catalogDatabase = "monir-olap-bd",catalogTableName = "Dim-client")
DataSink2.setFormat("csv")
DataSink2.writeFrame(Transform1)

job.commit()