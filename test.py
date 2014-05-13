import MySQLdb as mydb
import sys
class Database:
	user = 'root'
	passwd = 'root'
	host = 'localhost'
	db = 'TrustModel'

	def __init__(self):
		self.connection = mydb.connect(user = self.user, passwd=self.passwd,host=self.host,db=self.db)

	def query(self,q):
		cursor = self.connection.cursor(mydb.cursors.DictCursor)
		cursor.execute(q)
		self.connection.commit()
		return cursor.fetchall()

	def __del__(self):
		self.connection.close()

if __name__ == '__main__':
	try:
		db = Database()
		qj = input("Enter quality:")
		l = int(input("Enter level:"))
		w = int(input("Enter interest:"))
		q = '''insert into Requirment(quality,level,interest,time_stamp) values({0},{1},{2},now())'''.format(qj,l,w)
		db.query(q)
	except KeyboardInterrupt:
		print 'You cancelled the execution ..!!'
	except IOError:
		print 'Error: input error ..!!'
		sys.exit(1)

	print '\nThe current entry is:'
	print '\n'
	p = db.query('''SELECT id,quality,level,interest, DATE_FORMAT( time_stamp, '%W %H:%i' )
		FROM Requirment
		ORDER BY id DESC
		LIMIT 1
		''')
	for item in p:
		print 'Id:%s'%item['id']
		print 'Quality:%s'%item['quality']
		print 'Level:%s'%item['level']
		print 'Interest:%s'%item['interest']