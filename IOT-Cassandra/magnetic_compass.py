import random
from uuid import uuid4

def magnetic_compass(session):
    magnetic_compass_id_1 = uuid4()
    magnetic_compass_id_2 = uuid4()
    magnetic_compass_1 = random.uniform(0, 359)
    magnetic_compass_2 = random.uniform(0, 359)
    try:
        session.execute(
            """
            INSERT INTO magnetic_compass_sensor_1 (sensor_magnetic_compass_id, magnetic_compass)
            VALUES (%s, %s)
            """,
            (magnetic_compass_id_1, magnetic_compass_1)
        )
        session.execute(
            """
            INSERT INTO magnetic_compass_sensor_2 (sensor_magnetic_compass_id, magnetic_compass)
            VALUES (%s, %s)
            """,
            (magnetic_compass_id_2, magnetic_compass_2)
        )
    except Exception as e:
        print(f"Error: {e}")