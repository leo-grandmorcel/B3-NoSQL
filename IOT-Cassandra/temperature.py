import random
from uuid import uuid4

def temperature(session):
    sensor_temp_id_1 = uuid4()
    sensor_temp_id_2 = uuid4()
    temperature_1 = random.uniform(0, 100)
    temperature_2 = random.uniform(0, 100)
    try:
        session.execute(
            """
            INSERT INTO temperature_sensor_1 (sensor_temp_id, temperature)
            VALUES (%s, %s)
            """,
            (sensor_temp_id_1, temperature_1)
        )
        session.execute(
            """
            INSERT INTO temperature_sensor_2 (sensor_temp_id, temperature)
            VALUES (%s, %s)
            """,
            (sensor_temp_id_2, temperature_2)
        )

    except Exception as e:
        print(f"Error: {e}")
