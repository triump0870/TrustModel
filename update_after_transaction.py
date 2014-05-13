import sys
def error():
	print "\nError!!! You entered wrong values\n"
	sys.exit(1)
for i in range(service):
	r = input("Enter your rating[1-5]:")
	s = input("Enter your satisfaction(0/1):")
	rating = r if 0<r<6 else error()
	satisfaction = s if s==0 or s==1 else error()
	Ns = 0
	N = 0
	if 1 in satisfaction:
		Ns += 1
		N += 1
	elif 0 in satisfaction:
		N = 1
