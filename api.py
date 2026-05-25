from fastapi import FastAPI # type: ignore
from database import get_connection
import psycopg2 # type: ignore
from pydantic import BaseModel # type: ignore

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
class PatientRequest(BaseModel):
    patient_id: int
    name: str
    age: int
    gender: str
    city: str

@app.post("/add-patient")
def add_patient(patient: PatientRequest):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO dim_patients (patient_id, name, age, gender, city)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (patient_id) DO NOTHING;
    """, (
        patient.patient_id,
        patient.name,
        patient.age,
        patient.gender,
        patient.city
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "✅ Patient added successfully"}