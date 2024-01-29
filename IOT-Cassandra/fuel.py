import random
from uuid import uuid4

def fuel(session):
    fuel_id_1 = uuid4()
    fuel_id_2 = uuid4()
    fuel_1 = random.uniform(0, 1000)
    fuel_2 = random.uniform(0, 1000)
    try:
        session.execute(
            """
            INSERT INTO fuel_sensor_1 (sensor_fuel_id, fuel)
            VALUES (%s, %s)
            """,
            (fuel_id_1, fuel_1)
        )
        session.execute(
            """
            INSERT INTO fuel_sensor_2 (sensor_fuel_id, fuel)
            VALUES (%s, %s)
            """,
            (fuel_id_2, fuel_2)
        )
    except Exception as e:
        print(f"Error: {e}")