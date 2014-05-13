import Database
import sys
def error():
	print "\nError!!! You entered wrong values\n"
	
if __name__=='__main__':
	db = Database.Database()
	q = "select * from WebServices"
	p = db.query(q)
	N = 0
	Ns = 0
	print type(p)
	for i in p:
		print type(i)
		print "Id=%s"%i['name']
		r = input("\nEnter raing for the above web service[1-5]:")
		s = input("\nAre you satisfied with the service (1 for YES and 0 for NO):")
		if 0<r<6:
			raing=r
		else:
			continue
		if s==0 or s==1:
			satisfaction = s 
		else:
			continue
		N += 1
		if satisfaction == 1:
			print "satisfaction=%s"%satisfaction
			Ns += 1
		p = Ns/N
		print "usefulness:%s"% p
