import random
from uuid import uuid4

def altimeter(session):
    sensor_alt_id_1 = uuid4()
    sensor_alt_id_2 = uuid4()
    altitude_1 = random.uniform(0, 40000)
    altitude_2 = random.uniform(0, 40000)
    try:
        session.execute(
            """
            INSERT INTO altimeter_sensor_1 (sensor_altimeter_id, altitude)
            VALUES (%s, %s)
            """,
            (sensor_alt_id_1, altitude_1)
        )
        session.execute(
            """
            INSERT INTO altimeter_sensor_2 (sensor_altimeter_id, altitude)
            VALUES (%s, %s)
            """,
            (sensor_alt_id_2, altitude_2)
        )
    except Exception as e:
        print(f"Error: {e}")