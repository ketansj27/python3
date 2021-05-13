"""
9.4 Write a program to read through the mbox-short.txt and figure out who has
the most commits. The program looks for 'From ' lines and takes the second word
of those lines as the person who sent the mail. The program creates a Python
dictionary that maps the senders mail address to a count of the number of times
they appear in the file. After the dictionary is produced, the program reads
through the dictionary using a maximum loop to find the most prolific committer.
"""

#output
#cwen@iupui.edu 5

mail = dict()
Max_add = None
count = 0
fname = input("Enter file name : ")
fhand = open(fname)
for line in fhand :
    if line.startswith('From '):
        line = line.split()
        M_add = line[1]
        mail[M_add] = mail.get(M_add,0) + 1
    else :
        continue
for (add,value) in mail.items():
    if value > count :
        count = value
        Max_add = add
print(Max_add,count)
