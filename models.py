

class Task:
    def __init__(self,
                 id_task,
                 text_task,
                 status):
        self.id_task = id_task
        self.text = text_task
        self.status: bool = status

    def change_task(self, new_text):
        self.text = new_text

    def is_done_task(self):
        self.status = True

    def isnt_done_task(self):
        self.status = False

class List_Tasks:
    def __init__(self):
        self.task_lst = []

    def add_task(self):
        print('enter you task')
        text = input()
        new_task = Task(len(self.task_lst)+1, text, False)
        self.task_lst.append(new_task)
        print('you add new task')

    def change_tasks(self):
        print('enter id')
        i = int(input())
        print('enter task')
        new_text = input()
        self.task_lst[i-1].change_task(new_text)
        print('task successfully change')

    def delete_task(self):
        print('enter id')
        i = int(input())
        self.task_lst.pop(i-1)
        for j in range(i-1, len(self.task_lst)):
            self.task_lst[j].id_task = j+1
        print('task №', i, 'delete')

    def done(self):
        print('enter id')
        i = int(input())
        self.task_lst[i-1].is_done_task()
        print('task is done')

    def not_done(self):
        print('enter id')
        i = int(input())
        self.task_lst[i-1].isnt_done_task()
        print('task is not done')

    def __str__(self):
        return f'{self.task_lst}'

    def all_list(self):
        for i in range(len(self.task_lst)):
            print(f'{self.task_lst[i].id_task}  {self.task_lst[i].text}  {self.task_lst[i].status}')

    def check_status(self):
        print('enter id')
        i = int(input())
        if self.task_lst[i-1].status is True:
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    lst_tasks = List_Tasks()
    print('hello, enter you request')
    print('1 - add; 2 - change; 3 - delete; 4 - done; 5 - not done; 6 - check; 7 - print; 0 - exit')
    request = input()
    while request != '0':
        if request == '1':
            lst_tasks.add_task()

        elif request == '2':
            lst_tasks.change_tasks()

        elif request == '3':
            lst_tasks.delete_task()

        elif request == '4':
            lst_tasks.done()

        elif request == '5':
            lst_tasks.not_done()

        elif request == '6':
            lst_tasks.check_status()

        elif request == '7':
            lst_tasks.all_list()

        else:
            print('i do not understand')

        print('enter new request')
        print('1 - add; 2 - change; 3 - delete; 4 - done; 5 - not done; 6 - check; 7 - print; 0 - exit')
        request = input()
    print('thank you!')