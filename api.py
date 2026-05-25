from fastapi import FastAPI # type: ignore
from database import get_connection
import psycopg2 # type: ignore

app = FastAPI()

# ✅ GET API - Fetch patients
@app.get("/patients")
def get_patients():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dim_patients LIMIT 10;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"data": rows}


# ✅ GET API - Fetch doctors
@app.get("/doctors")
def get_doctors():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dim_doctors LIMIT 10;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"data": rows}


# ✅ GET API - Join query (important for POC)
@app.get("/visits")
def get_visits():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.name, d.name, f.disease, f.treatment_cost
        FROM fact_patient_visits f
        JOIN dim_patients p ON f.patient_id = p.patient_id
        JOIN dim_doctors d ON f.doctor_id = d.doctor_id
        LIMIT 10;
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"data": rows}


# ✅ POST API - Add patient
@app.post("/add-patient")
def add_patient(patient_id: int, name: str, age: int, gender: str, city: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO dim_patients (patient_id, name, age, gender, city)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (patient_id) DO NOTHING;
    """, (patient_id, name, age, gender, city))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "✅ Patient added successfully"}