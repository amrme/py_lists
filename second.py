fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt" #good line, bad comment!

fh = open(fname)
count = 0
for line in fh:
	if line == "":  
		continue

	words = line.split()

	for word in words:
		# print words[0]
		if word != "From" or word == "From:":  
			continue

		count += 1
		print words[1]

print "There were", count, "lines in the file with From as the first word"
