# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 00:42:41 2019

@author: lukek
"""

import requests, bs4
import selenium
from selenium import webdriver
import time
import shutil, os
#downloadbox=driver.find_element_by_name('Download')
#using chrome
#define driver


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
prefs = {"profile.default_content_settings.popups": 0,
"download.default_directory": r"C:\Users\lukek\Desktop\Python\airplane\\",
"directory_upgrade": True}
options.add_experimental_option("prefs", prefs)
driver=webdriver.Chrome(executable_path=r'C:\Users\lukek\Desktop\Python\chromedriver.exe', options=options)


#open website
driver.get('https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time')
checkbox=['\'YEAR\'','\'MONTH\'', '\'DAY_OF_MONTH\'','\'FL_DATE\'',	'\'ORIGIN\'', '\'ORIGIN_CITY_NAME\'','\'ORIGIN_STATE_ABR\'','\'DEST\'', '\'DEST_CITY_NAME\'','\'DEST_STATE_ABR\'', '\'DEP_TIME\'', '\'DEP_DELAY\'', '\'ARR_TIME\'', '\'ARR_DELAY\'', '\'CANCELLED\'', '\'AIR_TIME\'', '\'DISTANCE\'', '\'CARRIER_DELAY\'', '\'WEATHER_DELAY\'', '\'NAS_DELAY\'','\'SECURITY_DELAY\'', '\'LATE_AIRCRAFT_DELAY\'']
paths=[]
year=[]
for i in range(0,10):
    year.append(str(201)+str(i))
months=['\'January\'','\'February\'','\'March\'','\'April\'','\'May\'','\'June\'','\'July\'','\'August\'','\'September\'','\'October\'','\'November\'','\'December\'']

for i in range(0,len(checkbox)):
    paths.append("//input[@type='checkbox' and @value=" + checkbox[i]  +   "]")  
#

element = driver.find_element_by_xpath("//input[@type='checkbox' and @id='DownloadZip']").click()
element = driver.find_element_by_xpath("//input[@type='checkbox' and @id='DownloadZip']").click()

#

#click all columns needed
for j in range(0,len(paths)):
    driver.find_element_by_xpath(paths[j]).click()
    time.sleep(.006)

#select year


for yr in range(2012,2020):
    driver.find_element_by_xpath("//select[@id='XYEAR']/option[text()=" +str(yr) +"]" ).click()
    for month in months:
        driver.find_element_by_xpath("//select[@id='FREQUENCY']/option[text()=" +str(month) +"]" ).click()
        for dfile in os.listdir(r"C:\Users\lukek\Desktop\Python\airplane"):
            while dfile.endswith('.crdownload'):
                if dfile in os.listdir(r"C:\Users\lukek\Desktop\Python\airplane"):
                    continue
                break
        driver.find_element_by_name("Download").click()
        print('Saved File for' + str(month)+ ' '+str(yr))
        time.sleep(.06)
    
    #time.sleep(.2)




        



#driver.find_element_by_name("Download").click()
# =============================================================================
# for yr in range(2004,2010):
#     print(yr)
#     for month in months:
#         print(month)
# =============================================================================