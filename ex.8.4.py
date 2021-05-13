"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the
line into a list of words using the split() function. The program should build
a list of words. For each word on each line check to see if the word is already
in the list and if not append it to the list. When the program completes, sort
and print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
"""
#output:
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', #'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', #'through', 'what', 'window', 'with', 'yonder']

fname = input("Inter file name : ")
try :
    fhand = open(fname)
except:
    print("file, [",fname, "] is not found")
    exit()
w_list = list()
for line in fhand :
    line  = line.rstrip()
    lsplit = line.split()
    #print(lsplit)
    for word in lsplit :
        if word not in w_list :
            w_list.append(word)
        else :
            continue
w_list.sort()
print(w_list)
