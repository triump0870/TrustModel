import Database
import sys

if __name__ == '__main__':
	db = Database.Database()
	q = '''start transaction''' 
	db.query(q)
	q = '''insert into Consumers(name,time_stamp) values('roy',now()) '''
	db.query(q)
	q='''select id,name from Consumers order by time_stamp desc limit 1'''
	p = db.query(q)
	print p[0]['id']
	for i in p:
		print i
	q = '''select Raters.id,Consumers.name,Raters.td from Raters join Consumers where Raters.id = Consumers.id and Raters.webservice_id = 2'''
	s = db.query(q)
	for i in s:
		print "\n"
		print "Id=%s"%i['id']
		print "Name=%s"%i['name']
		print "Web service Trust Value=%s"%i['td']
	db.query('''commit''')