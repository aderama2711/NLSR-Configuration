sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.19
nfdc face create udp://192.168.1.34
nfdc face create udp://192.168.1.36
nfdc face create udp://192.168.1.38
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-banjarmasin.conf