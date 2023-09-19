import pandas as pd
import os

filename = "Thesis-CARI"

data = pd.read_excel(filename+".xlsx")
site=[]

for s in data['site'] :
    if s in site :
        continue
    else :
        site.append(s)

for i in site :
    dir = os.path.join(filename)
    if not os.path.exists(dir):
        os.mkdir(dir)
    dir = os.path.join(filename,i)
    if not os.path.exists(dir):
        os.mkdir(dir)
        
    #Generate netplan configuration
    file = open(filename+"/"+i+"/netplan-"+i+".conf","w")
    x = 0
    file.write("network:\n  version: 2\n  renderer: networkd\n  ethernets:\n    ens3:\n     dhcp4: yes\n")
    for s in data['site'] :
        if s == i :
            cps = int(data['interface'][x].split('eth')[1])
            file.write("    ens%s:\n     dhcp4: no\n     addresses: [%s/30]\n" % (str(cps+3),str(data['ip'][x])))
        x+=1
    file.close

    #Generate run
    file = open(filename+"/"+i+"/run-"+i+".sh","wb")
    x = 0
    string = ""
    for s in data['site'] :
        if s == i :
            string = string + "\nnfdc face create udp://%s" % data['neighbor ip'][x]
        x+=1
    string = string + "\necho $(date) > ~/timedate.log"
    file.write(string.encode())
    file.close
