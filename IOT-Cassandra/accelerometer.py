import random
from uuid import uuid4

def accelerometer(session):
    sensor_acc_id_1 = uuid4()
    sensor_acc_id_2 = uuid4()
    x_1 = random.uniform(-10, 10)
    y_1 = random.uniform(-10, 10)
    z_1 = random.uniform(-10, 10)
    x_2 = random.uniform(-10, 10)
    y_2 = random.uniform(-10, 10)
    z_2 = random.uniform(-10, 10)
    try:
        session.execute(
            """
            INSERT INTO accelerometer_sensor_1 (sensor_acc_id, x, y, z)
            VALUES (%s, %s, %s, %s)
            """,
            (sensor_acc_id_1, x_1, y_1, z_1)
        )
        session.execute(
            """
            INSERT INTO accelerometer_sensor_2 (sensor_acc_id, x, y, z)
            VALUES (%s, %s, %s, %s)
            """,
            (sensor_acc_id_2, x_2, y_2, z_2)
        )
    except Exception as e:
        print(f"Error: {e}")