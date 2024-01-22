from cassandra.cluster import Cluster

try:
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    # Créez le keyspace 'iot_data' s'il n'existe pas
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS iot_data 
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
    """)

    # Utilisez le keyspace 'iot_data'
    session.set_keyspace('iot_data')

    # Créez la table 'temperature_data' si elle n'existe pas
    session.execute("""
        CREATE TABLE IF NOT EXISTS temperature_data (
            sensor_id UUID PRIMARY KEY,
            temperature double
        )
    """)

    print("Keyspace and table exist. Connection is working!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Fermez la session et le cluster de manière plus robuste
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
