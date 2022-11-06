#I am importing a csv for reading a csv file
import csv
stops = list(csv.DictReader(open('stops.txt','r')))

#formulae for calculating a distance
def distance(x1, y1, x2, y2):     
    return (((x1-x2)**2) +  ((y1-y2)**2))**0.5;

row = len(stops)  #row of length
fRow1 = 0         #they will store final row1 where will maxDistance comes
fRow2 = 0
maxDistance = 0

#runs a iteration
for i in range(row):
  for j in range(i,row):
    # calcualting a distance by distance function
    dist = distance(float(stops[i]['stop_lat']),float(stops[i]['stop_lon']),
                    float(stops[j]['stop_lat']),float(stops[j]['stop_lon']))
    #here i store the maxDistance of fRow1 and fRow2
    if(maxDistance<dist):
      maxDistance=dist
      fRow1 = i
      fRow2 = j

#print(maxDistance)    

# printing the answer
print(stops[fRow1]['stop_name'])
print(stops[fRow2]['stop_name'])
