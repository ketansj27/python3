"""

7.1 Write a program that prompts for a file name, then opens that file and reads
through the file, and print the contents of the file in upper case. Use the file
words.txt to produce the output below.
You can download the sample data at http://www.pythonlearn.com/code/words.txt

"""

#python :

fname = input(" Inter file name : ")
try :
    fhand = open(fname)
except :
    print("file, [", fname, "] is not found")
    exit()
for line in fhand :
    line = line.rstrip()
    print(line.upper())
