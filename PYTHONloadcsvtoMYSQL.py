# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:52:01 2019

@author: lukek
"""

import mysql.connector
import pymysql
import os
pymysql.install_as_MySQLdb()
import MySQLdb
# other method conn=mysql.connector.connect(host="localhost",user="root",passwd="Baconpizza2!")


conn=pymysql.connect(host="localhost",user="root",passwd="Baconpizza2!",local_infile=True)
c=conn.cursor()
c.execute("use dataworld;")
c.execute("show tables;")
c.fetchall()
import csv

csv_location=r'C:/Users/lukek/Desktop/SQL/huge datasets/airplane'


num=0
os.chdir(csv_location)
for file in os.listdir(csv_location):
    myfile=open(file,'r')
    csv_data = csv.reader(myfile,delimiter=',')
    next(csv_data)
    for row in csv_data:
        row=row[:22]
        for i in range(1,22):
            if row[i]=='':
                row[i]=0
        c.execute("INSERT INTO Airplane(YEAR,MONTH,DAY_OF_MONTH,FL_DATE,ORIGIN,ORIGIN_CITY_NAME,ORIGIN_STATE_ABR,DEST,DEST_CITY_NAME,DEST_STATE_ABR,DEP_TIME,DEP_DELAY,ARR_TIME,ARR_DELAY,CANCELLED,AIR_TIME,DISTANCE,CARRIER_DELAY,WEATHER_DELAY,NAS_DELAY,SECURITY_DELAY,LATE_AIRCRAFT_DELAY) VALUES(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)", row)
        print('row done'+str(num))
        num=num+1
    myfile.close()

#close the connection to the database.

conn.commit()
conn.close()
c.execute("SET GLOBAL local_infile = 'ON';")
c.execute("SHOW GLOBAL VARIABLES LIKE 'local_infile';")



for csvv in os.listdir(csv_location):
    c.execute("""LOAD DATA local INFILE %s INTO TABLE airplane_2010 FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;""", csvv)
    conn.commit()
    print('Uploaded' + str(csvv))


---------------do it by year----------------------------
csv_location=r'C:/Users/lukek/Desktop/SQL/huge datasets/new'
os.chdir(csv_location)

conn=pymysql.connect(host="localhost",user="root",passwd="Baconpizza2!",local_infile=True)
c=conn.cursor()    
c.execute("use airplaneyear;")
conn.commit()

for csvv in os.listdir(csv_location):
    if '2010' in csvv:
        c.execute("""LOAD DATA local INFILE %s INTO TABLE airplane_2010 FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;""", csvv)
        conn.commit()
        print('Uploaded' + str(csvv))



