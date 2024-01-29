import random
from uuid import uuid4

def oil_pressure(session):
    oil_pressure_id_1 = uuid4()
    oil_pressure_id_2 = uuid4()
    oil_pressure_1 = random.uniform(0, 500)
    oil_pressure_2 = random.uniform(0, 500)
    try:
        session.execute(
            """
            INSERT INTO oil_pressure_data (oil_pressure_id, oil_pressure)
            VALUES (%s, %s)
            """,
            (oil_pressure_id_1, oil_pressure_1)
        )
        session.execute(
            """
            INSERT INTO oil_pressure_data (oil_pressure_id, oil_pressure)
            VALUES (%s, %s)
            """,
            (oil_pressure_id_2, oil_pressure_2)
        )
    except Exception as e:
        print(f"Error: {e}")