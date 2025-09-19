from psycopg2 import connect

from environs import Env 



env = Env()
env.read_env("/home/qudratillo_tolibjonov/Рабочий стол/homework/.env")



def get_connect ():
    return connect(
        user=env.str("USER"),
        database = env.str("DATABASE"),
        host = env.str("HOST"),
        port = env.str("PORT"),
        password = env.str("PASSWORD")

    )
get_connect().set_session(autocommit=True)
def query_sql(query,*args,fetchall=False,fetchone=False,commit=False):
    """
    This function gives you opportunities for fast typing query ;
    Format :
    IN ARGS PLEASE WRITE YOUR VALUES WHICH YOU WRITE IN KEYS OF YOUR QUERY !!!
    Fetchall when you WANT TO READ SOMETHING FROM DATABASE !!!
    Fetchone when you WANT TO READ SOMETHING FROM DATABASE but only one !!!
    Commit when you DOALTER USER postgres WITH PASSWORD 'newpassword123';
N'T WANT READ,YOU WANT TO COMMIT SMTH!!!"""




    try:
        with  get_connect()as db:
            db.autocommit = True
            db.set_session(autocommit=True)
            with db.cursor() as dbc:
                if args:
                    dbc.execute(query,args)
                else:
                    dbc.execute(query)


                if fetchall:
                    return dbc.fetchall()
                if fetchone :
                    return dbc.fetchone()
                if commit:
                    return True
    except Exception as e:
        raise Exception(f"Sometihng went wrong , Please attention to your query here {e}!!!")
    return None

test = query_sql("""
    CREATE DATABASE homework ;""",commit=True)


    
