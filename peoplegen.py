#!/usr/bin/python
import sys
import urllib2
import random
random.seed()


def namegen (Namearry):
	nmrand = random.randrange(1,len(Namearry)+1)
	name = Namearry[nmrand - 1]
	return name

def phonegen ():
	randnum = random.randrange(1,4)
	phon1 = '%03d' % random.randrange(0,999)
	phon2 = '%04d' % random.randrange(0,9999)
	if randnum == 1:
		return "931-" + str(phon1) + "-" + str(phon2)
	elif randnum == 2:
		return "(931) " + str(phon1) + "-" + str(phon2)
	elif randnum == 3:
		return "931" + str(phon1) + str(phon2)


inpnum = int(sys.argv[1])

lastnm = []	
req = urllib2.Request("http://www.census.gov/genealogy/names/dist.all.last")
resp = urllib2.urlopen(req)
for line in resp:
	lastnm.append(line.partition(" ")[0])

resp.close()

firstnm = []

req1 = urllib2.Request("http://www.census.gov/genealogy/names/dist.male.first")
resp1 = urllib2.urlopen(req1)

for line in resp1:
	firstnm.append(line.partition(" ")[0])
resp1.close()

req2 = urllib2.Request("http://www.census.gov/genealogy/names/dist.female.first")
resp2 = urllib2.urlopen(req2)
for line in resp2:
	firstnm.append(line.partition(" ")[0])
resp2.close()

outfile = []
count = 0

while ( count < inpnum ):
	suffix = [" Jr."," Sr."," III"]

#a pseudo-random number to see if a suffix is used or not
	chance = random.random()
#chance that a person has a middle name
	middlechance = random.random()

	if chance > 0.5:
		suffixrand = random.randrange(1,4)
		suffix = suffix[suffixrand - 1]
	else:
		suffix = ""

	ini = ""
	mi = ""
	firstnme = namegen(firstnm)
	lastnme = namegen(lastnm)
	mi = firstnme[:1]
	if middlechance > 0.63:
		middlerand = random.randrange(1,4)
		for i in range(1,middlerand + 1):
			if i == 1:
				ini = namegen(firstnm) + " "
				mi += ini[:1]
			else:
				comp = namegen(firstnm)
				ini +=  comp + " "
				mi += comp[:1]
	else:
		ini = ""

	emailaddy = mi.lower() + lastnme.lower()
	emailaddy += "@tntech.edu"
	full = firstnme + " " + ini + lastnme + suffix

	s = set([])
	tid = ""
	i = 0
	idg = random.randrange(00000,100000)
	if idg not in s:
		tid = "T" + str(idg)
		s.add(idg)
	else:
		idg = random.randrange(00000,100000)
		if idg not in s:
			tid = "T" + str(idg)
			s.add(idg)

	phoner1 = phonegen()
	phoner2 = phonegen()
	phoner3 = phonegen()
	complete = full + "," + tid + "," + emailaddy + "," + "{" + phoner1 + "," + phoner2 + "," + phoner3 + "}" + ",CSC" + "\n"
	outfile.append(complete )
	count += 1

for x in range(0,len(outfile)):
	sys.stdout.write(outfile[x])
