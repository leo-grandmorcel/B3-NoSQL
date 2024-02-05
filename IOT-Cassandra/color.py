import random
from uuid import uuid4

def color(session):
    sensor_color_id_1 = uuid4()
    sensor_color_id_2 = uuid4()
    red_1 = int(random.uniform(0, 255)//1)
    green_1 = int(random.uniform(0, 255)//1)
    blue_1 = int(random.uniform(0, 255)//1)
    red_2 = int(random.uniform(0, 255)//1)
    green_2 = int(random.uniform(0, 255)//1)
    blue_2 = int(random.uniform(0, 255)//1)
    try:
        session.execute(
            """
            INSERT INTO color_sensor_1 (sensor_color_id, red, green, blue)
            VALUES (%s, %s, %s, %s)
            """,
            (sensor_color_id_1, red_1, green_1, blue_1)
        )
        session.execute(
            """
            INSERT INTO color_sensor_2 (sensor_color_id, red, green, blue)
            VALUES (%s, %s, %s, %s)
            """,
            (sensor_color_id_2, red_2, green_2, blue_2)
        )
    except Exception as e:
        print(f"Error: {e}")
