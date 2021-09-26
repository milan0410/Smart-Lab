from datetime import datetime
def assign(status,names,name1):
    for i in range(6):
        if status[i]==0:
            status[i]=1
            names[i]=name1
            return i+1
def deassign(status,names,name1):
    for i in range(6):
        if names[i]==name1:
            status[i]=0
            names[i]="unassigned"
            return i+1
        
def available(status):
    if status.count(1)==6:
        return 0
    else:
        return 1
