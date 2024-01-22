from cassandra.cluster import Cluster
import time
from datetime import datetime
import random

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

    print("Keyspace and table exist. Connection is working!")
    cpt = 60
    while cpt != 0:
        temperature = random.uniform(20.0, 30.0)
        # TODO: Send data to the data ingestion component    print(f"Timestamp: {timestamp}, Temperature: {temperature}")
        cpt -= 1
        session.execute(
            """
            INSERT INTO temperature_data (temperature)
            VALUES (%s, %s)
            """,
            (temperature),
        )
        time.sleep(1)

    print("Data sent to the data ingestion component")

    rows = session.execute("SELECT * FROM temperature_data")
    for row in rows:
        print(row)

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
