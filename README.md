# 🚚 Smart Logistics & Delivery Data Engineering Pipeline (PySpark)

## Executive Summary

The Smart Logistics & Delivery Data Engineering Pipeline is a
production-style batch data platform that simulates how a modern
logistics company processes shipment, warehouse, and delivery
performance data at scale.

This project demonstrates enterprise-grade data engineering principles
including:

-   Layered Data Lake architecture (Bronze → Silver → Gold)
-   Data validation and quality enforcement
-   SLA breach detection
-   Risk scoring logic
-   Dimensional modeling (Star Schema)
-   Business KPI generation
-   Modular, production-ready PySpark design

It is designed to reflect real-world logistics, supply chain, and
transportation analytics systems.

------------------------------------------------------------------------

## Business Context

Logistics companies must monitor shipment performance, delivery
timelines, and SLA compliance to maintain operational excellence and
customer satisfaction.

This pipeline enables:

-   Monitoring late deliveries
-   Identifying SLA breaches
-   Evaluating delivery risk levels
-   Tracking revenue by destination
-   Measuring average delivery time performance

------------------------------------------------------------------------

## Architecture Overview

Raw CSV Data\
↓\
Bronze Layer (Raw Ingestion & Schema Enforcement)\
↓\
Silver Layer (Data Cleaning, Validation & Enrichment)\
↓\
SLA Detection Layer\
↓\
Risk Scoring Layer\
↓\
Gold Layer (Dimensional Star Schema)\
↓\
Business KPI Reports

------------------------------------------------------------------------

## Data Lake Layer Design

### Bronze Layer

-   Raw shipment ingestion from CSV
-   Schema enforcement
-   Stored in Parquet format
-   Immutable raw dataset

### Silver Layer

-   Duplicate removal
-   Date type conversions
-   Delivery duration calculation
-   Positive value validation
-   Clean, analytics-ready dataset

### SLA Detection

-   Configurable SLA threshold
-   Flags shipments as BREACH or ON_TIME

### Risk Scoring

-   Multi-level risk classification
-   Risk score (1--3) based on delivery delay

### Gold Layer (Star Schema)

Dimension Tables: - dim_customer - dim_warehouse

Fact Table: - fact_shipments

Optimized for BI tools and analytics workloads.

------------------------------------------------------------------------

## Technology Stack

-   Python 3.9+
-   PySpark 3.5
-   Parquet (Columnar Storage)
-   Local Data Lake (File System)
-   Modular Python Architecture

------------------------------------------------------------------------

## Project Structure
```
smart_logistics_pipeline/

├── main.py\
├── config.py\
├── requirements.txt

├── data/\
│ └── shipments.csv

├── jobs/\
│ ├── bronze_ingestion.py\
│ ├── silver_transformation.py\
│ ├── sla_detection.py\
│ ├── risk_scoring.py\
│ ├── gold_star_schema.py\
│ └── business_kpis.py

├── utils/
│ ├── spark_session.py
│ ├── schema.py
│ ├── validators.py
│ └── helpers.py

└── output/
├── bronze/
├── silver/
├── gold/
└── reports/
```
------------------------------------------------------------------------

## Execution Instructions

### Install Dependencies

pip install -r requirements.txt

### Run Pipeline

python main.py

Execution Flow: 1. Bronze ingestion 2. Silver transformation 3. SLA
breach detection 4. Risk scoring 5. Gold star schema creation 6. KPI
report generation

------------------------------------------------------------------------

## Key Metrics Generated

-   Total shipping revenue by destination city
-   Average delivery days by city
-   SLA breach distribution
-   Shipment risk distribution

Reports are written to:

output/reports/

------------------------------------------------------------------------

## Data Model Overview

### Dimension: dim_customer

-   customer_id

### Dimension: dim_warehouse

-   warehouse_id
-   origin_city

### Fact: fact_shipments

-   shipment_id
-   customer_id
-   warehouse_id
-   destination_city
-   weight_kg
-   shipping_cost
-   delivery_days
-   sla_breach
-   risk_score

This model supports BI dashboards, operational reporting, and
performance monitoring.

------------------------------------------------------------------------

## Enterprise Engineering Practices Demonstrated

-   Modular PySpark job design
-   Config-driven architecture
-   Data validation layer
-   Layered transformation pattern
-   Clear separation of ingestion and analytics layers
-   Star schema modeling
-   Reproducible batch execution

------------------------------------------------------------------------

## Scalability & Production Extensions

This pipeline can be extended with:

-   Partitioning by date and region
-   Delta Lake integration
-   Cloud storage (AWS S3 / Azure Data Lake)
-   Orchestration via Apache Airflow
-   Streaming ingestion using Kafka
-   CI/CD integration
-   Data quality monitoring framework

------------------------------------------------------------------------
