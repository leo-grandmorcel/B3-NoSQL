import random
from uuid import uuid4

def color(session):
    sensor_color_id_1 = uuid4()
    sensor_color_id_2 = uuid4()
    red_1 = random.uniform(0, 255)
    green_1 = random.uniform(0, 255)
    blue_1 = random.uniform(0, 255)
    red_2 = random.uniform(0, 255)
    green_2 = random.uniform(0, 255)
    blue_2 = random.uniform(0, 255)
    try:
        session.execute(
            """
            INSERT INTO color_data (sensor_color_id, red, green, blue)
            VALUES (%s, %s, %s, %s)
            """,
            (sensor_color_id_1, red_1, green_1, blue_1)
        )
        session.execute(
            """
            INSERT INTO color_data (sensor_color_id, red, green, blue)
            VALUES (%s, %s, %s, %s)
            """,
            (sensor_color_id_2, red_2, green_2, blue_2)
        )
    except Exception as e:
        print(f"Error: {e}")
