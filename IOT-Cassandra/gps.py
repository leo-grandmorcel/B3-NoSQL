import random
from uuid import uuid4

def gps(session):
    sensor_gps_id_1 = uuid4()
    sensor_gps_id_2 = uuid4()
    latitude_1 = random.uniform(0, 100)
    longitude_1 = random.uniform(0, 100)
    latitude_2 = random.uniform(0, 100)
    longitude_2 = random.uniform(0, 100)
    try:
        session.execute(
            """
            INSERT INTO gps_sensor_1 (sensor_gps_id, latitude, longitude)
            VALUES (%s, %s, %s)
            """,
            (sensor_gps_id_1, latitude_1, longitude_1)
        )
        session.execute(
            """
            INSERT INTO gps_sensor_2 (sensor_gps_id, latitude, longitude)
            VALUES (%s, %s, %s)
            """,
            (sensor_gps_id_2, latitude_2, longitude_2)
        )
    except Exception as e:
        print(f"Error: {e}")