"""
10.2 Write a program to read through the mbox-short.txt and
figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time
and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below. Note that the autograder
does not have support for the sorted() function.
"""
dict = dict()
try :
    fname = input("Inter file name : ")
except :
    print("file, [", fname "]is not found")
    exit()
fhand = open(fname)
for line in fhand :
    if line.startswith('From '):
        line = line.split()
        #print(line)
        time = line[5]
        #print(time)
        time = time.split(':')
        hour = time[0]
        dict[hour] = dict.get(hour,0) + 1
    else :
        continue
list = sorted(dict.items())
print(list)
