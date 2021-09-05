from datetime import *
from time import sleep
import re

host_path = r"/etc/hosts"  
redirect = "127.0.0.1"  
websites = ["www.facebook.com", "https://www.facebook.com"]  

def isGreaterThan(hourNow, minuteNow, restrictionHour, restrictionMinute):
    if hourNow > restrictionHour:
        return True
    elif hourNow == restrictionHour:
        if minuteNow >= restrictionMinute:
            return True
        else:
            return False
    else:
        return False


def isLessThan(hourNow, minuteNow, restrictionHour, restrictionMinute):
    if hourNow < restrictionHour:
        return True
    elif hourNow == restrictionHour:
        if minuteNow < restrictionMinute:
            return True
        else:
            return False
    else:
        return False

def addToFile(file, websites):
    with open(file, 'r+') as f:
        allLines = f.readlines()
        
        for website in websites:
            webRegex = re.compile(r'{0}'.format(website))
            match = webRegex.search(" ".join(allLines))
            if match != None:
                print("Match found")
            else:
                f.write(redirect+"    "+website+"\n")  

def deleteFromFile(file, websites):
    with open(file, 'r+') as f:
        allLines = f.readlines()
        newLines = allLines[:-len(websites)]
        
        for website in websites:
            webRegex = re.compile(r'{0}'.format(website))
            match = webRegex.search(" ".join(allLines))
            if match != None:
                f.truncate(0)
                f.seek(0,0)
                for line in newLines:
                    f.write(line)
            else:
                print("No match found")
    


startRestriction = datetime.strptime("11:00AM", "%I:%M%p")
startRestrictionHour = int(startRestriction.strftime("%H"))
startRestrictionMinute = int(startRestriction.strftime("%M"))

endRestriction = datetime.strptime("12:21PM", "%I:%M%p")
endRestrictionHour = int(endRestriction.strftime("%H"))
endRestrictionMinute = int(endRestriction.strftime("%M"))


while True:
    hourNow = int(datetime.now().strftime("%H"))
    minuteNow = int(datetime.now().strftime("%M"))
    
    print(hourNow)
    print(minuteNow)
    if isGreaterThan(hourNow, minuteNow, startRestrictionHour, startRestrictionMinute) and isLessThan(hourNow, minuteNow, endRestrictionHour, endRestrictionMinute):
        addToFile(host_path, websites)
        print("Restricted")
    elif isGreaterThan(hourNow, minuteNow, endRestrictionHour, endRestrictionMinute):
        deleteFromFile(host_path, websites)
        print("Restriction period over")
        break
    else:
        print("Restriction period has not started")
    
    sleep(5)
    
    
