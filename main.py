from models import Task
from database import *

def main():
    print('hello! i am your tasks manager! what you want to do?')

    con = sqlite3.connect('tasks.db')
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks_manager
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        task TEXT,
                        status BOOLEAN)
                    """)

    print('1 - add, 2 - update task, 3 - update status, 4 - delete task, 5 - return task, 6 - return all tasks, 0 - exit')
    query = input()
    while query != '0':
        if query == '1':
            print('enter your task')
            text = input()
            add_new_task(con, text)
        elif query == '2':
            print('what task do you want to change?')
            id_task = int(input())
            print('enter new task')
            new_text = input()
            update_task(con, id_task, new_text)
        elif query == '3':
            print('which task is status should i change?')
            id_task = int(input())
            print('you completed the task? (да or нет)')
            answer = input()
            if answer == 'yes':
                update_status(con, id_task, True)
            else:
                update_status(con, id_task, False)
        elif query == '4':
            print('which task to delete?')
            id_task = int(input())
            delete_task(con, id_task)
        elif query == '5':
            print('what task to look at?')
            id_task = int(input())
            task = get_task_by_id(con, id_task)
            print(task)
        elif query == '6':
            tasks = select_tasks(con)
            for i in tasks:
                print(i)
        else:
            print('i do not understand...')

        print('enter new query')
        print('1 - add, 2 - update task, 3 - update status, 4 - delete task, 5 - return task, 6 - return all tasks, 0 - exit')
        query = input()
    print('thank you!')

if __name__ == '__main__':
    main()
