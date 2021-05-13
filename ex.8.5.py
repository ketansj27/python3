"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
"""
# outpot = There were 27 lines in the file with From as the first word

#python

fname = input("Inter file name : ")
try :
    fhand = open(fname)
except :
    print("file, [", fname, "] is not found")
count = 0
for line in fhand :
    if line.startswith('From ') :
        #print(line)
        count = count + 1
        line = line.split()
        print(line[1])
print("There were", count, "lines in the file with From as the first word")
