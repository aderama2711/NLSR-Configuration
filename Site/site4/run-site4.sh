delay(5)
nfdc face create udp://192.168.2.1
nfdc face create udp://192.168.4.1
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-site4.conf