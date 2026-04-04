import psycopg2
from config import load_config


def connect():
    config = load_config()
    conn = psycopg2.connect(**config)
    return conn

import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="1234",
        options='-c client_encoding=UTF8'
    )
