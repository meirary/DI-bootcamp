import time
 
def minutes():
    m=0
    while m<=60:
        if m == 60:
            m-=60
        print(format(m,'02'))
        time.sleep(60)
        m+=1
 
def seconds():
    s=1
    while s<=60:
        if s == 60:
            s-=60
        print(format(s,'02'))
        time.sleep(1)
        s+=1
 
def hours():
    h=0
    while h<=24:
        if h == 24:
            h-=24
        print(format(h,'02'))
        time.sleep(3600)
        s+=1
        
print( '%s:%s:%s' %(hours(),minutes(),seconds()))
