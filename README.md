# Retail Sales Data Warehouse & Business Intelligence System

End-to-end retail analytics project demonstrating **Python ETL, SQL data warehousing, data quality validation, business analysis, and BI-ready reporting**.

## Project Architecture

Raw CSV → Python ETL → SQL Data Warehouse → Data Quality Checks → BI-ready Datasets → Dashboard

## Business Objective

Build a reliable retail analytics pipeline that transforms raw transactional data into validated, analysis-ready datasets for business reporting and decision-making.

## Tools & Technologies

- Python
- Pandas
- SQL
- SQLite
- Excel
- Power BI
- GitHub

## Key Skills Demonstrated

- ETL pipeline development
- Data cleaning and transformation
- SQL joins and aggregations
- CTEs and window functions
- Data warehouse design
- Data quality validation
- KPI analysis
- Regional and product performance analysis
- Business insights generation

## Data Quality Checks

The project validates common real-world data issues including:

- Missing values
- Invalid quantities
- Negative sales values
- Missing payment methods
- Orphan customer keys
- Orphan product keys

## Business Analysis

The project produces BI-ready datasets for:

- Monthly sales performance
- Regional revenue analysis
- Product performance
- KPI summary
- Revenue and profit analysis

## Project Structure

```text
data/
├── raw/
└── processed/

python_etl/
├── etl_pipeline.py
└── data_quality_checks.py

sql/
├── 01_schema.sql
├── 02_business_analysis.sql
└── 03_data_quality.sql

warehouse/
└── retail_dw.db

powerbi/
├── monthly_sales.csv
├── region_performance.csv
├── product_performance.csv
└── kpi_summary.csv

business_insights/
└── business_insights.md

screenshots/
├── architecture.png
└── dashboard_preview.png

docs/
└── data_dictionary.csv
