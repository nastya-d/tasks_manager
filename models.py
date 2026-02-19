
class Task:
    def __init__(self,
                 id_task,
                 text_task,
                 status):
        self.id_task = id_task
        self.text = text_task
        self.status: bool = status

    def __str__(self):
        return f'{self.id_task}   {self.text}   {self.status}'