import requests
import time
from datetime import datetime, date

f = open("ontime","r")
f1 = open("notontime","r")



API_URL = "https://api-v3.amtraker.com/v3/trains"


def make_api_request():
    response = requests.get(API_URL)  # Use authorized session
    data = response.json()
    return data
api_data = make_api_request()

print(api_data["7"][1]["stations"][10]["arrCmnt"])

com = api_data["7"][1]["stations"][10]["arrCmnt"]


fl1 = f.read()
fl2 = f1.read()




fl1i = int(fl1)
fl2i = int(fl2)


if com == "On Time":
    fl1p = str(fl1i + 1)
    fw = open("ontime","w")
    fw.write(fl1p)
    print(fl1)
else:
    fl2p = str(fl2i + 1)
    f1w = open("notontime","w")
    f1w.write(fl2p)
    print(fl2)

f.close()
f1.close()



