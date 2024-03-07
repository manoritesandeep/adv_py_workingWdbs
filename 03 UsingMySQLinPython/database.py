import mysql.connector as mysql

def connect(db_name):
    try:
        return mysql.connect(host='localhost',
                            user="root",
                            password="MySQL123",
                            database=db_name)
    except mysql.Error as e:
        print(e)


def add_project(cursor, project_title, project_description, tasks):
    project_data = (project_title, project_description)
    cursor.execute(''' INSERT INTO projects(title, description)
                   VALUES (%s, %s)''', project_data)
    
    tasks_data = []
    for task in tasks:
        task_data = (cursor.lastrowid, task)
        tasks_data.append(task_data)

    cursor.executemany(''' INSERT INTO tasks(project_id, description) 
                       vALUES(%s, %s)''', tasks_data)


if __name__ == '__main__':
    db = connect("projects")

    cursor = db.cursor()

    tasks = ["Clean bathroom", "Clean Kitchen", "Clean living room"]
    add_project(cursor=cursor, 
                project_title="Clean house", 
                project_description="Clean house by room", 
                tasks=tasks)
    db.commit()
    
    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    print(project_records)

    cursor.execute("SELECT * FROM tasks")
    task_records = cursor.fetchall()
    print(task_records)






















# if __name__ == '__main__':
#     db = connect("projects")
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM projects")
#     project_records = cursor.fetchall()
#     print(project_records)
#     db.close()

