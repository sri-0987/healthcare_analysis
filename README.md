Healthcare ETL Pipeline & API

###Overview
This project implements an end-to-end Healthcare Data Processing System using Python, PostgreSQL, and FastAPI.

It includes:
-ETL pipeline to process healthcare data
-Data storage using PostgreSQL (dim + fact tables)
-REST APIs for accessing and managing data
-API testing using Postman

###Technologies

-Python
-Pandas
-PostgreSQL
-FastAPI
-psycopg2
-python-dotenv
-Postman

###How to Run
Install dependencies
pip install pandas psycopg2 fastapi uvicorn python-dotenv

-Run ETL Pipeline
python pipeline.py

Output
Extracting.....
Transforming.....
Loading.....
ETL Completed.....!

-Run psql
psql -U postgres -d healthcare_db

-Run API Server
python -m uvicorn api:app --reload

Open:
http://127.0.0.1:8000/docs


###Project Achievements & Insights
✅ Revenue Analysis

Identified top-performing doctors
Calculated total treatment cost

✅ Patient Analysis

Detected repeat patients
Identified high-cost patients

✅ Disease Analysis

Found most common diseases
Calculated average treatment cost

✅ Hospital Performance

Compared hospitals based on patient volume
Identified high-load hospitals

✅ Time-Based Trends

Analyzed monthly visit patterns
Identified seasonal trends