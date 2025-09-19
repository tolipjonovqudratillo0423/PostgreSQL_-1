from psycopg2 import connect
from environs import Env

env = Env()
env.read_env("/home/qudratillo_tolibjonov/Рабочий стол/homework/.env")

conn = connect(
    user=env.str("USER"),
    password=env.str("PASSWORD"),
    host=env.str("HOST"),
    port=env.str("PORT"),
    database=env.str("DATABASE")
)
print("Connected successfully!")
conn.close()
