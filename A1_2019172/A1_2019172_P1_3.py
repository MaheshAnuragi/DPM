#I am importing a csv for reading a csv file
import csv
stops = list(csv.DictReader(open('stops.txt','r')))

# taking the input of threshold distance and StopId
t = input("Enter a threshold distance: ")
stopID = input("Enter a stop_ID: ")

#here i importing a geopy for calculting a distance
from geopy.distance import distance

row = len(stops) #row of length

fRow = 0

for i in range(row):
  if(stops[i]['	stop_id']==stopID):   #it findings a row of stopId which is given
      fRow=i

#print(fRow)

fRow4 = 0
for i in range(row):
  dist = distance((stops[fRow]['stop_lat'],stops[fRow]['stop_lon']),    # calculating a distance from 
                    (stops[i]['stop_lat'],stops[i]['stop_lon']))      # from given stopID
  if(dist<=float(t)):                       
    print(stops[i]['	stop_id'])    # it prints the stopID that Distance which is smaller than 
                                    # or equals to threshold Distance
                              