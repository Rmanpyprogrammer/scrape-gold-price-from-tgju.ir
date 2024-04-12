import requests 
import json
from colorama import Fore
from time import sleep
from datetime import datetime,timedelta
import re


gold_url = "https://www.tgju.org/profile/geram18"

urlBackEnd = "http://127.0.0.1:5042/api-gold/"



Response = requests.get(url=gold_url)
if Response.status_code == 200:

    Data =  Response.text
    res=re.findall(r"<td class=\"text-left\">(\d*,\d*,\d*)<\/td>",Data)
    res=int(res[0].replace(",",""))

    print(Fore.YELLOW + "data scraped")
    
    SendToBackEnd = requests.post(urlBackEnd , json=res)
    if SendToBackEnd.status_code == 201:
        print(Fore.GREEN +"kar jame")
    else :
        print(SendToBackEnd.status_code)
        print(Fore.RED + "error")
        
 
 
else:
    print(Fore.RED +"error")
    print(Response.status_code)
