from psycopg2 import connect

db = connect(
    user="postgres",
    password="Aprel2010",
    host="localhost",
    port="5432",
    database="postgres"

    
)
db.autocommit = True    
dbc = db.cursor()
dbc.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY,
        name varchar(50) NOT NULL,
        email varchar(50) NOT NULL);
        """)
dbc.execute("""insert into users(name,email)values
    ('kamal','kamal@.com'),
    ('kamal2','kamal2@.com'),   
    ('kamal3','kamal3@.com'),
    ('kamal4','kamal4@.com'),
    ('kamal5','kamal5@.com'),
    ('kamal6','kamal6@.com'),
    ('kamal7','kamal7@.com'),
    ('kamal8','kamal8@.com'),
    ('kamal9','kamal9@.com'),
    ('kamal10','kamal10@.com');""")
dbc.execute("""

create table if not exists passport(
    id serial primary key,
    passport_number int unique not null,
    user_id int not null unique references users(id));""")
dbc.execute("""
insert into passport(passport_number,user_id)values
(1234567890,1),
(1234567891,2),
(1234567892,3),
(1234567893,4),
(1234567894,5),
(1234567895,6),
(1234567896,7),
(1234567897,8),
(1234567898,9),
(1234567899,10);""")
db.commit()
db.close()