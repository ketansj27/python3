"""
The basic outline of this problem is to read the file, look for integers using
the re.findall(), looking for a regular expression of '[0-9]+' and then
converting the extracted strings to integers and summing up the integers.

Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt
(There are 87 values with a sum=445822)
Actual data: http://python-data.dr-chuck.net/regex_sum_201873.txt
(There are 96 values and the sum ends with 156)
"""
import re
sum = 0
count = 0
fname = input("Inter file name : ")
try :
    fhand = open(fname)
except :
    print("file, [", fname,"] is not found")
    exit()
for line in fhand :
    line = re.findall('[0-9]+',line)
    #print(value)
    for num in line :
        count = count + 1
        sum = int(num) + sum
print(sum)
print(count)
