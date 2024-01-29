import random
from uuid import uuid4

def tire(session):
    tire_id_1 = uuid4()
    tire_id_2 = uuid4()
    tire_1 = random.uniform(0, 2000)
    tire_2 = random.uniform(0, 2000)
    try:
        session.execute(
            """
            INSERT INTO tire_sensor_1 (sensor_tire_id, tire)
            VALUES (%s, %s)
            """,
            (tire_id_1, tire_1)
        )
        session.execute(
            """
            INSERT INTO tire_sensor_2 (sensor_tire_id, tire)
            VALUES (%s, %s)
            """,
            (tire_id_2, tire_2)
        )
    except Exception as e:
        print(f"Error: {e}")