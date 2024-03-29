import pandas as pd
import os
import sys

def main():

    if len(sys.argv) <= 1:
        print(f'Usage: {sys.argv[0]} <filename>')
        exit(0)

    filename = sys.argv[1]

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
        if i == data['root'][0] :
            file.write("\nsecurity\n{\n  validator\n  {\n    rule\n    {\n      id \"NLSR Hello Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<nlsr><INFO>]*<nlsr><INFO><><>$\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          hyper-relation\n          {\n            k-regex ^([^<KEY><nlsr>]*)<nlsr><KEY><>{1,3}$\n            k-expand \\\\1\n            h-relation equal\n            p-regex ^([^<nlsr><INFO>]*)<nlsr><INFO><><>$\n            p-expand \\\\1\n          }\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR LSA Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<nlsr><LSA>]*<nlsr><LSA>\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          hyper-relation\n          {\n            k-regex ^([^<KEY><nlsr>]*)<nlsr><KEY><>{1,3}$\n            k-expand \\\\1\n            h-relation equal\n            ; the last four components in the prefix should be <lsaType><seqNo><version><segmentNo>\n            p-regex ^<localhop>([^<nlsr><LSA>]*)<nlsr><LSA>(<>*)<><><><>$\n            p-expand \\\\1\\\\2\n          }\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR datasets\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<nlsr>]*<nlsr>[<lsdb><routing-table>]\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          hyper-relation\n          {\n            k-regex ^([^<KEY>]*)<KEY><>{1,3}$ ; router key or certificate\n            k-expand \\\\1\n            h-relation equal\n            p-regex ^([^<nlsr>]*)<nlsr>[<lsdb><routing-table>]\n            p-expand \\\\1\n          }\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR Hierarchy Exception Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<KEY><%C1.Router>]*<%C1.Router>[^<KEY><nlsr>]*<KEY><><><>$\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          hyper-relation\n          {\n            k-regex ^([^<KEY><%C1.Operator>]*)<%C1.Operator>[^<KEY>]*<KEY><>{1,3}$\n            k-expand \\\\1\n            h-relation equal\n            p-regex ^([^<KEY><%C1.Router>]*)<%C1.Router>[^<KEY>]*<KEY><><><>$\n            p-expand \\\\1\n          }\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR Hierarchical Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<KEY>]*<KEY><><><>$\n      }\n      checker\n      {\n        type hierarchical\n        sig-type ecdsa-sha256\n      }\n    }\n\n    trust-anchor\n    {\n      type any\n    }\n  }\n\n  prefix-update-validator\n  {\n    rule\n    {\n      id \"NLSR ControlCommand Rule\"\n      for interest\n      filter\n      {\n        type name\n        ; /<prefix>/<management-module>/<command-verb>/<control-parameters>\n        ; /<timestamp>/<random-value>/<signed-interests-components>\n        regex ^<localhost><nlsr><prefix-update>[<advertise><withdraw>]<><><>$\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          regex ^([^<KEY><%C1.Operator>]*)<%C1.Operator>[^<KEY>]*<KEY><>{1,3}$\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR Hierarchy Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<KEY>]*<KEY><><><>$\n      }\n      checker\n      {\n        type hierarchical\n        sig-type ecdsa-sha256\n      }\n    }\n\n    trust-anchor\n    {\n      type any\n    }\n  }\n}")
        else :
            file.write("\nsecurity\n{\n  validator\n  {\n    rule\n    {\n      id \"NLSR Hello Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<nlsr><INFO>]*<nlsr><INFO><><>$\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          hyper-relation\n          {\n            k-regex ^([^<KEY><nlsr>]*)<nlsr><KEY><>{1,3}$\n            k-expand \\\\1\n            h-relation equal\n            p-regex ^([^<nlsr><INFO>]*)<nlsr><INFO><><>$\n            p-expand \\\\1\n          }\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR LSA Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<nlsr><LSA>]*<nlsr><LSA>\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          hyper-relation\n          {\n            k-regex ^([^<KEY><nlsr>]*)<nlsr><KEY><>{1,3}$\n            k-expand \\\\1\n            h-relation equal\n            ; the last four components in the prefix should be <lsaType><seqNo><version><segmentNo>\n            p-regex ^<localhop>([^<nlsr><LSA>]*)<nlsr><LSA>(<>*)<><><><>$\n            p-expand \\\\1\\\\2\n          }\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR datasets\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<nlsr>]*<nlsr>[<lsdb><routing-table>]\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          hyper-relation\n          {\n            k-regex ^([^<KEY>]*)<KEY><>{1,3}$ ; router key or certificate\n            k-expand \\\\1\n            h-relation equal\n            p-regex ^([^<nlsr>]*)<nlsr>[<lsdb><routing-table>]\n            p-expand \\\\1\n          }\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR Hierarchy Exception Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<KEY><%C1.Router>]*<%C1.Router>[^<KEY><nlsr>]*<KEY><><><>$\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          hyper-relation\n          {\n            k-regex ^([^<KEY><%C1.Operator>]*)<%C1.Operator>[^<KEY>]*<KEY><>{1,3}$\n            k-expand \\\\1\n            h-relation equal\n            p-regex ^([^<KEY><%C1.Router>]*)<%C1.Router>[^<KEY>]*<KEY><><><>$\n            p-expand \\\\1\n          }\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR Hierarchical Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<KEY>]*<KEY><><><>$\n      }\n      checker\n      {\n        type hierarchical\n        sig-type ecdsa-sha256\n      }\n    }\n\n    trust-anchor\n    {\n      type any\n    }\n  }\n\n  prefix-update-validator\n  {\n    rule\n    {\n      id \"NLSR ControlCommand Rule\"\n      for interest\n      filter\n      {\n        type name\n        ; /<prefix>/<management-module>/<command-verb>/<control-parameters>\n        ; /<timestamp>/<random-value>/<signed-interests-components>\n        regex ^<localhost><nlsr><prefix-update>[<advertise><withdraw>]<><><>$\n      }\n      checker\n      {\n        type customized\n        sig-type ecdsa-sha256\n        key-locator\n        {\n          type name\n          regex ^([^<KEY><%C1.Operator>]*)<%C1.Operator>[^<KEY>]*<KEY><>{1,3}$\n        }\n      }\n    }\n\n    rule\n    {\n      id \"NLSR Hierarchy Rule\"\n      for data\n      filter\n      {\n        type name\n        regex ^[^<KEY>]*<KEY><><><>$\n      }\n      checker\n      {\n        type hierarchical\n        sig-type ecdsa-sha256\n      }\n    }\n\n    trust-anchor\n    {\n      type any\n    }\n  }\n}")
        file.close
        
        #Generate initial
        file = open(filename+"/"+i+"/initial-"+i+".sh","wb")
        string = "\nndnsec-key-gen /ndn/%s > site.key\nndnsec-cert-gen -s /ndn/ site.key > site.cert\nndnsec-cert-install -f site.cert\n" % i + "\nndnsec-key-gen /ndn/%s/%%C1.Operator/op > operator.key \nndnsec-cert-gen -s /ndn/%s operator.key > operator.cert \nndnsec-cert-install -f operator.cert" % (i,i) + "\n\nndnsec-key-gen /ndn/%s/%%C1.Router/router > router.key \nndnsec-cert-gen -s /ndn/%s/%%C1.Operator/op router.key > router.cert \nndnsec-cert-install -f router.cert" % (i,i) + "\nsudo cp /usr/local/etc/ndn/nfd.conf.sample /usr/local/etc/ndn/nfd.conf"	
        file.write(string.encode())
        file.close

        #Generate run
        file = open(filename+"/"+i+"/run-"+i+".sh","wb")
        x = 0
        string = ""
        for s in data['site'] :
            if s == i :
                string = string + "\nnfdc face create udp://%s" % data['neighbor ip'][x]
            x+=1
        string = string + "\nsudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-%s.conf" % i
        file.write(string.encode())
        file.close

if __name__ == '__main__':
    main()
