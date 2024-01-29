import random
from uuid import uuid4

def air_qual(session):
    air_qual_id_1 = uuid4()
    air_qual_id_2 = uuid4()
    air_qual_1 = random.uniform(0, 100)
    air_qual_2 = random.uniform(0, 100)
    try:
        session.execute(
            """
            INSERT INTO air_qual_data (air_qual_id, air_qual)
            VALUES (%s, %s)
            """,
            (air_qual_id_1, air_qual_1)
        )
        session.execute(
            """
            INSERT INTO air_qual_data (air_qual_id, air_qual)
            VALUES (%s, %s)
            """,
            (air_qual_id_2, air_qual_2)
        )
    except Exception as e:
        print(f"Error: {e}")