# read a file
# split it up into words
# append all new words in the file to a list
# sort that list
# print that sorted list

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    # split line
    listed_line = line.split()
    # print listed_line
    for word in listed_line:
        # print word
        if word in lst:
                # print "yuo"
                continue

        lst.append(word)
        # print "appended"
        # print lst



sorted_list = sorted(lst)

print sorted_list