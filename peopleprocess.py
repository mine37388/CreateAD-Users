#!/usr/bin/python
import sys
listarr = []
listarr = sys.stdin.readlines()
	
for i in range(0,len(listarr)):
	stra = ""
	stra = listarr[i].rstrip('\n')
	name = ""
	uid = ""
	email = ""
	phone1 = ""
	phone2 = ""
	phone3 = ""
	depart = ""
	user = ""
	name = stra.split(",")[0]
	uid = stra.split(",")[1]
	email = stra.split(",")[2]
	user = email[0:email.find('@')]
	phone1 = stra.split(",")[3].lstrip('{')
	phone2 = stra.split(",")[4]
	phone3 = stra.split(",")[5].rstrip('}')
	depart = stra.split(",")[6]
        info = name + "," + email + "," + phone1 + "," + phone2 + "," + phone3 + "," + depart
	print "adduser -p " + uid + " -c " + "\"" + info + "\"" + " " + user
