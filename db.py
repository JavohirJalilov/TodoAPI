from tinydb import TinyDB,Query

User = Query()

db = TinyDB('db.json')
todo_list = db.table('todoList')
count_table = db.table('Count')

def read():
	data = todo_list.all()
	todo = {"TODO_LIST":data}
	return todo

def addTask(ID:int,status:bool,task_name:str,task_description:str):
	todo_list.insert({
		"id":ID,
		"status":status,
		"task_name":task_name,
		"task_description":task_description
		})

def countUpdate(ID):
	count_table.update({'count':ID},User.language=='python')

def count():
    i = count_table.all()[0]['count']
    return i