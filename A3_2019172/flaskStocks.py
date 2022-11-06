# for runs simply run that file
# I assumed 52 weeks as general year not as Leap year
from flask import *
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import glob
import os
from datetime import timedelta

app = Flask(__name__)

stlist = os.listdir("static/archive")
for i in range(len(stlist)):
    stlist[i] = stlist[i].split('.')[0]

path = 'static/archive/'
all_files=glob.glob(path+"/*.csv")

all_files

max = None
min = None
error = None

def isValid(date):
    global error
    global max
    global min
    day,month,year = date.split('/')
    day=int(day)
    month=int(month)
    year=int(year)

    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        max_days=31
    elif month==4 or month==6 or month==9 or month==11:
        max_days=30
    elif year%4==0 or year%100!=0 or year%400==0:
        max_days=29
    else:
        max_days=28
    
    if month<1 or month>12:
        max = None
        min = None
        error='pls Check Month, Date is Invalid!'
        return False
    elif day<1 or day>max_days:
        max = None
        min = None
        error='pls Check Day, Date is Invalid!'
        return False
    else:
        return True

def solve(x):
    global max
    global min
    global error
    StockName = x['StockName']
    StartDate = x['StartDate']
    EndDate = x['EndDate']
    
    if(len(StartDate)==0):
        max = None
        min = None
        error='pls Enter the StartDate!'
        return
    elif(isValid(StartDate)==False):
        return
    elif(len(EndDate)>0 and (isValid(EndDate)==False)):
        return

    bef_str = 'static/archive\\'
    aft_str = '.csv'

    final_str = "".join((bef_str,StockName,aft_str))

    li = []
    
    for filename in all_files:
        if(filename==final_str):
            print(filename)
            df = pd.read_csv(filename, usecols=['Date','Symbol','Close'],index_col=None, header=0)
            li.append(df)
            break

    frame = pd.concat(li, axis=0, ignore_index=True)
    # print(frame)
    frame.Date=pd.to_datetime(frame.Date, utc= True)

    if(len(EndDate)==0):
        start_date = pd.to_datetime(StartDate, dayfirst = True,utc= True)
        dt = start_date - timedelta(364)
        dt = pd.to_datetime(dt, dayfirst = True,utc= True)
        ans = frame[frame.Date.between(dt,start_date)]

        if(len(ans)==0):
            max = None
            min = None
            error = 'No Data Exist'
            return
        else:
            error = None
        
        print(len(ans))
        max = ans['Close'].loc[ans['Close'].idxmax()]      # Maximum in column
        # print(max)

        min = ans['Close'].loc[ans['Close'].idxmin()]      # Minimum in column
        # print(min)

    else:
        if(pd.Timestamp(StartDate)>pd.Timestamp(EndDate)):
            max = None
            min = None
            error = 'StartDate must be smaller than EndDate'
            return
        else:
            error = None
        
        start_date = pd.to_datetime(StartDate, dayfirst = True,utc= True)
        end_date = pd.to_datetime(EndDate, dayfirst = True,utc= True)

        ans = frame[frame.Date.between(start_date, end_date)]

        if(len(ans)==0):
            max = None
            min = None
            error = 'No Data Exist'
            return
        else:
            error = None
        
        print(len(ans))

        max = ans['Close'].loc[ans['Close'].idxmax()]      # Maximum in column
        # print(max)

        min = ans['Close'].loc[ans['Close'].idxmin()]      # Minimum in column
        # print(min)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        x = request.form
        solve(x)
    return render_template('index.html',stocks=stlist,Highest=max,Lowest=min,Error=error)

if __name__ == "__main__":
    app.run(debug=True)