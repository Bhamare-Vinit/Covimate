import requests
import json
from datetime import datetime, timedelta
today = datetime.today()

pin = [""] #Enter Your Pincode. You can also enter multiple pincode by seperating them with a ,
num_day = 3      #Enter the number of days from today that you want to check the availability
all_dates = []
for i in range(num_day):
    all_dates.append(today + timedelta(i) )
    
final_dates = []
for i in all_dates:
    final_dates.append(i.strftime("%d-%m-%y"))

for p in pin:
    
    for d in final_dates:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}".format(p,d)
        
        result=requests.get(URL)

        json_result=result.json()

        if json_result["sessions"]:
            for center in json_result["sessions"]:
                if (center['available_capacity']>0):
                    print("pincode: "+str(center["pincode"]))
                    print("date: "+f"{today}")
                    print("Center Name: ", center["name"])
                    print("Center Address: ",center["address"])
                    print("No of Vaciness Avaliable: ", center["available_capacity"])
                    print("Vaccine Type:", center["vaccine"])
                    print("Minimum Age Limit:", center["min_age_limit"])
                    print("\n")

    