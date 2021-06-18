# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:48:42 2019

@author: lukek
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:48:45 2019

@author: lukek
"""

import os
import zipfile
import shutil
import csv
import time
#example of how it works


zip_location=r"C:\Users\lukek\Desktop\Python\airplane"
csv_location=r"C:\Users\lukek\Desktop\SQL\huge datasets\Airplane data"

names=[]
num=0
os.chdir(zip_location)
for zfile in os.listdir(zip_location):
     if zfile.endswith(".zip") and 'ONTIME_REPORTING' in zfile:
         names.append(os.path.abspath(zfile))
 
for i in range(0,len(names)):
    zzip= zipfile.ZipFile(os.path.abspath(names[i]))
    zzip.extractall(csv_location)
    zzip.close()
    print('done')
    
        
znum=0 

for i in os.listdir(zip_location): 
    os.chdir(zip_location)      
    zzip= zipfile.ZipFile(os.path.abspath(i))
    zzip.extractall(csv_location)   
    os.chdir(csv_location)
    for csvname in os.listdir():
        if 'ONTIME_REPORTING' in csvname:
            with open(csvname) as csvfile:
                filereader=csv.reader(csvfile)
                str(next(filereader)[0])
                try:
                        year=str(next(filereader)[0])
                        month=str(next(filereader)[1])
                        csvfile.close()
                        newname=str(znum)+'airplane year ' + str(year) + ' month ' +str(month) +".csv"
                        os.rename(csvname, newname)
                        print('extracted ' + str(csvname) + ' from ' + str(i) + ' as ' + str(newname))
                        csvfile.close()
                        zzip.close()
                        znum=znum+1
                except:
                    print('no more data in file')
                    csvfile.close()
                    zzip.close()
                    