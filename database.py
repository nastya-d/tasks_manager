import sqlite3
from models import Task

def add_new_task(connect, text):
    cursor = connect.cursor()
    try:
        cursor.execute("""
        INSERT INTO
            tasks_manager (task, status)
        VALUES
            (?, ?);
        """, (text, False,))
        connect.commit()
        print('success!')
    except sqlite3.DatabaseError as err:
        print('error: ', err)

def update_task(connect, id_task, text):
    cursor = connect.cursor()
    try:
        cursor.execute("""
        UPDATE
            tasks_manager
        SET
            task = ?
        WHERE
            id = ?
        """, (text, id_task,))
        connect.commit()
        print('success!')
    except sqlite3.DatabaseError as err:
        print('error: ', err)

def update_status(connect, id_task, new_status):
    cursor = connect.cursor()
    try:
        cursor.execute("""
           UPDATE
               tasks_manager
           SET
               status = ?
           WHERE
               id = ?
           """, (new_status, id_task,))
        connect.commit()
        print('success!')
    except sqlite3.DatabaseError as err:
        print('error: ', err)

def delete_task(connect, id_task):
    cursor = connect.cursor()
    try:
        cursor.execute("""
        DELETE FROM
            tasks_manager
        WHERE
            id = ?
        """, (id_task,))
        connect.commit()
        print('success!')
    except sqlite3.DatabaseError as err:
        print('error: ', err)

def select_tasks(connect):
    cursor = connect.cursor()
    cursor.execute("""
        SELECT * FROM tasks_manager
    """)
    rows = cursor.fetchall()

    tasks = []
    for row in rows:
        task = Task(row[0], row[1], bool(row[2]))
        tasks.append(task)
    return tasks

def get_task_by_id(connect, id_task):
    cursor = connect.cursor()
    cursor.execute("""
        SELECT 
            id, task, status 
        FROM 
            tasks_manager
        WHERE
            id = ?    
        """, (id_task,))
    row = cursor.fetchone()
    if row is None:
        return None
    task = Task(row[0], row[1], bool(row[2]))
    return task
