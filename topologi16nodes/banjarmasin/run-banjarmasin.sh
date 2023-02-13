sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.37
nfdc face create udp://192.168.1.69
nfdc face create udp://192.168.1.78
nfdc face create udp://192.168.1.82
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-banjarmasin.conf