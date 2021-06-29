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


CREATE TABLE assignar_olap_db.dimention_user 
(
user_id	INT,
suburb VARCHAR(100),
state VARCHAR(50),
postcode VARCHAR(10),
employment_type	VARCHAR(50),
user_active_status VARCHAR(50),
user_modified_time DATETIME,
user_type VARCHAR(50),
user_label VARCHAR(50)
);


CREATE TABLE assignar_olap_db.dimention_client 
(
client_id INT,
city VARCHAR(100),
postcode VARCHAR(10),
state VARCHAR(50),
client_active INT
);


CREATE TABLE assignar_olap_db.dimention_suppliers
(
suppliers_id	INT,
city VARCHAR(100),
postcode VARCHAR(10),
state VARCHAR(50),
suppliers_active_status VARCHAR(50),
suppliers_date_added DATETIME,
suppliers_date_modified DATETIME,
suppliers_modified_time DATETIME
);