#I am importing a csv for reading a csv file
import csv
stops = list(csv.DictReader(open('stops.txt','r')))

#taking a dictionary for returning a answer
ans = {}

row = len(stops)  #row of length

for i in range(row):
  list_Value=[stops[i]['	stop_id']]  #here i create a list for adding a value
  key = stops[i]['stop_name']       # key which store a stop_name
  if( key in ans):                # if key present in dict then it will continue
    continue
  for j in range(row):          
    if(i!=j and stops[i]['stop_name']==stops[j]['stop_name']):  #if stop_name equals to another row of stop_Name
      list_Value.append(stops[j]['	stop_id'])                  #then it will add stopId in list
  if(len(list_Value)>1):                              # if list length grater than 1 
    ans[stops[i]['stop_name']]=list_Value           #then it will add on in Value of key

# here printing a answer
print(ans)