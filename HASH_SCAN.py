import os
import pathlib
import hashlib
import requests
import json
import wmi
from pathlib import Path
import pandas as pd


home = str(Path.home())
RES=home+"\results_exe"

liste =[]
f = wmi.WMI()
for process in f.Win32_Process():
    file_extension = pathlib.Path(process.Name).suffix
    if file_extension == '.exe':
        liste.append(process.Name)
    
BUF_SIZE = 32768
md5 = hashlib.md5()
sha1 = hashlib.sha1()



headers = {

    "Accept": "application/json",

    "x-apikey": "0f901f14014fb58f6ea58e0ea143366e519c015182329999c89eda8066eb855c"

}



def find(name):
    for root, dirs, files in os.walk("C:\\"):
        if name in files:
            return os.path.join(root, name)


with open(home+"/vt_Result_exe.txt",'a') as vt:
    vt.write ('Name,Harmless,Type Unsupported,Suspicious,Confirmed Timeout,Confirmed Timeout,Failure,Malicious,Undetected\n\n')

for i in range(len(liste)):
    path=find(liste[i])
    if type(path) == str:
        with open(path,"rb") as f:
            bytes = f.read()
            readable_hash = hashlib.md5(bytes).hexdigest();
        url = "https://www.virustotal.com/api/v3/search?query="
        url = url+readable_hash
        response = requests.get(url, headers=headers)
        x = json.loads(response.content)
        del x["links"]
        if len(x["data"]) != 0:
            data =  x["data"][0]["attributes"]["last_analysis_stats"]
            with open(home+"/vt_Result_exe.txt",'a') as vt:
                vt.write("{}".format(liste[i]))
                for value in data.values():
                    vt.write(',{}'.format(value))
                vt.write("\n")
            print("[{}/{}] DONE".format(i+1,len(liste)))
        else:
            with open(home+"/vt_Result_exe.txt",'a') as vt:
                vt.write("{},Built-in-Service".format(liste[i]))
                vt.write("\n")
            print("[{}/{}] DONE".format(i+1,len(liste)))
    else:
        with open(home+"/vt_Result_exe.txt",'a') as vt:
            vt.write("{},NOT FOUND".format(liste[i]))
            vt.write("\n")
        print("[{}/{}] DONE".format(i+1,len(liste)))
           
   
df = pd.read_csv("vt_Result_exe.txt", sep=',')
os.remove("vt_Result_exe.txt") 
df.to_csv('vt_Result_exe.csv', sep=',', index=False)
    
print("SCANNING COMPLETED")       
