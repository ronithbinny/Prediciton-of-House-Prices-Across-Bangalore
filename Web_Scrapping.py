import bs4
import requests
import pandas as pd
import numpy as np
import re

place = []
price = []
carpet_area = []
bedroom = []
possession = []
floor = []
bathroom = []
parking = []
powerbackup = []
security = []
swimmingpool = []


for x in range(1,100) :
    
    print(x)
    
    res = requests.get("https://www.commonfloor.com/bangalore-property/for-sale?page={}".format(x))
    
    soup = bs4.BeautifulSoup(res.text, "html")
    
    #Place,Carpet Area, Possessopn, Floor, Bathroom
    for i in range(0,len(soup.find_all("div",{"class" : "snb-tile-info"})) * 2) :
        
        try :
            place.append(soup.find_all("a",{"class" : "gtloc"})[i].text)
        except :
            pass
        try :
            carpet_area.append((soup.find_all("div",{"class" : "inforow"})[i].find_all("div",{"class" : "infodata"})[0].find("span").text)[2:].strip())
        except :
            pass
        try :
            possession.append(soup.find_all("div",{"class" : "inforow"})[i].find_all("div",{"class" : "infodata"})[1].find("span").text)
        except :
            pass
        try :
            floor.append(soup.find_all("div",{"class" : "inforow"})[i].find_all("div",{"class" : "infodata"})[2].find("span").text)
        except :
            pass
        try :  
            bathroom.append(soup.find_all("div",{"class" : "inforow"})[i].find_all("div",{"class" : "infodata"})[3].find("span").text)
        except :
            pass
        
        if i < len(soup.find_all("div",{"class" : "snb-tile-info"})) :  
            
            #Bedroom
            xx = str(soup.find_all("div",{"class" : "st_title"})[i].text.strip())
        
            p = ((re.findall("\d+", xx)))
            try :
                bedroom.append(p[0])
            except :
                No = 0
                bedroom.append(No) 
            
            #Price
            try :
                price.append((soup.find_all("div",{"class" : "p_section"})[i].find_all("span")[1].text)[2:].strip())
            except :
                price.append("NA")
            
            # Pool,Security,PowerBackup and Parking
            aa = str(type((soup.find_all("div",{"class" : "snb-tile-info"})[i].find("div",{"class" : "inforow pull-right infoline"}))))
            
            if aa == "<class 'NoneType'>" :
                No = 0
                parking.append(No)
                security.append(No)
                powerbackup.append(No)
                swimmingpool.append(No)
                
            else :
                nam = []
                    
                for w in range(0,4) :
                    try :
                        am = ((soup.find_all("ul",{"class" : "i_l"})[i].find_all("li",{"class" : "na"})[w]).text).strip()
                        nam.append(am)
                    except :
                        pass
                No = 0
                Yes = 1
                if "Parking" in nam :
                    parking.append(No)
                else :
                    parking.append(Yes)
                    
                if "Security" in nam :
                    security.append(No)
                else :
                    security.append(Yes)
                        
                if "Power Backup" in nam :
                    powerbackup.append(No)
                else :
                    powerbackup.append(Yes)
                        
                if "Swimming Pool" in nam :
                    swimmingpool.append(No)
                else :
                    swimmingpool.append(Yes)
            


submission = pd.DataFrame({"Location" : place, "Price" : price, "Carpet Area" : carpet_area,
                           "Bedroom" : bedroom, "Bathroom" : bathroom, "Floor" : floor, 
                           "Parking" : parking, "Security" : security, "Power-Backup" : powerbackup,
                           "Pool" : swimmingpool, "Possession" : possession})
     
filename = "commonfloor-01.csv"

submission.to_csv(filename, index = False)
