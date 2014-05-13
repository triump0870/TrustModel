import Database
import sys
import numpy
if __name__ == '__main__':
	try:
		db = Database.Database()
		#while(1):
		name = str(raw_input('\nEnter your name:'))
		print name
		cslist = list(raw_input("\nEnter the id of the web services that you want to use separated by space\n1.Video\n2.Music\n3.Image\n4.Document\n\nYour Choice:").split())
		qj = input("Enter quality(0->Speed 1->Availability 2->Cost):")
		l = int(input("\nEnter required level of quality\n1.Very Low\n2.Low\n3.Good\n4.High\n5.Very High\n\nYour Choice:"))
		w = int(input("\nEnter your level of interesest on the above quality\n0.Not interested\n2.Interested\n3.Very Interested\n\nYour Choice:"))
		q = '''start transaction'''
		db.query(q)
		q = '''insert into Consumers(name,time_stamp) values('{0}',now())'''.format(name)
		db.query(q)
		consumer_id = db.query('''select id from Consumers order by time_stamp DESC limit 1''')
		q = '''insert into Requirment(consumer_id,quality,level,interest,time_stamp) values({0},{1},{2},{3},now())'''.format(consumer_id[0]['id'],qj,l,w)
		db.query(q)
		q = "select * from WebServices"
		ws = db.query(q)
		tx = []
		tdx = []
		trx = []
		tcx = []
		for i in range(len(cslist)):
			tcx.insert(i,0)
			for j in ws:
				if cslist[i] in str(j['id']):
					print "\n<--{0} using the web service {1}-->".format(name,j['name'])
					dx= input("\n\nEnter the trust(0/1):")
					tdx.insert(i,dx)
					A = 0
					B = 0
					q = '''select Raters.id,Consumers.name,Raters.td from Raters join Consumers where Raters.id = Consumers.id and Raters.webservice_id = {0}'''.format(cslist[i])
					cs = db.query(q)
					for y in cs:
						print "\n"
						print "Rater's Name:%s"%y['name']
						print "Current Consumer:%s"%name
						print "{0}'s trust value on the web service {1}:{2}".format(y['name'],j['name'],y['td'])
						print "\n"
						tdy = y['td']
						credibility = 0.5
						A += tdy * credibility
						B += credibility
					trx.insert(i,A/B)
					print trx[i]
					conforance = 0.5
					l = tdx[i] * 0.5 + trx[i] * 0.25 + tcx[i] * 0.25
					tx.insert(i,l)
					q = '''update WebServices set tf = {0} where id = {1} '''.format(j['id'],tx[i])
					db.query(q)
					print trx
		print trx
		q = '''select * from WebServices order by tf DESC limit 4'''
		newws = db.query(q) 
		for i in newws:
			print "\n"
			print "Web Service {0} has Trust value:{1}".format(i['name'],i['tf'])
		#db.query('''commit''')
	except KeyboardInterrupt:
		print 'You cancelled the execution ..!!'
		sys.exit(1)
	except IOError:
		print 'Error: input error ..!!'
		sys.exit(1)
	except EOFError:
		print "Error!!! We reached end of the file while reading a line\n"
		sys.exit(1)