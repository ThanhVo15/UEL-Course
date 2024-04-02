class Task:
    def __init__(self,title,content,deadline,deadlinetime,isfinish):
        self.title=title
        self.content=content
        self.deadline=deadline
        self.deadlinetime=deadlinetime
        self.isfinish=isfinish
        pass
    def __str__(self):
        return self.title

from Tasks import Task
class Tasks:
    def __init__(self):
        self.lists=[]
    def item(self,index)->Task:
        return self.lists[index]
    def add(self,task):
        self.lists.append(task)
    def addAll(self,tasks):
        for i in range(len(tasks)):
            task=tasks[i]
            self.add(task)
    def index(self,task):
        i=self.lists.index(task)
        return i
    def update(self,index,task)->Task:
        self.lists[index]=task
        return self.lists[index]
    def removeByIndex(self,index)->Task:
        return self.lists.pop(index)
    def removeByItem(self,item):
        self.lists.remove(item)
    def clear(self):
        self.lists.clear()
    def size(self):
        return len(self.lists)