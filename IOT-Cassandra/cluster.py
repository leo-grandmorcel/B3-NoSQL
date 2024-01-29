from cassandra.cluster import Cluster
import time
from datetime import datetime
import random
from uuid import uuid4

from temperature import temperature
from color import color
from distance import distance
from motion import motion
from air_qual import air_qual
from air_spe import air_spe
from gps import gps
from altimeter import altimeter

cluster = None
session = None

try:
    cluster = Cluster(["127.0.0.1"])
    session = cluster.connect()

    session.execute("DROP KEYSPACE IF EXISTS iot_data")
    session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS iot_data
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
    """
    )

    session.set_keyspace("iot_data")

    session.execute(
        """
        CREATE TABLE IF NOT EXISTS temperature_sensor_1 (
            sensor_temp_id UUID PRIMARY KEY,
            temperature double
        )
    """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS temperature_sensor_2 (
            sensor_temp_id UUID PRIMARY KEY,
            temperature double
        )
    """
    )

    session.execute(
        """
        CREATE TABLE IF NOT EXISTS color_sensor_1 (
            sensor_color_id UUID PRIMARY KEY,
            red int,
            green int,
            blue int
        )
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS color_sensor_2 (
            sensor_color_id UUID PRIMARY KEY,
            red int,
            green int,
            blue int
        )
        """
    )

    session.execute(
        """
        CREATE TABLE IF NOT EXISTS distance_sensor_1 (
            sensor_dist_id UUID PRIMARY KEY,
            distance double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS distance_sensor_2 (
            sensor_dist_id UUID PRIMARY KEY,
            distance double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS motion_sensor_1 (
            sensor_motion_id UUID PRIMARY KEY,
            motion boolean
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS motion_sensor_2 (
            sensor_motion_id UUID PRIMARY KEY,
            motion boolean
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS air_qual_sensor_1 (
            sensor_air_qual_id UUID PRIMARY KEY,
            air_qual double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS air_qual_sensor_2 (
            sensor_air_qual_id UUID PRIMARY KEY,
            air_qual double
        );
        """
    )

    print("Keyspace and tables exist. Connection is working!")
    cpt = 150
    while cpt != 0:
        temperature(session, uuid4(), uuid4())
        color(session, uuid4(), uuid4())
        distance(session, uuid4(), uuid4())
        motion(session, uuid4(), uuid4())
        air_qual(session, uuid4(), uuid4())
        air_spe(session, uuid4(), uuid4())
        gps(session, uuid4(), uuid4())
        altimeter(session, uuid4(), uuid4())
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
