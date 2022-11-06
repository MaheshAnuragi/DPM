#I am importing a csv for reading a csv file
import csv
stops = list(csv.DictReader(open('stops.txt','r')))

row = len(stops)  #row of length
fRow3 = 0       #they will store final row1 where will maxDistance comes
maxLen = 0

#runs a iteration
for i in range(row):
  stop_Len = len(stops[i]['stop_name'])  #calcuate the maxLength of stopName
  if(maxLen<stop_Len):    #here it stores the maxLength of stopName
    maxLen = stop_Len
    fRow3 = i           # here it stores the row of maxLength of stopName

#print(maxLen)

# print the stopName
print(stops[fRow3]['stop_name'])