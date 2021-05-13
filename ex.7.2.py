"""
7.2 Write a program that prompts for a file name, then opens that file and reads
through the file, looking for lines of the form:
           X-DSPAM-Confidence:    0.8475
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
"""
#python :

fname = input(" Inter file name : ")
try:
    fhand = open(fname)
except:
    print("file, [", fname, "] is not found")
    exit()
count = 0
sum = 0
for line in fhand :
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        print(line)
        pos = line.find(':')
        #print(pos)
        digits = line[19:]
        strip = digits.strip()
        #print(strip)
        sum = float(strip) + float(sum)
#print("Average spam confident: ", float(sum/count))
