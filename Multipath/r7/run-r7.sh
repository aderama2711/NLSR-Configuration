sudo mkdir /var/lib/nlsr

nfdc face create udp://192.168.1.25
nfdc face create udp://192.168.1.54
sudo NDN_LOG='nlsr.*=DEBUG' nlsr -f nlsr-r7.conf