import MySQLdb as mydb
class Database:
	user = 'rohan'
	passwd = 'rohan0870'
	host = '54.186.61.27'
	db = 'TrustModel'

	def __init__(self):
		self.connection = mydb.connect(user = self.user, passwd=self.passwd,host=self.host,db=self.db)

	def query(self,q):
		cursor = self.connection.cursor(mydb.cursors.DictCursor)
		cursor.execute(q)
		return cursor.fetchall()

	def __del__(self):
		self.connection.close()