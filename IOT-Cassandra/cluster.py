from cassandra.cluster import Cluster
import time
from datetime import datetime
import random
from uuid import uuid4

cluster = None
session = None

try:
    cluster = Cluster(["127.0.0.1"])
    session = cluster.connect()

    session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS iot_data 
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
    """
    )

    session.set_keyspace("iot_data")

    session.execute(
        """
        CREATE TABLE IF NOT EXISTS temperature_data (
            sensor_id UUID PRIMARY KEY,
            temperature double
        )
    """
    )

    session.execute(
        """
        CREATE TABLE IF NOT EXISTS color_data (
            sensor_id UUID PRIMARY KEY,
            red int,
            green int,
            blue int
        )
        """
    )

    print("Keyspace and tables exist. Connection is working!")
    cpt = 60
    while cpt != 0:
        temperature = random.uniform(0.0, 100.0)
        color = {
            'red': random.randint(0, 255),
            'green': random.randint(0, 255),
            'blue': random.randint(0, 255)
        }
        sensor_id = uuid4()

        session.execute(
            """
            INSERT INTO temperature_data (sensor_id, temperature)
            VALUES (%s, %s)
            """,
            (sensor_id, temperature)
        )
        session.execute(
            """
            INSERT INTO color_data (sensor_id, red, green, blue)
            VALUES (%s, %s, %s, %s)
            """,
            (sensor_id, color['red'], color['green'], color['blue'])
        )
        cpt -= 1
        time.sleep(1)

    print("Data sent to the data ingestion component")

    rows = session.execute("SELECT * FROM temperature_data")
    print(rows)
    # for row in rows:
    #     print(row)

except Exception as e:
    print(f"Error: {e}")

finally:
    try:
        if session:
            session.shutdown()
    except Exception as e:
        print(f"Error while closing session: {e}")

    try:
        if cluster:
            cluster.shutdown()
    except Exception as e:
        print(f"Error while closing cluster: {e}")
