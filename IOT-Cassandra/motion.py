import random
from uuid import uuid4

def motion(session):
    sensor_motion_id_1 = uuid4()
    sensor_motion_id_2 = uuid4()
    motion_1 = random.choice([True, False])
    motion_2 = random.choice([True, False])
    try:
        session.execute(
            """
            INSERT INTO motion_data (sensor_motion_id, motion)
            VALUES (%s, %s)
            """,
            (sensor_motion_id_1, motion_1)
        )
        session.execute(
            """
            INSERT INTO motion_data (sensor_motion_id, motion)
            VALUES (%s, %s)
            """,
            (sensor_motion_id_2, motion_2)
        )
    except Exception as e:
        print(f"Error: {e}")