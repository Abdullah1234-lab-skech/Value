import random 
import time 
def getRandomdate(startdate, enddate):  
    print('Printing random date between',startdate,'and',enddate) 
    randomGenerater=random.random() 
    dateformat= '%m/%d/%Y' 
    startTime=time.mktime(time.strptime(startdate,dateformat)) 
    endtime=time.mktime(time.strptime(enddate,dateformat)) 
    randomtime=startTime + randomGenerater*(endtime-startTime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime)) 
    return randomdate
print('Random date =',getRandomdate('1/1/2016','12/12/2016')) 
