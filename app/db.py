import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import OperationalError
import time

#Settings from config.py holds our credentials
from app.config import settings

def get_db_connection():
    '''Called from main.py's create_student'''
    
    while True:
        try:
            #settings is user frienly way to access typed variables
            conn = psycopg2.connect(
                host=settings.DATABASE_HOST,
                database = settings.DATABASE_NAME,
                user = settings.DATABASE_USER,
                password = settings.DATABASE_PASSWORD,
                cursor_factory = RealDictCursor
            )
            cursor = conn.cursor()
            print("Connection Successful")
            break
        except Exception as error:
            print("Connection Failed")
            print("Error: ", error)
            time.sleep(2)

    return conn, cursor