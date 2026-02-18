

class Task:
    def __init__(self,
                 id_task,
                 text,
                 is_done):
        self.id_task: int = id_task
        self.text: str = text
        self.is_done: bool = is_done

    def change_task(self, new_text):
        self.text = new_text

    def is_done_task(self):
        self.id_task = True

    def isnt_done_task(self):
        self.id_task = False

class List_Tasks:
    def __init__(self):
        self.task_lst = []

    def add_task(self, text):
        new_task = Task(len(self.task_lst), text, False)
        self.task_lst.append(new_task)

    def change_task(self, id_task, new_text):
        self.task_lst[id_task-1].change(new_text)

    def delete_task(self, id_task):
        self.task_lst.pop(id_task-1)
        for i in range(id_task-1, len(self.task_lst)):
            self.task_lst[i].id_task = i

    def done(self, id_task):
        self.task_lst[id_task-1].is_done_task()

    def not_done(self, id_task):
        self.task_lst[id_task-1].isnt_done_task()

    def check_status(self, id_task):
        if self.task_lst[id_task-1].is_done is True:
            print('yes')
        else:
            print('no')