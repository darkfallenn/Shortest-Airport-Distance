
import csv
import math
def deg_to_rad(deg):
    return deg*(math.pi/180)
def calculate_distance(a,b):
    #distance calculation according to Haversine formula
    new_listo=[]
    new_listo.extend(a)
    new_listo.extend(b)
    R=6371
    dis_lat=deg_to_rad(new_listo[5]-new_listo[1])
    dis_lon=deg_to_rad(new_listo[4]-new_listo[0])
    a=math.sin(dis_lat/2)**2+math.cos(deg_to_rad(new_listo[5])*math.cos(deg_to_rad(
                                                                          new_listo[5])))*math.sin(
                                                                                          dis_lon/2)**2
    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a));
    d=R*c
    print("Distance from destination {}-{} to destination {}-{} is {} km".format(new_listo[2],new_listo[3],new_listo[6],new_listo[7],round(d,2)))
def route_fetcher(loc):
    
    f=open('routes.dat',encoding="utf-8")
    for row in csv.reader(f):
        a=[]
        b=[]
        try:     
            a=loc[row[3]]
            b=loc[row[5]]
            a.extend([row[3],row[2]])
            b.extend([row[5],row[4]])                       
            calculate_distance(a,b)
        except Exception:
            pass 
def content_retriever():
    listo=[] 
    location={}
    f=open('airports.dat',encoding="utf-8")
    for row in csv.reader(f):
        try:
            location[row[0]]=[float(row[6]),float(row[7])]
        except UnicodeEncodeError:
            pass
            
    return location   
if __name__=='__main__':           
    route_fetcher(content_retriever())
