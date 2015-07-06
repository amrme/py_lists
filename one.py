
# read a file
# split it up into words
# 

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()


for line in fh:
    # split line
    listed_line = line.split()
    for word in listed_line:
        if word in listed_line: 
            continue
    	lst.append(word)
      
sorted_list = lst.sort()
    
print sorted_list
