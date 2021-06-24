from tinydb import TinyDB,Query

User = Query()

db = TinyDB('db.json')

def read():
	return {}