from cassandra.cluster import Cluster
import time
from datetime import datetime
from uuid import uuid4

from temperature import temperature
from color import color
from distance import distance
from motion import motion
from air_qual import air_qual
from air_spe import air_spe
from gps import gps
from altimeter import altimeter
from magnetic_compass import magnetic_compass
from oil_pressure import oil_pressure
from fuel import fuel
from tire import tire
from accelerometer import accelerometer

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
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS air_spe_sensor_1 (
            sensor_air_spe_id UUID PRIMARY KEY,
            air_spe double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS air_spe_sensor_2 (
            sensor_air_spe_id UUID PRIMARY KEY,
            air_spe double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS gps_sensor_1 (
            sensor_gps_id UUID PRIMARY KEY,
            latitude double,
            longitude double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS gps_sensor_2 (
            sensor_gps_id UUID PRIMARY KEY,
            latitude double,
            longitude double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS altimeter_sensor_1 (
            sensor_altimeter_id UUID PRIMARY KEY,
            altitude double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS altimeter_sensor_2 (
            sensor_altimeter_id UUID PRIMARY KEY,
            altitude double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS magnetic_compass_sensor_1 (
            sensor_magnetic_compass_id UUID PRIMARY KEY,
            magnetic_compass double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS magnetic_compass_sensor_2 (
            sensor_magnetic_compass_id UUID PRIMARY KEY,
            magnetic_compass double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS oil_pressure_sensor_1 (
            sensor_oil_pressure_id UUID PRIMARY KEY,
            oil_pressure double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS oil_pressure_sensor_2 (
            sensor_oil_pressure_id UUID PRIMARY KEY,
            oil_pressure double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS fuel_sensor_1 (
            sensor_fuel_id UUID PRIMARY KEY,
            fuel double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS fuel_sensor_2 (
            sensor_fuel_id UUID PRIMARY KEY,
            fuel double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS tire_sensor_1 (
            sensor_tire_id UUID PRIMARY KEY,
            tire double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS tire_sensor_2 (
            sensor_tire_id UUID PRIMARY KEY,
            tire double
        );
        """
    )

    session.execute(
        """
        CREATE TABLE IF NOT EXISTS accelerometer_sensor_1 (
            sensor_accelerometer_id UUID PRIMARY KEY,
            x double,
            y double,
            z double
        );
        """
    )
    session.execute(
        """
        CREATE TABLE IF NOT EXISTS accelerometer_sensor_2 (
            sensor_accelerometer_id UUID PRIMARY KEY,
            x double,
            y double,
            z double
        );
        """
    )

    print("Keyspace and tables exist. Connection is working!")
    cpt = 150
    while cpt != 0:
        temperature(session)
        color(session)
        distance(session)
        motion(session)
        air_qual(session)
        air_spe(session)
        gps(session)
        altimeter(session)
        magnetic_compass(session)
        oil_pressure(session)
        fuel(session)
        tire(session)
        accelerometer(session)
        cpt -= 1
        time.sleep(1)

    print("Data sent to the data ingestion component")

    rows = session.execute("SELECT * FROM temperature_data")
    print(rows)

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
