import random
from uuid import uuid4

def air_spe(session):
    air_spe_id_1 = uuid4()
    air_spe_id_2 = uuid4()
    air_spe_1 = random.uniform(0, 340)
    air_spe_2 = random.uniform(0, 680)
    try:
        session.execute(
            """
            INSERT INTO air_spe_sensor_1 (sensor_air_spe_id, air_spe)
            VALUES (%s, %s)
            """,
            (air_spe_id_1, air_spe_1)
        )
        session.execute(
            """
            INSERT INTO air_spe_sensor_2 (sensor_air_spe_id, air_spe)
            VALUES (%s, %s)
            """,
            (air_spe_id_2, air_spe_2)
        )
    except Exception as e:
        print(f"Error: {e}")