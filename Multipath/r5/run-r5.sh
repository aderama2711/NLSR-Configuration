sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.17
nfdc face create udp://192.168.1.46
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-r5.conf