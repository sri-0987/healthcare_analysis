import psycopg2  # type: ignore
# import psycopg2
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )

        print("✅ Database connected successfully")
        return conn

    except Exception as e:
        print("❌ Database connection failed:", e)
def insert_data(conn,df):
    cursor = conn.cursor()
    for _, row in df.iterrows():

        cursor.execute("""
            INSERT INTO dim_patients (patient_id, name, age, gender, city)
            VALUES (%s,%s,%s,%s,%s)
            ON CONFLICT (patient_id) DO NOTHING;
        """, (row['patient_id'], row['name'], row['age'], row['gender'], row['city']))

        cursor.execute("""
            INSERT INTO dim_doctors (doctor_id, name, specialization, experience_years)
            VALUES (%s,%s,%s,%s)
            ON CONFLICT (doctor_id) DO NOTHING;
        """, (row['doctor_id'], row['doctor_name'], row['specialization'], 10))

        cursor.execute("""
           
  INSERT INTO fact_patient_visits
(visit_id, patient_id, doctor_id, hospital_id, date_id, disease, treatment_cost, admission_type, stay_days)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (visit_id) DO NOTHING;

        """, (
            row['visit_id'],
            row['patient_id'],
            row['doctor_id'],
            row['hospital_id'],
            row['date_id'],
            row['disease'],
            row['cost'],
            'OP',
            0
        ))

    conn.commit()
    cursor.close()
    conn.close()