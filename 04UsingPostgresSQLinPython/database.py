import psycopg2

db_name ="red30"
user="postgres"
pwd = "a"

conn = psycopg2.connect(database=db_name, 
                        user=user,
                        password=pwd,
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

# # create table
# cursor.execute(''' CREATE TABLE SALES(
#                order_num INT PRIMARY KEY,
#                cust_name TEXT,
#                prod_number TEXT,
#                prod_name TEXT, 
#                quantity INT,
#                price REAL,
#                discount REAL,
#                order_total REAL); ''')


## Insert data
sales = [ (1100935, "Spencer Educators", "DK204","BYOD-300", 2, 89, 0, 178),
(1100948, "Ewan Ladd", "TV810", "Understanding Automation", 1, 44.95, 0, 44.95),
(1100963, "Stehr Group", "DS301", "DA-SA702 Drone", 3, 399, .1, 1077.3),
(1100971, "Hettinger and Sons", "DS306", "DA-SA702 Drone", 12, 250, .5, 1500),
(1100998, "Luz O'Donoghue", "TV809", "Understanding 3D Printing", 1, 42.99, 0, 42.99) ]

cursor.executemany("INSERT INTO sales VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", sales)

conn.commit()
conn.close()