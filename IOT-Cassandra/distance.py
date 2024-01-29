import random
from uuid import uuid4

def distance(session):
    sensor_dist_id_1 = uuid4()
    sensor_dist_id_2 = uuid4()
    distance_1 = random.uniform(0.0, 100.0)
    distance_2 = random.uniform(0.0, 100.0)
    try:
        session.execute(
            """
            INSERT INTO distance_data (sensor_dist_id, distance)
            VALUES (%s, %s)
            """,
            (sensor_dist_id_1, distance_1)
        )
        session.execute(
            """
            INSERT INTO distance_data (sensor_dist_id, distance)
            VALUES (%s, %s)
            """,
            (sensor_dist_id_2, distance_2)
        )
    except Exception as e:
        print(f"Error: {e}")