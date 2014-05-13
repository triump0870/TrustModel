import MySQLdb as db
class Consumer:
	user = "rohan"
	passwd = "rohan0870"
	host = "54.186.61.27"
	def __init__(self):
		self.connection = db.connect(user = self.user, passwd= self.passwd, host=self.host)

	def query(self,q):
		cursor = self.connection.cursor()
		cursor.execute(q)
		cursor.close()
	def __del__(self):
		self.connection.close()

