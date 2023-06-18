import pandas as pd
import os

filename = "nlsrmininode"

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
    
    #Generate .conf
    file = open(filename+"/"+i+"/nlsr-"+i+".conf","w")
    file.write("general\n{\n  network /ndn/\n  site /%s\n  router /%%C1.Router/router\n\n  lsa-refresh-time 1800\n\n  lsa-interest-lifetime 4\n  \n  sync-protocol psync\n\n  sync-interest-lifetime 60000\n\n  state-dir       /var/lib/nlsr\n}" % i)
    file.write("\n\nneighbors\n{\n   hello-retries 3\n   \n   hello-timeout 1\n   \n   hello-interval  60\n\n  adj-lsa-build-interval 10\n\n  face-dataset-fetch-tries 3\n  \n  face-dataset-fetch-interval 3600\n")
    x = 0
    for s in data['site'] :
        if s == i :
            file.write("\n\n  neighbor\n  {\n    name /ndn/%s/%%C1.Router/router\n    face-uri  udp://%s\n    link-cost %s\n  }" % (data['neighbor'][x],data['neighbor ip'][x],data['link cost'][x]))
        x+=1
    file.write("\n}\n\nhyperbolic\n{\n\n  state off\n  \n  radius   123.456\n  angle    1.45,2.36\n}\n\nfib\n{\n  max-faces-per-prefix 3\n  \n  routing-calc-interval 15\n  \n}")
    file.write("\n\nadvertising\n{\n\n  prefix /ndn/%s/lab/ndn\n  \n}" % i)
    file.write("\nsecurity\n{\n  validator\n  {\n    trust-anchor\n    {\n      type any\n    }\n  }\n  prefix-update-validator\n  {\n    trust-anchor\n    {\n      type any\n    }\n  }\n}")
    file.close

    #Generate run
    file = open(filename+"/"+i+"/run-"+i+".sh","wb")
    x = 0
    string = "sudo mkdir /var/lib/nlsr\n"
    for s in data['site'] :
        if s == i :
            string = string + "\nnfdc face create udp://%s" % data['neighbor ip'][x]
        x+=1
    string = string + "\nsudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-%s.conf" % i
    file.write(string.encode())
    file.close
