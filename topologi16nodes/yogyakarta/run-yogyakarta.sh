sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.49
nfdc face create udp://192.168.1.54
nfdc face create udp://192.168.1.58
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-yogyakarta.conf