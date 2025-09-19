from psycopg2 import connect
from environs import Env 

env = Env()
env.read_env()

def get_connect(autocommit=False):
    conn = connect(
        user=env.str("USER"),
        database=env.str("DATABASE"),
        host=env.str("HOST"),
        port=env.str("PORT"),
        password=env.str("PASSWORD")
    )
    conn.autocommit = autocommit
    return conn

def query_sql(query, *args, fetchall=False, fetchone=False, commit=False):
    try:
        sql = query.strip().upper()

        # 🚀 CREATE DATABASE uchun maxsus ishlash
        if sql.startswith("CREATE DATABASE"):
            conn = get_connect(autocommit=True)
            cur = conn.cursor()
            cur.execute(query)
            cur.close()
            conn.close()
            return True

        # 🔹 Oddiy querylar uchun WITH ishlaydi
        with get_connect(autocommit=commit) as db:
            with db.cursor() as dbc:
                if args:
                    dbc.execute(query, args)
                else:
                    dbc.execute(query)

                if fetchall:
                    return dbc.fetchall()
                if fetchone:
                    return dbc.fetchone()
                if commit:
                    return True
    except Exception as e:
        raise Exception(f"Something went wrong, check your query: {e}!!!")
    return None

# test
test = query_sql("CREATE DATABASE homework;")
print("Database created:", test)
