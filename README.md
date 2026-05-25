readme_content = """
# 🏥 Healthcare ETL Pipeline & API

## Overview
This project implements an end-to-end Healthcare Data Processing System using Python, PostgreSQL, and FastAPI.

## Features
- ETL pipeline using Pandas
- PostgreSQL data warehouse (dim + fact)
- FastAPI endpoints (GET & POST)
- API testing with Postman

## Technologies
- Python
- Pandas
- PostgreSQL
- FastAPI
- psycopg2
- dotenv

## Project Structure
healthcare_analysis/
├── logic.py
├── database.py
├── pipeline.py
├── api.py
├── data.csv
├── .env

## How to Run

Install:
pip install pandas psycopg2 fastapi uvicorn python-dotenv

Run ETL:
python pipeline.py

Run psql:
psql -U postgres -d healthcare_db

Run API:
python -m uvicorn api:app --reload

## API Endpoints

GET /patients  
GET /doctors  
GET /visits  
GET /patient/{patient_id}  

POST /add-patient  

## Data Flow
CSV → ETL → PostgreSQL → FastAPI → Postman

## Conclusion
This project demonstrates a complete backend healthcare system with ETL and API integration.
"""
