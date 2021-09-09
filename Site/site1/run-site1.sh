delay(5)
nfdc face create udp://192.168.1.2
nfdc face create udp://192.168.2.2
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-site1.conf